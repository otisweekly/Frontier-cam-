#!/usr/bin/env python3
"""
Frontier Film LUT Generator v2
Creates film-look transformation LUTs for digital photos

Approach: Identity mapping + Film characteristics
- Start with identity (input = output)
- Apply film tone curves (highlight rolloff, shadow lift)
- Apply color transformations (daylight vs tungsten)
- Film contrast (gentle S-curve)
- Preserve grain-friendly latitude
"""

import numpy as np
import json
from pathlib import Path

class FilmLUTGenerator:
    """Generate film-look LUTs for transforming digital photos"""

    def __init__(self, lut_size=33):
        self.lut_size = lut_size
        print(f"🎬 Initializing Film LUT Generator (size: {lut_size}x{lut_size}x{lut_size})")

    def srgb_to_linear(self, srgb):
        """Convert sRGB to linear RGB (gamma decode)"""
        return np.where(srgb <= 0.04045,
                       srgb / 12.92,
                       np.power((srgb + 0.055) / 1.055, 2.4))

    def linear_to_srgb(self, linear):
        """Convert linear RGB to sRGB (gamma encode)"""
        return np.where(linear <= 0.0031308,
                       linear * 12.92,
                       1.055 * np.power(linear, 1.0/2.4) - 0.055)

    def film_tone_curve(self, lum, shadow_lift=0.02, highlight_rolloff=0.12):
        """
        Film-characteristic tone curve
        - Lifts shadows (no crushed blacks)
        - Compresses highlights (soft rolloff like film)
        """
        # Shadow lift (gentle, film-like)
        if lum < 0.15:
            lift_amount = (0.15 - lum) / 0.15
            lum = lum + shadow_lift * lift_amount

        # Highlight compression (film rolloff)
        if lum > 0.75:
            rolloff_amount = (lum - 0.75) / 0.25
            compressed = 0.75 + (lum - 0.75) * (1 - rolloff_amount * highlight_rolloff)
            lum = compressed

        return np.clip(lum, 0, 1)

    def film_contrast_curve(self, value, strength=0.15):
        """
        Gentle S-curve for film-like contrast
        Not too aggressive - preserves grain latitude
        """
        # Simplified S-curve using tanh
        centered = (value - 0.5) * 2.0  # Center around 0
        curved = np.tanh(centered * (1 + strength))
        return (curved / 2.0) + 0.5

    def daylight_color_shift(self, rgb):
        """
        SUPRA daylight film characteristics
        - Slightly cool (natural daylight)
        - Clean, neutral rendering
        - Subtle blue lift in shadows
        """
        r, g, b = rgb

        # Get luminance for selective color grading
        lum = 0.2126 * r + 0.7152 * g + 0.0722 * b

        # Subtle blue lift in shadows (film characteristic)
        if lum < 0.3:
            shadow_amount = (0.3 - lum) / 0.3
            b = b + 0.02 * shadow_amount

        # Slightly warmer midtones (film prints tend to be slightly warm)
        if 0.3 <= lum <= 0.7:
            mid_amount = 1.0 - abs(lum - 0.5) / 0.2
            r = r + 0.01 * mid_amount
            g = g + 0.005 * mid_amount

        # Cool, clean highlights
        if lum > 0.7:
            highlight_amount = (lum - 0.7) / 0.3
            b = b + 0.01 * highlight_amount

        return np.clip([r, g, b], 0, 1)

    def tungsten_color_shift(self, rgb):
        """
        CHROME tungsten film characteristics
        - Warm color temperature (~3200K)
        - Amber/golden shift
        - Gentle warm glow in highlights
        """
        r, g, b = rgb

        # Get luminance
        lum = 0.2126 * r + 0.7152 * g + 0.0722 * b

        # Warm shift throughout (tungsten characteristic)
        r = r + 0.04
        g = g + 0.02
        b = b - 0.02

        # Extra warmth in midtones (where skin tones live)
        if 0.2 <= lum <= 0.6:
            mid_amount = 1.0 - abs(lum - 0.4) / 0.2
            r = r + 0.02 * mid_amount
            g = g + 0.01 * mid_amount

        # Gentle warm glow in highlights
        if lum > 0.6:
            highlight_amount = (lum - 0.6) / 0.4
            r = r + 0.03 * highlight_amount
            g = g + 0.015 * highlight_amount

        return np.clip([r, g, b], 0, 1)

    def generate_supra_lut(self):
        """
        Generate SUPRA (daylight) film LUT
        Characteristics:
        - Natural daylight rendering
        - Clean highlights
        - Subtle shadow detail
        - Film-like contrast
        """
        print("🌅 Generating SUPRA (Daylight) LUT...")

        lut_data = []
        size = self.lut_size

        for b_idx in range(size):
            for g_idx in range(size):
                for r_idx in range(size):
                    # Input color (normalized 0-1)
                    r = r_idx / (size - 1)
                    g = g_idx / (size - 1)
                    b = b_idx / (size - 1)

                    # Convert to linear for proper color math
                    r_lin = self.srgb_to_linear(r)
                    g_lin = self.srgb_to_linear(g)
                    b_lin = self.srgb_to_linear(b)

                    # Calculate luminance in linear space
                    lum_lin = 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

                    # Apply film tone curve
                    new_lum_lin = self.film_tone_curve(lum_lin,
                                                       shadow_lift=0.02,
                                                       highlight_rolloff=0.10)

                    # Scale RGB to preserve color while changing luminance
                    if lum_lin > 0:
                        scale = new_lum_lin / lum_lin
                        r_lin *= scale
                        g_lin *= scale
                        b_lin *= scale

                    # Apply film contrast
                    r_lin = self.film_contrast_curve(r_lin, strength=0.12)
                    g_lin = self.film_contrast_curve(g_lin, strength=0.12)
                    b_lin = self.film_contrast_curve(b_lin, strength=0.12)

                    # Convert back to sRGB for color shift
                    r_srgb = self.linear_to_srgb(r_lin)
                    g_srgb = self.linear_to_srgb(g_lin)
                    b_srgb = self.linear_to_srgb(b_lin)

                    # Apply daylight color shift
                    rgb_shifted = self.daylight_color_shift([r_srgb, g_srgb, b_srgb])

                    # Convert back to linear for output
                    r_out = self.srgb_to_linear(rgb_shifted[0])
                    g_out = self.srgb_to_linear(rgb_shifted[1])
                    b_out = self.srgb_to_linear(rgb_shifted[2])

                    lut_data.extend([r_out, g_out, b_out])

        return lut_data

    def generate_chrome_lut(self):
        """
        Generate CHROME (tungsten) film LUT
        Characteristics:
        - Warm tungsten color balance
        - Golden/amber shift
        - Gentle shadows
        - Film-like highlight rolloff
        """
        print("🔥 Generating CHROME (Tungsten) LUT...")

        lut_data = []
        size = self.lut_size

        for b_idx in range(size):
            for g_idx in range(size):
                for r_idx in range(size):
                    # Input color (normalized 0-1)
                    r = r_idx / (size - 1)
                    g = g_idx / (size - 1)
                    b = b_idx / (size - 1)

                    # Convert to linear
                    r_lin = self.srgb_to_linear(r)
                    g_lin = self.srgb_to_linear(g)
                    b_lin = self.srgb_to_linear(b)

                    # Calculate luminance
                    lum_lin = 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin

                    # Apply film tone curve (slightly more shadow lift for tungsten)
                    new_lum_lin = self.film_tone_curve(lum_lin,
                                                       shadow_lift=0.025,
                                                       highlight_rolloff=0.12)

                    # Scale RGB
                    if lum_lin > 0:
                        scale = new_lum_lin / lum_lin
                        r_lin *= scale
                        g_lin *= scale
                        b_lin *= scale

                    # Apply film contrast (slightly gentler for tungsten)
                    r_lin = self.film_contrast_curve(r_lin, strength=0.10)
                    g_lin = self.film_contrast_curve(g_lin, strength=0.10)
                    b_lin = self.film_contrast_curve(b_lin, strength=0.10)

                    # Convert back to sRGB
                    r_srgb = self.linear_to_srgb(r_lin)
                    g_srgb = self.linear_to_srgb(g_lin)
                    b_srgb = self.linear_to_srgb(b_lin)

                    # Apply tungsten color shift
                    rgb_shifted = self.tungsten_color_shift([r_srgb, g_srgb, b_srgb])

                    # Convert back to linear
                    r_out = self.srgb_to_linear(rgb_shifted[0])
                    g_out = self.srgb_to_linear(rgb_shifted[1])
                    b_out = self.srgb_to_linear(rgb_shifted[2])

                    lut_data.extend([r_out, g_out, b_out])

        return lut_data

    def write_cube_file(self, lut_data, filename, title):
        """Write LUT data to .cube file format"""
        with open(filename, 'w') as f:
            f.write(f"TITLE \"{title}\"\n")
            f.write(f"LUT_3D_SIZE {self.lut_size}\n")
            f.write("DOMAIN_MIN 0.0 0.0 0.0\n")
            f.write("DOMAIN_MAX 1.0 1.0 1.0\n")
            f.write("\n")

            # Write LUT entries
            for i in range(0, len(lut_data), 3):
                r, g, b = lut_data[i:i+3]
                f.write(f"{r:.6f} {g:.6f} {b:.6f}\n")

        print(f"✅ Wrote {filename}")

def main():
    print("=" * 60)
    print("FRONTIER FILM LUT GENERATOR V2")
    print("Identity + Film Character Approach")
    print("=" * 60)
    print()

    # Create output directory
    output_dir = Path("film-luts/Generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize generator
    generator = FilmLUTGenerator(lut_size=33)

    # Generate SUPRA (daylight) LUT
    print()
    supra_lut = generator.generate_supra_lut()
    supra_path = output_dir / "SUPRA.cube"
    generator.write_cube_file(supra_lut, supra_path,
                             "Frontier SUPRA - Daylight Film Emulation")

    # Generate CHROME (tungsten) LUT
    print()
    chrome_lut = generator.generate_chrome_lut()
    chrome_path = output_dir / "CHROME.cube"
    generator.write_cube_file(chrome_lut, chrome_path,
                             "Frontier CHROME - Tungsten Film Emulation")

    # Generate report
    print()
    print("📊 Generating analysis report...")
    report = {
        "version": "2.0",
        "approach": "Identity mapping + Film characteristics",
        "lut_properties": {
            "resolution": f"{generator.lut_size}x{generator.lut_size}x{generator.lut_size}",
            "color_space": "Linear RGB (sRGB gamma decoded)",
            "method": "Algorithmic film emulation"
        },
        "characteristics": {
            "SUPRA": {
                "name": "Daylight Film Emulation",
                "color_temperature": "~5500K (neutral daylight)",
                "tone_curve": "Soft highlight rolloff (10%), gentle shadow lift (2%)",
                "contrast": "Film S-curve (12% strength)",
                "color_grading": "Subtle blue lift in shadows, clean highlights",
                "use_case": "Outdoor photography, natural light, portraits, landscapes"
            },
            "CHROME": {
                "name": "Tungsten Film Emulation",
                "color_temperature": "~3200K (warm tungsten)",
                "tone_curve": "Soft highlight rolloff (12%), shadow lift (2.5%)",
                "contrast": "Gentle film S-curve (10% strength)",
                "color_grading": "Warm amber shift, golden midtones, glowing highlights",
                "use_case": "Indoor photography, night scenes, warm artificial light"
            }
        },
        "technical_notes": [
            "All processing done in linear RGB with gamma correction",
            "Tone curves preserve film latitude (grain-friendly)",
            "Color shifts applied in sRGB for perceptual accuracy",
            "Highlight rolloff prevents clipping (film-like)",
            "Shadow lift preserves detail (no crushed blacks)"
        ],
        "files_generated": [
            str(supra_path),
            str(chrome_path)
        ]
    }

    report_path = output_dir / "analysis_report_v2.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"✅ Wrote {report_path}")
    print()
    print("=" * 60)
    print("✨ FILM LUT GENERATION COMPLETE")
    print("=" * 60)
    print()
    print("Generated LUTs:")
    print(f"  - SUPRA.cube  (Daylight film emulation)")
    print(f"  - CHROME.cube (Tungsten film emulation)")
    print()
    print("These LUTs transform digital photos to have film characteristics:")
    print("  • Soft highlight compression (film rolloff)")
    print("  • Gentle shadow detail (no crushed blacks)")
    print("  • Film-like contrast curves")
    print("  • Authentic color rendering")
    print("  • Grain-friendly latitude")
    print()
    print("Ready to use in Frontier Digital Processor!")

if __name__ == "__main__":
    main()

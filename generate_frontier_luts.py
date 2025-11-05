#!/usr/bin/env python3
"""
Frontier Film Scan LUT Generator
Analyzes 500+ film scans and creates production-ready 3D LUTs for film emulation.
"""

import os
import numpy as np
from PIL import Image
import json
from pathlib import Path
from collections import defaultdict
import time

# Configuration
SCANS_DIR = " film-scans"  # Note: folder has leading space
OUTPUT_DIR = "film-luts/Generated"
SUPRA_LUT = "SUPRA.cube"
CHROME_LUT = "CHROME.cube"
LUT_SIZE = 33  # 33x33x33 for quality
SAMPLE_SIZE = 100  # Number of samples per image for analysis

class FrontierLUTGenerator:
    def __init__(self):
        self.daylight_images = []
        self.tungsten_images = []
        self.analysis_data = {
            'daylight': {'count': 0, 'avg_temp': 0, 'tone_curves': [], 'colors': []},
            'tungsten': {'count': 0, 'avg_temp': 0, 'tone_curves': [], 'colors': []},
            'total_analyzed': 0,
            'processing_time': 0
        }

    def rgb_to_linear(self, rgb):
        """Convert sRGB to linear RGB (for proper color math)"""
        rgb = np.array(rgb, dtype=np.float32) / 255.0
        linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
        return linear

    def linear_to_rgb(self, linear):
        """Convert linear RGB back to sRGB"""
        rgb = np.where(linear <= 0.0031308, linear * 12.92, 1.055 * (linear ** (1/2.4)) - 0.055)
        return np.clip(rgb * 255, 0, 255).astype(np.uint8)

    def estimate_color_temperature(self, img_array):
        """
        Estimate color temperature from image statistics
        Returns: temperature in Kelvin (approximate)
        """
        # Sample the image (faster than analyzing every pixel)
        h, w = img_array.shape[:2]
        step = max(h // 20, w // 20, 1)
        sample = img_array[::step, ::step]

        # Get average RGB in linear space
        linear = self.rgb_to_linear(sample)
        avg_r = np.mean(linear[:,:,0])
        avg_g = np.mean(linear[:,:,1])
        avg_b = np.mean(linear[:,:,2])

        # Avoid division by zero
        if avg_b < 0.001:
            avg_b = 0.001

        # R/B ratio indicates color temperature
        # Higher R/B = warmer (tungsten)
        # Lower R/B = cooler (daylight)
        rb_ratio = avg_r / avg_b

        # Rough mapping (based on film scanner characteristics)
        # Daylight: ~5500K (rb_ratio ≈ 0.95-1.05)
        # Tungsten: ~3200K (rb_ratio ≈ 1.2-1.5)

        if rb_ratio > 1.15:
            temp = max(2500, 6500 - (rb_ratio - 1.0) * 3000)
        else:
            temp = min(7500, 3000 + (1.0 / (rb_ratio + 0.01)) * 2000)

        return temp, rb_ratio

    def extract_tone_curve(self, img_array, num_samples=SAMPLE_SIZE):
        """
        Extract tone response by analyzing luminance distribution
        Returns array of (input_lum, output_lum) points
        """
        # Convert to linear for proper luminance calculation
        linear = self.rgb_to_linear(img_array)

        # Calculate luminance (Rec.709 coefficients)
        lum = 0.2126 * linear[:,:,0] + 0.7152 * linear[:,:,1] + 0.0722 * linear[:,:,2]

        # Get histogram
        hist, bins = np.histogram(lum.flatten(), bins=num_samples, range=(0, 1))

        # Calculate cumulative distribution (tone mapping)
        cdf = hist.cumsum()
        cdf = cdf / cdf[-1]  # Normalize

        # Return tone curve points
        return bins[:-1], cdf

    def analyze_image(self, image_path):
        """Analyze a single image and categorize it"""
        try:
            img = Image.open(image_path).convert('RGB')

            # Resize for faster processing (maintain aspect ratio)
            img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            img_array = np.array(img)

            # Estimate color temperature
            temp, rb_ratio = self.estimate_color_temperature(img_array)

            # Extract tone curve
            input_lum, output_lum = self.extract_tone_curve(img_array)

            # Get color statistics (for color grading info)
            linear = self.rgb_to_linear(img_array)
            color_stats = {
                'r_mean': float(np.mean(linear[:,:,0])),
                'g_mean': float(np.mean(linear[:,:,1])),
                'b_mean': float(np.mean(linear[:,:,2])),
                'r_std': float(np.std(linear[:,:,0])),
                'g_std': float(np.std(linear[:,:,1])),
                'b_std': float(np.std(linear[:,:,2]))
            }

            # Categorize
            is_daylight = temp > 4500  # Threshold for daylight vs tungsten

            return {
                'path': str(image_path),
                'temp': temp,
                'rb_ratio': rb_ratio,
                'tone_curve': (input_lum, output_lum),
                'color_stats': color_stats,
                'is_daylight': is_daylight
            }

        except Exception as e:
            print(f"Error analyzing {image_path}: {e}")
            return None

    def analyze_all_scans(self):
        """Analyze all film scans in the directory"""
        print("🎞️  Starting Frontier Film Scan Analysis...")
        print(f"📁 Scanning directory: {SCANS_DIR}")

        start_time = time.time()

        # Find all JPEG files
        scan_path = Path(SCANS_DIR)
        image_files = list(scan_path.glob("*.jpg")) + list(scan_path.glob("*.JPG")) + \
                      list(scan_path.glob("*.jpeg")) + list(scan_path.glob("*.JPEG"))

        total = len(image_files)
        print(f"📸 Found {total} images to analyze\n")

        # Analyze each image
        for i, img_path in enumerate(image_files, 1):
            if i % 50 == 0 or i == 1:
                print(f"   Analyzing image {i}/{total} ({i/total*100:.1f}%)")

            result = self.analyze_image(img_path)
            if result:
                self.analysis_data['total_analyzed'] += 1

                if result['is_daylight']:
                    self.daylight_images.append(result)
                    self.analysis_data['daylight']['count'] += 1
                    self.analysis_data['daylight']['tone_curves'].append(result['tone_curve'])
                    self.analysis_data['daylight']['colors'].append(result['color_stats'])
                else:
                    self.tungsten_images.append(result)
                    self.analysis_data['tungsten']['count'] += 1
                    self.analysis_data['tungsten']['tone_curves'].append(result['tone_curve'])
                    self.analysis_data['tungsten']['colors'].append(result['color_stats'])

        # Calculate statistics
        if self.daylight_images:
            self.analysis_data['daylight']['avg_temp'] = np.mean([img['temp'] for img in self.daylight_images])
        if self.tungsten_images:
            self.analysis_data['tungsten']['avg_temp'] = np.mean([img['temp'] for img in self.tungsten_images])

        self.analysis_data['processing_time'] = time.time() - start_time

        print(f"\n✅ Analysis complete!")
        print(f"   Total analyzed: {self.analysis_data['total_analyzed']}")
        print(f"   Daylight images: {self.analysis_data['daylight']['count']}")
        print(f"   Tungsten images: {self.analysis_data['tungsten']['count']}")
        print(f"   Time: {self.analysis_data['processing_time']:.1f}s\n")

    def generate_lut_3d(self, category='daylight', size=LUT_SIZE):
        """
        Generate a 3D LUT from analyzed images
        category: 'daylight' or 'tungsten'
        """
        print(f"🎨 Generating {category.upper()} LUT ({size}x{size}x{size})...")

        images = self.daylight_images if category == 'daylight' else self.tungsten_images
        if not images:
            print(f"   ⚠️  No {category} images found!")
            return None

        # Get average tone curve
        all_inputs = []
        all_outputs = []
        for img in images:
            inp, out = img['tone_curve']
            all_inputs.append(inp)
            all_outputs.append(out)

        avg_input = np.mean(all_inputs, axis=0)
        avg_output = np.mean(all_outputs, axis=0)

        # Create interpolation function for tone curve
        from scipy import interpolate
        tone_func = interpolate.interp1d(avg_input, avg_output,
                                         kind='cubic',
                                         bounds_error=False,
                                         fill_value=(0, 1))

        # Calculate average color shift
        colors = self.analysis_data[category]['colors']
        avg_r = np.mean([c['r_mean'] for c in colors])
        avg_g = np.mean([c['g_mean'] for c in colors])
        avg_b = np.mean([c['b_mean'] for c in colors])

        # Normalize to green (reference)
        r_shift = avg_r / avg_g if avg_g > 0 else 1.0
        b_shift = avg_b / avg_g if avg_g > 0 else 1.0

        # Generate 3D LUT
        lut = np.zeros((size, size, size, 3))

        for r in range(size):
            for g in range(size):
                for b in range(size):
                    # Input colors (normalized 0-1)
                    input_r = r / (size - 1)
                    input_g = g / (size - 1)
                    input_b = b / (size - 1)

                    # Calculate luminance
                    lum = 0.2126 * input_r + 0.7152 * input_g + 0.0722 * input_b

                    # Apply film-like tone curve (soft highlight rolloff)
                    new_lum = float(tone_func(lum))

                    # Soft contrast adjustment (preserve grain)
                    contrast = 1.05 if category == 'daylight' else 1.03
                    new_lum = 0.5 + (new_lum - 0.5) * contrast

                    # Film highlight rolloff (prevent clipping)
                    if new_lum > 0.85:
                        rolloff = (new_lum - 0.85) / 0.15
                        new_lum = 0.85 + rolloff * 0.12  # Compress highlights

                    # Gentle shadow lift (preserve detail)
                    if new_lum < 0.15:
                        lift = (0.15 - new_lum) / 0.15
                        new_lum = new_lum + lift * 0.02

                    # Apply luminance change while preserving color ratios
                    if lum > 0.001:
                        scale = new_lum / lum
                    else:
                        scale = 1.0

                    output_r = input_r * scale * r_shift
                    output_g = input_g * scale
                    output_b = input_b * scale * b_shift

                    # Subtle color grading based on category
                    if category == 'tungsten':
                        # Warm preservation (don't overcorrect)
                        output_r *= 1.02
                        output_b *= 0.98
                    else:
                        # Slight cool bias for daylight
                        output_b *= 1.01

                    # Clamp and store
                    lut[r, g, b, 0] = np.clip(output_r, 0, 1)
                    lut[r, g, b, 1] = np.clip(output_g, 0, 1)
                    lut[r, g, b, 2] = np.clip(output_b, 0, 1)

        return lut

    def write_cube_file(self, lut, filename, title):
        """Write LUT in .cube format"""
        size = lut.shape[0]

        with open(filename, 'w') as f:
            f.write(f"# {title}\n")
            f.write(f"# Generated from {self.analysis_data['total_analyzed']} Frontier film scans\n")
            f.write(f"# Created by Frontier LUT Generator\n")
            f.write(f"# Linear RGB color space\n\n")
            f.write(f"TITLE \"{title}\"\n")
            f.write(f"LUT_3D_SIZE {size}\n")
            f.write(f"DOMAIN_MIN 0.0 0.0 0.0\n")
            f.write(f"DOMAIN_MAX 1.0 1.0 1.0\n\n")

            # Write LUT data (Blue-fastest order)
            for b in range(size):
                for g in range(size):
                    for r in range(size):
                        f.write(f"{lut[r,g,b,0]:.6f} {lut[r,g,b,1]:.6f} {lut[r,g,b,2]:.6f}\n")

        print(f"   ✅ Saved: {filename}")

    def generate_analysis_report(self):
        """Generate detailed analysis report"""
        print("\n📊 Generating analysis report...")

        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        report = {
            'summary': {
                'total_images': self.analysis_data['total_analyzed'],
                'daylight_count': self.analysis_data['daylight']['count'],
                'tungsten_count': self.analysis_data['tungsten']['count'],
                'processing_time_seconds': self.analysis_data['processing_time'],
                'daylight_percentage': (self.analysis_data['daylight']['count'] /
                                       self.analysis_data['total_analyzed'] * 100),
                'tungsten_percentage': (self.analysis_data['tungsten']['count'] /
                                       self.analysis_data['total_analyzed'] * 100)
            },
            'characteristics': {
                'daylight': {
                    'avg_color_temp_k': round(self.analysis_data['daylight']['avg_temp']),
                    'characteristics': 'Natural light, higher blue content, cleaner highlights'
                },
                'tungsten': {
                    'avg_color_temp_k': round(self.analysis_data['tungsten']['avg_temp']),
                    'characteristics': 'Warm artificial light, amber shift, gentle shadows'
                }
            },
            'lut_properties': {
                'resolution': f'{LUT_SIZE}x{LUT_SIZE}x{LUT_SIZE}',
                'color_space': 'Linear RGB (for WebAssembly processing)',
                'characteristics': [
                    'Soft highlight compression (film rolloff)',
                    'Gentle shadow transitions (no crushed blacks)',
                    'Grain-friendly contrast (preserves grain structure)',
                    'Organic color relationships (scanned film look)',
                    'Optimized for 32-bit float linear processing'
                ]
            },
            'usage_recommendations': {
                'SUPRA.cube': 'Use for outdoor/daylight scenes. Best for natural light portraits, landscapes, street photography.',
                'CHROME.cube': 'Use for indoor/tungsten scenes. Best for night photography, warm interior lighting, artificial light sources.'
            }
        }

        # Save JSON report
        report_path = os.path.join(OUTPUT_DIR, 'analysis_report.json')
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"   ✅ Saved: {report_path}")

        # Print summary to console
        print("\n" + "="*60)
        print("📊 FRONTIER FILM SCAN ANALYSIS REPORT")
        print("="*60)
        print(f"\n📸 Images Analyzed: {report['summary']['total_images']}")
        print(f"   • Daylight: {report['summary']['daylight_count']} ({report['summary']['daylight_percentage']:.1f}%)")
        print(f"   • Tungsten: {report['summary']['tungsten_count']} ({report['summary']['tungsten_percentage']:.1f}%)")
        print(f"\n🌡️  Color Temperature:")
        print(f"   • Daylight average: ~{report['characteristics']['daylight']['avg_color_temp_k']}K")
        print(f"   • Tungsten average: ~{report['characteristics']['tungsten']['avg_color_temp_k']}K")
        print(f"\n🎨 LUT Characteristics:")
        for char in report['lut_properties']['characteristics']:
            print(f"   • {char}")
        print(f"\n💡 Usage Recommendations:")
        print(f"   SUPRA.cube  → {report['usage_recommendations']['SUPRA.cube']}")
        print(f"   CHROME.cube → {report['usage_recommendations']['CHROME.cube']}")
        print("\n" + "="*60)

        return report

    def generate_all(self):
        """Main workflow: analyze and generate everything"""
        # Step 1: Analyze all scans
        self.analyze_all_scans()

        if self.analysis_data['total_analyzed'] == 0:
            print("❌ No images analyzed. Exiting.")
            return

        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Step 2: Generate SUPRA LUT (daylight)
        if self.daylight_images:
            supra_lut = self.generate_lut_3d('daylight', LUT_SIZE)
            if supra_lut is not None:
                supra_path = os.path.join(OUTPUT_DIR, SUPRA_LUT)
                self.write_cube_file(supra_lut, supra_path, "SUPRA - Frontier Daylight Film Emulation")
        else:
            print("⚠️  No daylight images found, skipping SUPRA.cube")

        # Step 3: Generate CHROME LUT (tungsten)
        if self.tungsten_images:
            chrome_lut = self.generate_lut_3d('tungsten', LUT_SIZE)
            if chrome_lut is not None:
                chrome_path = os.path.join(OUTPUT_DIR, CHROME_LUT)
                self.write_cube_file(chrome_lut, chrome_path, "CHROME - Frontier Tungsten Film Emulation")
        else:
            print("⚠️  No tungsten images found, skipping CHROME.cube")

        # Step 4: Generate report
        self.generate_analysis_report()

        print(f"\n✨ Complete! LUTs saved to: {OUTPUT_DIR}")
        print("🎬 Ready for use in your WebAssembly film emulation app\n")

if __name__ == '__main__':
    generator = FrontierLUTGenerator()
    generator.generate_all()

#!/usr/bin/env python3
"""
Modify LUT files to bake in global improvements:
- 10% contrast reduction
- Global luminosity boost
- SUPRA-specific: grey preservation + warmth for colorful pixels
"""

import re
import os

def parse_cube_file(filepath):
    """Parse a .cube LUT file and return header and data"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    header_lines = []
    data_lines = []
    in_data = False
    lut_size = 0

    for line in lines:
        stripped = line.strip()

        # Check for LUT_3D_SIZE
        if stripped.startswith('LUT_3D_SIZE'):
            lut_size = int(stripped.split()[1])
            header_lines.append(line)
        elif not in_data and (stripped == '' or stripped.startswith('#') or stripped.startswith('TITLE') or stripped.startswith('DOMAIN_MIN') or stripped.startswith('DOMAIN_MAX')):
            header_lines.append(line)
        else:
            # Check if this looks like RGB data
            parts = stripped.split()
            if len(parts) == 3:
                try:
                    float(parts[0])
                    float(parts[1])
                    float(parts[2])
                    in_data = True
                    data_lines.append(line)
                except ValueError:
                    if not in_data:
                        header_lines.append(line)
            elif not in_data:
                header_lines.append(line)
            elif stripped:
                data_lines.append(line)

    return header_lines, data_lines, lut_size

def apply_contrast_reduction(r, g, b, amount=0.10):
    """Reduce contrast by moving RGB values toward midpoint"""
    midpoint = 0.5
    r = r + (midpoint - r) * amount
    g = g + (midpoint - g) * amount
    b = b + (midpoint - b) * amount
    return r, g, b

def apply_luminosity(r, g, b):
    """Apply global luminosity boost to highlights"""
    brightness = (r + g + b) / 3.0

    if brightness > 0.392:  # 100/255 = 0.392
        luminosity_strength = (brightness - 0.392) / 0.608  # 155/255 = 0.608
        lift = luminosity_strength * 0.0235  # 6/255 = 0.0235
        r = min(1.0, r + lift)
        g = min(1.0, g + lift)
        b = min(1.0, b + lift)

    return r, g, b

def apply_supra_warmth(r, g, b):
    """
    SUPRA-specific: Add warmth only to colorful pixels, preserve greys
    """
    max_channel = max(r, g, b)
    min_channel = min(r, g, b)
    saturation = (max_channel - min_channel) / max_channel if max_channel > 0 else 0
    brightness = (r + g + b) / 3.0

    # Only apply warmth to colorful pixels (sat > 0.15)
    # Scale from 0% at sat=0.05 to 100% at sat=0.20
    colorfulness = max(0, min(1, (saturation - 0.05) / 0.15))

    warmth_strength = brightness  # Stronger in brighter areas

    # Add warmth scaled by colorfulness
    r = min(1.0, r + (6.0/255.0) * warmth_strength * colorfulness)
    b = max(0.0, b - (5.0/255.0) * warmth_strength * colorfulness)

    # Midtone warmth boost
    midtone_boost = 1.0 - abs(brightness - 0.502) / 0.502  # 128/255 = 0.502
    r = min(1.0, r + (3.0/255.0) * midtone_boost * colorfulness)

    return r, g, b

def modify_lut_data(data_lines, preset_name):
    """Modify LUT data with global improvements + preset-specific adjustments"""
    modified_lines = []

    for line in data_lines:
        stripped = line.strip()
        if not stripped:
            modified_lines.append(line)
            continue

        parts = stripped.split()
        if len(parts) != 3:
            modified_lines.append(line)
            continue

        try:
            r, g, b = float(parts[0]), float(parts[1]), float(parts[2])

            # Apply global improvements to ALL presets
            r, g, b = apply_contrast_reduction(r, g, b, amount=0.10)
            r, g, b = apply_luminosity(r, g, b)

            # SUPRA-specific: add warmth while preserving greys
            if preset_name == 'supra':
                r, g, b = apply_supra_warmth(r, g, b)

            # Clamp values
            r = max(0.0, min(1.0, r))
            g = max(0.0, min(1.0, g))
            b = max(0.0, min(1.0, b))

            modified_lines.append(f"{r:.6f} {g:.6f} {b:.6f}\n")
        except ValueError:
            modified_lines.append(line)

    return modified_lines

def backup_and_modify_lut(filepath, preset_name):
    """Backup original LUT and create modified version"""
    # Create backup
    backup_path = filepath + '.backup'
    if not os.path.exists(backup_path):
        with open(filepath, 'r') as src, open(backup_path, 'w') as dst:
            dst.write(src.read())
        print(f"✅ Backed up: {backup_path}")

    # Parse LUT
    header_lines, data_lines, lut_size = parse_cube_file(filepath)
    print(f"📊 {preset_name.upper()}: LUT size = {lut_size}x{lut_size}x{lut_size} ({lut_size**3} entries)")

    # Modify data
    modified_data = modify_lut_data(data_lines, preset_name)

    # Write modified LUT
    with open(filepath, 'w') as f:
        f.writelines(header_lines)
        f.writelines(modified_data)

    print(f"✅ Modified: {filepath}")

def main():
    base_path = "/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor"

    luts = {
        'supra': 'film-luts/Frontier luts/Fuji_Pro_400H_v3_REBUILT.cube',
        'chrome': 'film-luts/Frontier luts/ClassicPrint 16mm DWG LUT v3 Technicolor.cube',
        'xxx': 'film-luts/Frontier luts/ClassicPrint 16mm DWG LUT v3 500T.cube'
    }

    print("🎨 Modifying LUT files with baked-in improvements...\n")

    for preset_name, lut_path in luts.items():
        full_path = os.path.join(base_path, lut_path)

        if not os.path.exists(full_path):
            print(f"⚠️  NOT FOUND: {full_path}")
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {preset_name.upper()}")
        print(f"{'='*60}")

        backup_and_modify_lut(full_path, preset_name)

    print("\n✅ All LUTs modified successfully!")
    print("\nChanges applied:")
    print("  - 10% contrast reduction (all presets)")
    print("  - Global luminosity boost (all presets)")
    print("  - SUPRA: Warmth + grey preservation")

if __name__ == '__main__':
    main()

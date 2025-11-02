# Film LUTs Directory

Place your ClassicPrint 16mm film LUTs here with the following filenames:

## Required LUT Files:

```
ClassicPrint_16mm_250D_Rec709.cube
ClassicPrint_16mm_500T_Rec709.cube
ClassicPrint_16mm_Ektachrome_Rec709.cube
```

## Format:

- File format: `.cube` (3D LUT cube format)
- Color space: Rec709 (standard for web/mobile)
- Size: Typically 64x64x64 (most common)

## Testing:

Once you add the .cube files here, the app will automatically:
1. Load them when you select a preset
2. Cache them for performance
3. Apply them to both photos and videos

## Troubleshooting:

- Check browser console (F12) or mobile debug button (🐛) for error messages
- Verify filenames match exactly (case-sensitive)
- Ensure .cube files are valid format
- Make sure files are committed to git and deployed

## Current Presets:

- **250D**: Daylight balanced, fine grain
- **500T**: Tungsten balanced, versatile  
- **Ektachrome**: Vibrant colors, punchy

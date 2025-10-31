# SP500 Film Simulator

A mobile-first progressive web app that simulates the **Fuji Frontier SP500 film scanner editing experience**. Upload photos from your iPhone camera roll, apply professional film lab adjustments (tone, color, grain), and save processed images back to your Photos library.

![SP500 Banner](https://via.placeholder.com/800x400/000000/4fd1c5?text=SP500+Film+Simulator)

## ✨ Features

### Photo Management
- 📤 **Upload 1-36 photos** from camera roll
- 🎞️ **Horizontal filmstrip** navigation with frame counter
- 👆 **Touch-optimized gestures** (swipe, tap, drag)
- 🔄 **Before/After toggle** to compare original vs. edited
- 📱 **iPhone-optimized** with safe area support (notch/Dynamic Island)

### Professional Film Lab Processing

#### 🎨 Frontier Color Profile
Authentic Fujifilm color science emulation:
- Warmer color temperature
- Enhanced reds (beautiful skin tones)
- Rich, saturated blues
- Slight magenta push in shadows
- Smooth highlight rolloff

#### 📊 Tone Adjustment (7 Presets)
- **Standard** - Balanced default tone curve
- **All Hard** - Increased contrast across all tones
- **All Soft** - Decreased contrast (gentler curve)
- **Highlight Hard** - Increased contrast in bright areas
- **Highlight Soft** - Recover blown highlights
- **Shadow Hard** - Deepen blacks
- **Shadow Soft** - Lift shadows

#### 💡 Hypertone (Dodging)
Simulates photographic dodging - selective exposure adjustment:
- **OFF** - No processing
- **Mode 1** - Moderate adjustment (balance subject vs background)
- **Mode 2** - Stronger adjustment

#### 🔆 Density Correction
Linear brightness adjustment (-50 to +50):
- Negative values = darker
- Positive values = lighter
- Affects overall exposure

#### 🌈 CMY Color Correction
Professional subtractive color model (like film labs use):
- **Cyan (-20 to +20)**: Add cyan / remove red
- **Magenta (-20 to +20)**: Add magenta / remove green
- **Yellow (-20 to +20)**: Add yellow / remove blue

#### 🔪 Sharpness (7 Levels)
Unsharp mask algorithm:
- Low 3, Low 2, Low 1
- Normal
- High 1, High 2, High 3

#### 🎨 Saturation
Adjustable color intensity (0-200%):
- 0% = Black & white
- 100% = Original
- 200% = Maximum saturation

#### 🎞️ Portra 400 Film Grain
Realistic Kodak Portra 400 grain simulation:
- Fine, tight grain structure
- More visible in shadows
- Smooth, organic appearance (not digital noise)
- Intensity scales with exposure

### Batch Operations
- ⚡ **Process All** - Batch process up to 36 photos
- 📋 **Copy to All** - Apply current settings to all photos
- 🔄 **Reset** - Reset individual or all settings

### Export
- 💾 **Save to Photos** - iOS native share sheet (single photo)
- 📦 **Batch Download** - Download all processed photos as individual files
- 🖼️ **High Quality** - JPEG export at 95% quality
- 🏷️ **Auto-naming** - Files named `sp500_frame_001.jpg`, etc.

## 📱 iOS PWA Features

### Progressive Web App
- ✅ **Add to Home Screen** - Install as standalone app
- ✅ **Offline Support** - Service Worker caching
- ✅ **Full Screen** - No browser chrome in standalone mode
- ✅ **Safe Area Aware** - Respects iPhone notch/Dynamic Island
- ✅ **Dark Theme** - OLED-optimized interface

### iOS Optimizations
- 📳 **Haptic Feedback** - Vibration on slider adjustments & button taps
- 👆 **Large Touch Targets** - Minimum 44x44pt (iOS standard)
- 🎨 **Teal Accent** - `#4fd1c5` (Fujifilm branding)
- 🔒 **Prevent Zoom** - No zoom on input focus
- 🌊 **Smooth Scrolling** - Momentum scrolling on filmstrip
- 🚫 **No Text Selection** - During gestures (better UX)

### Gestures
- ⬅️➡️ **Swipe Left/Right** - Navigate between photos
- 👆 **Tap Preview** - Toggle before/after
- 📸 **Tap Thumbnail** - Jump to specific photo

## 🚀 Getting Started

### Quick Start

1. **Open the app** in Safari on your iPhone:
   ```
   https://your-domain.com/sp500.html
   ```

2. **Add to Home Screen** (optional but recommended):
   - Tap the Share button (⎋)
   - Select "Add to Home Screen"
   - Tap "Add"

3. **Upload photos**:
   - Tap the upload area
   - Select 1-36 photos from your camera roll
   - Supports JPG, PNG, and HEIC formats

4. **Edit your photos**:
   - Adjust tone, color, grain, etc.
   - Swipe left/right to navigate
   - Tap "TAP FOR BEFORE" to compare

5. **Process & Export**:
   - Tap "PROCESS ALL" to batch process
   - Tap "EXPORT PHOTOS" to save

### Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd Frontier-cam-

# Serve locally (requires HTTPS for camera/file access in production)
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/sp500.html
```

### Deployment

#### Netlify (Recommended)
```bash
# Already configured with netlify.toml
netlify deploy --prod
```

#### Vercel
```bash
# Already configured with vercel.json
vercel --prod
```

#### GitHub Pages
```bash
# Push to main branch
git push origin main

# Enable GitHub Pages in repo settings
# Source: main branch, / (root)
```

## 🎯 Technical Details

### Architecture
- **Single-file PWA** - All code in `sp500.html` for simplicity
- **Vanilla JavaScript** - No dependencies (easy to port to native)
- **Canvas API** - Pixel-level image processing
- **Service Worker** - Offline support & caching
- **Web Share API** - Native iOS share sheet integration

### Browser Support
- **iOS Safari 16+** (primary target)
- **Chrome/Edge 90+** (desktop/Android)
- **Firefox 88+** (desktop/Android)

### Performance
- **Real-time preview** - Updates on slider change
- **60fps UI** - Smooth animations
- **Memory efficient** - Cleans up unused resources
- **Progressive loading** - Thumbnails → Preview → Full resolution

### File Structure
```
/Frontier-cam-
  ├── sp500.html           # Main app (single-file PWA)
  ├── manifest.json        # PWA manifest
  ├── sw.js                # Service worker
  ├── icon-192.png         # App icon (192x192)
  ├── icon-512.png         # App icon (512x512)
  ├── README-SP500.md      # This file
  └── netlify.toml         # Deployment config
```

## 🎨 Processing Pipeline

The app applies adjustments in this sequence:

1. **Load original image** to Canvas
2. **Apply Frontier color profile** (warm, rich colors)
3. **Apply tone curve** (contrast adjustments)
4. **Apply hypertone** (dodging)
5. **Apply density correction** (brightness)
6. **Apply CMY color corrections** (subtractive color model)
7. **Apply saturation** adjustment
8. **Apply film grain** (Portra 400 simulation)
9. **Apply sharpening** (always last, unsharp mask)
10. **Output** to Canvas/Blob

## 📸 Use Cases

### Portrait Photography
```
Tone: Highlight Soft (recover skin highlights)
Hypertone: Mode 1 (balance face & background)
Density: +5 to +10 (slightly brighter)
Magenta: +2 to +5 (warm skin tones)
Yellow: +2 to +5 (golden look)
Saturation: 110-120% (vibrant but natural)
Grain: ON (Portra 400 look)
Sharpness: Normal or High 1
```

### Landscape Photography
```
Tone: All Hard or Highlight Hard (punchy contrast)
Hypertone: OFF or Mode 1
Density: 0 to -5 (rich colors)
Cyan: +3 to +8 (deep blue skies)
Saturation: 120-140% (vibrant nature)
Grain: ON or OFF (preference)
Sharpness: High 1 or High 2 (detail)
```

### Street Photography
```
Tone: Shadow Hard (deep blacks)
Hypertone: Mode 2 (strong local contrast)
Density: -5 to -10 (moody)
Cyan: -2 to 0 (warmer tones)
Magenta: +2 to +5 (film look)
Saturation: 90-110% (subtle)
Grain: ON (Portra 400 grit)
Sharpness: Normal or High 1
```

### Black & White Conversion
```
Tone: All Hard (high contrast B&W)
Hypertone: Mode 1 (local adjustments)
Density: As needed
CMY: Adjust for creative toning
  - Cyan +5 for cool B&W (blue shadows)
  - Yellow +5 for warm B&W (sepia tones)
Saturation: 0% (pure B&W)
Grain: ON (classic film grain)
Sharpness: High 2 (crisp details)
```

## 🛠️ Future Enhancements (V2)

- [ ] **Web Workers** - Non-blocking processing for large images
- [ ] **localStorage** - Persist settings between sessions
- [ ] **Custom Presets** - Save favorite setting combinations
- [ ] **More Film Stocks** - Portra 800, Ektar, Tri-X, etc.
- [ ] **Histogram** - RGB histogram visualization
- [ ] **Split View** - Drag divider for before/after comparison
- [ ] **Pinch to Zoom** - Zoom into preview
- [ ] **EXIF Preservation** - Keep metadata in exported photos
- [ ] **ZIP Export** - Download all photos as single ZIP file
- [ ] **Share to Instagram** - Direct social sharing
- [ ] **Comparison Grid** - See all processed photos at once

## 📱 Migration to Native iOS App

When ready to build a native iOS app, recommended approaches:

### Option 1: React Native (Recommended)
- Port to React components
- Access native iOS photo picker
- Better performance
- Publish to App Store

### Option 2: Capacitor
- Wrap existing PWA
- Add native plugins
- Quickest path to App Store

### Option 3: Swift/SwiftUI
- Full native rewrite
- Best performance
- Most control

The current architecture (component-based, clean state management) makes migration straightforward.

## 🐛 Troubleshooting

### Photos Won't Upload
- **iOS:** Ensure Safari has photo access permissions
- **Desktop:** Check file size (max ~10MB per photo recommended)

### Processing is Slow
- Reduce number of photos (process in smaller batches)
- Disable grain temporarily for faster preview
- Close other browser tabs (free up memory)

### Export Not Working
- **iOS:** Use Safari (not Chrome) for Web Share API support
- **Desktop:** Check pop-up blocker settings (blocks download)

### App Not Installing (Add to Home Screen)
- Use Safari (not Chrome/Firefox on iOS)
- Ensure HTTPS is enabled (required for PWA)
- Try reloading the page first

## 📄 License

MIT License - Feel free to use, modify, and distribute.

## 🙏 Credits

- Inspired by the **Fuji Frontier SP500** film scanner
- **Fujifilm** for their legendary color science
- **Kodak Portra 400** for the grain reference

## 📞 Support

For issues, feature requests, or contributions:
- Open an issue on GitHub
- Email: [your-email@example.com]
- Twitter: [@yourusername]

---

**Made with ❤️ for film photography enthusiasts**

Transform your digital photos into authentic film scans, right from your iPhone.

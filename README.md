# Frontier Digital Processor

A retro-styled professional film scanning and color grading processor for iPhone. Upload photos from your camera roll and apply authentic film lab processing effects with a beautiful 8-bit retro interface.

## Features

### Core Functionality
- **Upload Photos**: Load 1-36 photos from your camera roll
- **Professional Film Processing**: Real-time color grading and film effects
- **Batch Processing**: Process entire rolls of film at once
- **Export to Photos**: Save processed images directly to your Photos library
- **Retro Interface**: Pixel font and retro gray beige aesthetic with light/dark modes

### Film Processing Controls

#### Color Modes
- **STD**: Standard color (no film emulation)
- **C41**: Kodak Portra 400 color negative film
- **B&W**: Kodak Tri-X 400 black & white film
- **E6**: Ektachrome slide film

#### CMY Color Correction
Professional Fuji Frontier-style color correction:
- **Cyan**: -50 to +50
- **Magenta**: -50 to +50
- **Yellow**: -50 to +50
- **Density**: -50 to +50 (overall exposure)

#### Contrast Modes
- **Standard**: Normal contrast
- **Soft**: Reduced contrast for gentle look
- **Hard**: Increased contrast for dramatic look
- **Shadow Soft**: Lift shadows while preserving highlights
- **Shadow Hard**: Crush shadows for deeper blacks
- **Highlight Soft**: Roll off highlights smoothly

#### Special Effects
- **Bloom**: 0-100 (halation effect around highlights)
- **Grain**: 0.0-5.0 (film grain intensity)

### User Interface
- Pixel font aesthetic (Press Start 2P)
- Retro 3D button style
- Horizontal filmstrip navigation
- Before/after toggle
- Pinch-to-zoom on canvas
- Frame counter (current photo / total)
- Fuji turquoise accent color

## Quick Start

### Installation
1. Open `index.html` in iPhone Safari
2. Tap Share → Add to Home Screen
3. Launch from home screen for full PWA experience

### Basic Usage
1. **Upload**: Tap "TAP TO SELECT" and choose photos
2. **Edit**: Use COLOR, CMY, SOFT, BLOOM, GRAIN controls
3. **Navigate**: Swipe filmstrip to switch between photos
4. **Export**: Tap "SAVE TO PHOTOS" when done

## Controls Summary

| Action | Gesture |
|--------|---------|
| Upload photos | Tap "TAP TO SELECT" |
| Navigate photos | Tap filmstrip thumbnails or arrow buttons |
| Toggle film mode | Tap COLOR button |
| Adjust colors | Tap CMY button, use sliders |
| Change contrast | Tap SOFT button |
| Add effects | Tap BLOOM/GRAIN buttons |
| Compare | Tap BEFORE/AFTER button |
| Zoom | Pinch to zoom, drag to pan, tap to reset |
| Export | Tap SAVE TO PHOTOS |
| Reset | Tap RESET button |
| Toggle theme | Tap moon/sun icon |

## Technical Details

- **Framework**: Vanilla JavaScript (no dependencies)
- **Rendering**: HTML5 Canvas API with hardware acceleration
- **PWA**: Full offline support with service worker
- **Deployment**: Static files, works on any host

## Setup Notes

### Icons Required
You'll need to add PWA icons:
- `icon-192.png` (192x192)
- `icon-512.png` (512x512)

### Deployment
The app is ready to deploy to:
- **Netlify**: Just drag/drop the folder
- **Vercel**: Connect git repo
- **GitHub Pages**: Enable in repo settings
- **Any static host**: Upload all files

## Project Structure

```
frontier-digital-processor/
├── index.html          # Main application
├── manifest.json       # PWA configuration
├── sw.js              # Service worker
├── netlify.toml       # Netlify config
├── vercel.json        # Vercel config
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Browser Support

### Recommended
- iPhone 11 or newer
- iOS 14+
- Safari browser

### Requirements
- Modern browser with Canvas API
- Photo library access
- Touch screen

## Development

This is a single-page application with no build process. To modify:
1. Edit `index.html` directly
2. Test in Safari on iPhone
3. Deploy updated file

## Credits

Inspired by the legendary Fuji Frontier SP500 film scanner used in professional photo labs worldwide.

---

**Made with ♥ for film photography enthusiasts**

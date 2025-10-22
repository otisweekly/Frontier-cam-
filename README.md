# Leica Rangefinder Camera Web App

A professional Leica-style rangefinder camera web app optimized for iPhone Safari, featuring authentic film stock emulation and real rangefinder focusing mechanics.

## Features

### Core Functionality
- **Real-time Film Stock Emulation**: 6 authentic film stocks with color grading
  - Kodak Portra 400 (warm, natural colors)
  - Kodak Portra 800 (warmer, higher grain)
  - Kodak Tri-X 400 (classic B&W, high contrast)
  - Ilford HP5 Plus (B&W with fine grain)
  - Cinestill 800T (tungsten-balanced, cool tones)
  - Kodak Gold 200 (warm, vibrant)

- **Authentic Rangefinder Patch**: Split-image focusing system
  - Double image overlay effect
  - Ghost image offset when out of focus
  - Swipe on video to adjust focus
  - Yellow/gold tint on rangefinder patch
  - Images align when in focus

- **Manual Controls**:
  - Lens selection: 35mm, 50mm, 90mm (digital zoom)
  - Aperture: f/2, f/2.8, f/4, f/5.6, f/8
  - Frame counter (counts down from 36)

- **Focus Peaking**: Optional red overlay highlighting sharp edges

### User Interface
- Clean minimal Leica-inspired design
- Black bars top and bottom for cinematic feel
- Film window with yellow pill display
- Real-time exposure information
- Light meter indicator
- Large centered shutter button
- Thumbnail preview of last photo
- Slide-up settings panel

## How to Use

### Getting Started
1. Open `index.html` in iPhone Safari
2. Tap "Enable Camera" to grant camera permissions
3. Camera feed will appear with film effects applied

### Taking Photos
1. **Compose**: Frame your shot
2. **Focus**: Swipe left/right on the video feed to adjust focus
   - Watch the rangefinder patch - ghost image slides into alignment when in focus
3. **Shoot**: Tap the white shutter button
4. Photo is automatically downloaded to your device

### Changing Film Stocks
- Swipe left/right on the **film window** (yellow pill at bottom)
- Or swipe left/right on the **film name** (top right corner)
- Current film: Portra 400 (default)

### Adjusting Settings
1. Tap "MENU" button (bottom right)
2. Toggle features:
   - **Rangefinder Patch**: Enable/disable split-image focusing aid
   - **Focus Peaking**: Highlight sharp edges in red
3. Select lens focal length (35/50/90mm)
4. Select aperture (f/2 - f/8)
5. Tap "×" to close settings

## Film Stock Characteristics

### Kodak Portra 400
- Warm, natural skin tones
- Fine grain
- Excellent for portraits and everyday photography

### Kodak Portra 800
- Warmer tones than 400
- More visible grain
- Great for low light and indoor shooting

### Kodak Tri-X 400
- Classic black & white
- High contrast
- Visible grain structure
- Legendary street photography film

### Ilford HP5 Plus
- Black & white with fine grain
- Medium contrast
- Versatile for all conditions

### Cinestill 800T
- Tungsten-balanced (cool tones)
- High saturation
- Signature halation effect
- Perfect for night and indoor tungsten lighting

### Kodak Gold 200
- Warm, golden tones
- High saturation
- Vibrant colors
- Classic consumer film look

## Technical Details

### Camera Implementation
- Uses Canvas API for real-time image processing
- WebRTC MediaStream for camera access
- 60fps rendering pipeline
- Hardware-accelerated when available

### Rangefinder Mechanics
- Captures two overlapping images from video feed
- Horizontal offset simulates focus distance
- Touch gestures control ghost image alignment
- Yellow tint applied to match authentic rangefinder patches

### Focus Peaking
- Real-time Sobel edge detection
- Red overlay on high-contrast edges
- Helps manual focusing on complex subjects

### Film Grading
Each film stock applies unique color transformations:
- Color temperature adjustment (warmth/coolness)
- Saturation boosting or desaturation (B&W)
- Contrast curves
- Brightness compensation
- Film grain simulation
- RGB channel tinting

## Compatibility

### Recommended
- iPhone 11 or newer
- iOS 14+
- Safari browser

### Requirements
- Modern browser with WebRTC support
- Camera access permissions
- Touch screen for gestures

## Controls Summary

| Action | Gesture |
|--------|---------|
| Focus adjustment | Swipe left/right on video |
| Change film stock | Swipe left/right on film window/name |
| Take photo | Tap shutter button |
| Open settings | Tap MENU button |
| Close settings | Tap × button |

## Tips for Best Results

1. **Lighting**: Film stocks look best in natural light
2. **Focus**: Use rangefinder patch for precise focusing
3. **Composition**: Remember the rule of thirds
4. **Film Selection**:
   - Portra for portraits and skin tones
   - Tri-X for street photography
   - Cinestill for night scenes
   - Gold for warm, vibrant scenes

## Future Enhancements

Potential features for future versions:
- Manual exposure control
- ISO simulation
- More film stocks (Fuji, Agfa)
- Photo gallery
- EXIF data preservation
- Double exposure mode
- Time-lapse capability

## Credits

Built with modern web technologies:
- HTML5 Canvas API
- WebRTC MediaStream API
- CSS3 with safe area support
- Vanilla JavaScript (no frameworks)

Inspired by authentic Leica M-series rangefinder cameras and traditional film photography.

---

**Note**: This is a simulation. While the app faithfully recreates film aesthetics and rangefinder mechanics, actual results may vary from real film cameras. For best results, use in good lighting conditions and take time to compose your shots thoughtfully.

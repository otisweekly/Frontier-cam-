# SP500 Film Simulator

A retro-styled Fuji Frontier SP500 film scanner simulator for your iPhone. Upload photos from your camera roll and apply professional film lab processing effects with an authentic 8-bit aesthetic.

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
- Frame counter (shows current photo / total)
- Fuji turquoise accent color

## How to Use

### Getting Started
1. Open `sp500-retro.html` in iPhone Safari
2. Install as PWA (Add to Home Screen) for best experience
3. Tap "TAP TO SELECT" to upload photos

### Processing Photos
1. **Upload**: Select 1-36 photos from your camera roll
2. **Navigate**: Swipe through filmstrip at bottom to switch photos
3. **Adjust**: Use control buttons to adjust color, contrast, and effects
   - **COLOR**: Switch between film stocks (STD/C41/B&W/E6)
   - **CMY**: Fine-tune colors with professional color correction
   - **SOFT**: Adjust contrast curves
   - **BLOOM**: Add halation glow around highlights
   - **GRAIN**: Add film grain texture
4. **Compare**: Toggle BEFORE/AFTER to see original vs processed
5. **Export**: Tap "SAVE TO PHOTOS" to export all processed images

### Navigation Controls
- **Filmstrip**: Tap thumbnails to switch between photos
- **Arrow Buttons**: Navigate previous/next photo
- **Pinch**: Zoom in/out on main canvas
- **Pan**: Drag to move zoomed image
- **Reset Zoom**: Tap canvas once to reset zoom

## Film Stock Characteristics

### C41 (Portra 400)
- Warm, natural colors
- Smooth skin tones
- Subtle grain
- Perfect for portraits and everyday photography

### B&W (Tri-X 400)
- Classic black & white
- High contrast
- Visible grain structure
- Legendary street photography film

### E6 (Ektachrome)
- Vibrant, saturated colors
- Cool tones
- High sharpness
- Perfect for landscapes and product photography

## Technical Details

### Processing Pipeline
- Canvas API for real-time image processing
- Hardware-accelerated rendering
- Per-photo settings storage
- Batch export to camera roll

### Color Processing
Each film mode applies unique color transformations:
- **C41**: Warm color shift, green shadows, smooth highlight rolloff
- **B&W**: Desaturation with contrast boost and grain
- **E6**: Cool color shift, high saturation, punchy shadows

### CMY Correction
Professional film lab color correction:
- Cyan: Shifts green ↔ red
- Magenta: Shifts green ↔ magenta
- Yellow: Shifts blue ↔ yellow
- Density: Overall brightness adjustment

### Special Effects
- **Bloom**: Gaussian blur applied to highlights only, creates halation glow
- **Grain**: Procedural noise overlay with adjustable intensity

## Compatibility

### Recommended
- iPhone 11 or newer
- iOS 14+
- Safari browser

### Requirements
- Modern browser with Canvas API support
- Photo library access permissions

## Controls Summary

| Action | Gesture |
|--------|---------|
| Upload photos | Tap "TAP TO SELECT" |
| Navigate photos | Tap filmstrip thumbnails or arrow buttons |
| Toggle film mode | Tap COLOR button, select mode |
| Adjust CMY | Tap CMY button, use sliders |
| Change contrast | Tap SOFT button, select mode |
| Add bloom/grain | Tap BLOOM/GRAIN buttons, use sliders |
| Compare before/after | Tap BEFORE/AFTER button |
| Zoom canvas | Pinch to zoom, drag to pan, tap to reset |
| Export photos | Tap SAVE TO PHOTOS |
| Reset all settings | Tap RESET button |
| Change theme | Tap moon/sun icon (top right) |

## Tips for Best Results

1. **Start with Film Mode**: Choose your film stock first (C41/B&W/E6)
2. **Fine-tune with CMY**: Use subtle adjustments (-10 to +10) for natural looks
3. **Experiment with Bloom**: Try 10-30 for subtle halation, 50+ for dreamy looks
4. **Add Grain**: Keep between 0.5-2.0 for authentic film texture
5. **Use Soft Modes**: Shadow Soft is great for lifting dark photos
6. **Before/After Toggle**: Always compare to avoid over-processing

## Technical Implementation

Built with modern web technologies:
- HTML5 Canvas API
- Web File API for photo upload
- CSS3 with CSS custom properties for theming
- Vanilla JavaScript (no frameworks)
- PWA manifest for installability

Inspired by the legendary Fuji Frontier SP500 film scanner used in professional photo labs worldwide.

---

**Note**: This is a simulation of professional film scanning equipment. While the app faithfully recreates film processing effects and color grading workflows, results are artistic interpretations rather than chemically-accurate film reproductions.

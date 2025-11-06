# Frontier Digital Processor - Design System Specification

**Version:** 1.0
**Last Updated:** 2025-11-06

---

## Table of Contents

1. [Design Tokens](#design-tokens)
2. [Typography](#typography)
3. [Colors](#colors)
4. [Spacing](#spacing)
5. [Border Radius](#border-radius)
6. [Shadows](#shadows)
7. [Animations & Transitions](#animations--transitions)
8. [Button Components](#button-components)
9. [Modal & View Components](#modal--view-components)
10. [Layout Components](#layout-components)
11. [Special Components](#special-components)

---

## Design Tokens

### Typography

#### Font Families

| Token | Value | Usage |
|-------|-------|-------|
| `--font-primary` | 'PP Fuji', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif | Body text, general UI |
| `--font-display` | 'PP Neue Bit', monospace | Buttons, headings, technical displays |

#### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Standard text |
| Medium | 500 | PP Fuji medium emphasis |
| Bold | 700 | Buttons, headings, emphasis |

#### Font Sizes

| Size | Value | Usage |
|------|-------|-------|
| `--text-xs` | 7px | Control tab labels |
| `--text-sm` | 9px-11px | Photo counter labels, value labels |
| `--text-base` | 16px-18px | Standard buttons, body text |
| `--text-lg` | 20px-24px | Upload button, large buttons |
| `--text-xl` | 26px | Slider values, CMYK values |
| `--text-2xl` | 28px-32px | Hold flash, intensity values |
| `--text-3xl` | 35px | Slider button symbols |
| `--text-4xl` | 72px | Intensity indicator overlay |

---

## Colors

### Primary Colors

| Token | Hex Value | Usage |
|-------|-----------|-------|
| `--color-primary` | #3897AF | Brand primary, active states, turquoise accent |
| `--color-primary-dark` | #2A7B8F | Primary hover/active state |
| `--color-primary-border` | #0A5A6C | Primary button borders |

### Background Colors

| Token | Hex Value | Usage |
|-------|-----------|-------|
| `--bg-gradient-start` | #37A4A4 | Upload screen gradient start |
| `--bg-gradient-end` | #258B8B | Upload screen gradient end |
| `--bg-edit` | #6A6A6A | Edit section background, nav bar, dialogs |
| `--bg-canvas` | #4A4A4A | Canvas container, intensity display |
| `--bg-button` | #D4CEC8 | Standard button background (light gray) |
| `--bg-button-alt` | #B3B3B3 | Alternative button background |
| `--bg-dark` | #000000 | Nav buttons, active states, black backgrounds |
| `--bg-card-dark` | #1a1a1a | Contact sheet items, dark UI elements |
| `--bg-modal` | #000000 | Full-screen modals, overlays |

### Gradient Backgrounds

| Token | Value | Usage |
|-------|-------|-------|
| `--gradient-upload` | linear-gradient(135deg, #37A4A4 0%, #258B8B 100%) | Upload screen |
| `--gradient-display` | linear-gradient(180deg, #E8F0E8 0%, #F0F8F0 100%) | Photo counter, slider values, CMYK values |
| `--gradient-button-dark` | linear-gradient(180deg, #707070 0%, #505050 100%) | Contact sheet buttons, guide close |

### Border Colors

| Token | Hex Value | Usage |
|-------|-----------|-------|
| `--border-primary` | #000000 | Most UI elements (3px solid) |
| `--border-secondary` | #0D626E | Logo container |
| `--border-dark` | #3A3A3A | Dark mode buttons |
| `--border-card` | #333333 | Contact sheet items |
| `--border-subtle` | #222222 | Download previews |

### Text Colors

| Token | Hex Value | Usage |
|-------|-----------|-------|
| `--text-primary` | #000000 | Primary button text |
| `--text-inverse` | #FFFFFF | Text on dark backgrounds |
| `--text-muted` | #999999 | Labels, secondary text |
| `--text-tertiary` | #666666 | Disabled text, tertiary labels |
| `--text-bright` | #EEEDF0 | Upload labels |
| `--text-flash` | #E0E0E0 | Hold flash message |
| `--text-brand` | #3897AF | Brand color text |
| `--text-warning` | #FF8C00 | Orange status |

### Status Light Colors

| Status | Color | Hex Value | Animation |
|--------|-------|-----------|-----------|
| Ready | Green | #4ADE80 | pulse-green-gentle (3s) |
| Processing | Turquoise | #3897AF | pulse-turquoise (2s) |
| Loading | Orange | #FF8C00 | flash-orange (600ms) |
| Wait | Red | #EF4444 | blink-red (800ms) |

### Special State Colors

| State | Color | Hex Value | Usage |
|-------|-------|-----------|-------|
| Holding | Teal | #8CBABB | Copy/paste button holding state |
| Hold Active | Purple | #6355B5 | Hold button active |
| Active Indicator | Turquoise | #3897AF | Active settings indicators |

---

## Spacing

### Padding Values

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | 4px-6px | Small gaps, button internal spacing |
| `--space-sm` | 8px-10px | Standard gaps, padding |
| `--space-md` | 12px-15px | Medium padding, photo counter |
| `--space-lg` | 16px-20px | Large padding, section spacing |
| `--space-xl` | 24px | Extra large spacing, margins |
| `--space-2xl` | 40px-50px | Logo container padding |

### Gap Values

| Token | Value | Usage |
|-------|-------|-------|
| `--gap-xs` | 1px-2px | Minimal gaps |
| `--gap-sm` | 4px-6px | Small element gaps |
| `--gap-md` | 8px-10px | Standard gaps, grid spacing |
| `--gap-lg` | 12px-16px | Large gaps |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 3px | Small elements, control tabs |
| `--radius-md` | 4px | Standard buttons, most UI elements |
| `--radius-lg` | 6px | Slider buttons, photo counter, CMYK arrow buttons |
| `--radius-round` | 50% | Status lights, indicators, debug toggle |
| `--radius-partial` | 6px 6px 0 0 | CMYK values (top corners only) |

---

## Shadows

### Box Shadow Tokens

#### Elevated Shadow (8px)
**Value:** `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)`
**Usage:** Standard buttons, most interactive elements
**Active State:** `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)`

#### Medium Shadow (6px)
**Value:** `0 6px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)`
**Usage:** Background toggle buttons, guide buttons
**Active State:** `0 2px-3px 0 #222222, inset 0 2px-3px 5px rgba(0,0,0,0.3)`

#### Large Shadow (5px - Save Button)
**Value:** `0 5px 0 #222222`
**Usage:** Save button
**Active State:** `0 2px 0 #222222`

#### Small Shadow (4px)
**Value:** `0 4px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)`
**Usage:** History item buttons, contact sheet edit buttons
**Active State:** `0 2px 0 #222222, inset 0 2px 3px rgba(0,0,0,0.3)`

#### Tab Shadow (2px)
**Value:** `0 2px 0 #222222`
**Usage:** Control tabs
**Active State:** `0 1px 0 #222222`

### Inset Shadows

| Token | Value | Usage |
|-------|-------|-------|
| Display Inset | `inset 0 2px 4px rgba(0,0,0,0.15), inset 0 -1px 0 rgba(255,255,255,0.8)` | Photo counter, slider values, CMYK values |
| Nav Bar Inset | `inset 0 2px 0 rgba(0,0,0,0.3), inset 0 3px 0 rgba(255,255,255,0.1)` | Top nav bar, edit footer, dialogs |
| Logo Container | `inset 0 2px 0 rgba(255,255,255,0.1), inset 0 -2px 0 rgba(0,0,0,0.3), 0 4px 0 rgba(0,0,0,0.2)` | Logo container |

### Text Shadows

| Usage | Value |
|-------|-------|
| Intensity Indicator | `0 2px 8px rgba(0,0,0,0.8), 0 0 4px rgba(0,0,0,0.9)` |
| Hold Flash | `0 0 12px rgba(224,224,224,0.6), 0 2px 4px rgba(0,0,0,0.9)` |
| Fullscreen Hint | `0 2px 6px rgba(0,0,0,0.9)` |
| Progress Text | `0 1px 2px rgba(0,0,0,0.5)` |
| Contact Sheet Active | `0 1px 3px rgba(0,0,0,0.9)` |

### Glow Effects

| Element | Value |
|---------|-------|
| Status Light Active | `0 0 12px currentColor` |
| Indicator Pulse | `0 0 6px rgba(56,151,175,0.8)` to `0 0 12px rgba(56,151,175,1), 0 0 18px rgba(56,151,175,0.6)` |
| Indicator Glow | `0 0 8px rgba(56,151,175,0.8), 0 0 2px rgba(56,151,175,1)` to `0 0 16px rgba(56,151,175,1), 0 0 24px rgba(56,151,175,0.8), 0 0 4px rgba(56,151,175,1)` |

---

## Animations & Transitions

### Transition Durations

| Token | Value | Usage |
|-------|-------|-------|
| `--transition-instant` | 0s | Button interactions (no transition) |
| `--transition-fast` | 0.05s-0.15s | Film interframe |
| `--transition-normal` | 0.2s-0.3s | Modals, opacity changes, canvas transform |
| `--transition-smooth` | 0.3s | Panel transforms, canvas animations |

### Animation Keyframes

#### Status Light Animations

**pulse-green-gentle** (3s ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 8px #4ADE80, 0 0 4px #4ADE80; opacity: 1; }
50% { box-shadow: 0 0 14px #4ADE80, 0 0 8px #4ADE80; opacity: 0.95; }
```

**flash-orange** (600ms ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 16px #FF8C00, 0 0 8px #FF8C00; opacity: 1; transform: scale(1); }
50% { box-shadow: 0 0 24px #FF8C00, 0 0 12px #FF8C00; opacity: 0.9; transform: scale(1.05); }
```

**pulse-orange-steady** (1.5s ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 10px #FF8C00; opacity: 1; }
50% { box-shadow: 0 0 16px #FF8C00; opacity: 0.85; }
```

**pulse-turquoise** (2s ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 12px #3897AF, 0 0 6px #3897AF; opacity: 1; transform: scale(1); }
50% { box-shadow: 0 0 20px #3897AF, 0 0 10px #3897AF; opacity: 0.85; transform: scale(1.06); }
```

**pulse-turquoise-fast** (1s ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 12px #3897AF; opacity: 1; transform: scale(1); }
50% { box-shadow: 0 0 20px #3897AF; opacity: 0.8; transform: scale(1.08); }
```

**blink-red** (800ms ease-in-out infinite)
```css
0%, 49% { opacity: 1; box-shadow: 0 0 16px #EF4444; }
50%, 100% { opacity: 0.3; box-shadow: 0 0 4px #EF4444; }
```

**blink-orange** (800ms ease-in-out infinite)
```css
0%, 49% { opacity: 1; box-shadow: 0 0 16px #FF8C00; }
50%, 100% { opacity: 0.3; box-shadow: 0 0 4px #FF8C00; }
```

#### Indicator Animations

**indicatorPulse**
```css
0%, 100% { transform: scale(1); box-shadow: 0 0 6px rgba(56,151,175,0.8); }
50% { transform: scale(1.15); box-shadow: 0 0 12px rgba(56,151,175,1), 0 0 18px rgba(56,151,175,0.6); }
```

**indicatorGlow** (2s ease-in-out infinite)
```css
0%, 100% { box-shadow: 0 0 8px rgba(56,151,175,0.8), 0 0 2px rgba(56,151,175,1); }
50% { box-shadow: 0 0 16px rgba(56,151,175,1), 0 0 24px rgba(56,151,175,0.8), 0 0 4px rgba(56,151,175,1); }
```

**fadeIn** (0.3s ease)
```css
from { opacity: 0; }
to { opacity: 1; }
```

### Transform Behaviors

#### Button Press Transform
- **Default:** `translateY(0)`
- **Active:** `translateY(5px)` (most buttons)
- **Small Active:** `translateY(3px)` (small buttons)
- **Tab Active:** `translateY(1px)` (control tabs)

---

## Button Components

### Upload Button (`.upload-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | `min(400px, 85vw)` × 70px |
| **Background** | #D4CEC8 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 24px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Padding** | 0 20px |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 2px 0 rgba(255,255,255,0.3)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 4px 8px rgba(0,0,0,0.2)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `all 0s` |
| **Layout** | Flexbox, space-between alignment |

**Usage Notes:**
- Contains text "UPLOAD PHOTOS" and "≡" symbol
- Full-width responsive with max 400px
- Instant feedback (no transition delay)

---

### Preset Button (`.preset-btn`)

| Property | Value |
|----------|-------|
| **Background** | Default: #B3B3B3, Active: #000 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Font Size** | 22px |
| **Font Weight** | 700 |
| **Text Color** | Default: #000, Active: #fff |
| **Padding** | 6px |
| **Line Height** | 1.2 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.5)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `all 0s` |

**Variants:**
- SUPRA
- CHROME
- XXX

**Usage Notes:**
- Used in 4-column grid layout
- Active state inverts colors (black bg, white text)
- Instant press feedback

---

### Borders Button (`.borders-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 57px × 57px |
| **Background** | Default: #B3B3B3, Active: #000 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 18px |
| **Font Weight** | 700 |
| **Text Color** | Default: #000, Active: #fff |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.5)` |
| **Icon Size** | 32px × 32px |
| **Icon Filter** | Default: `brightness(0)`, Active: `brightness(0) invert(1)` |

**States:**
- Default: Light gray background, black icon
- Active: Black background, white icon, pressed state

---

### Copy/Paste Button (`.copy-paste-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 57px × 57px |
| **Background** | Default: #B3B3B3, Holding: #8CBABB |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 18px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Icon Size** | 28px × 28px |
| **Icon Filter** | `brightness(0)` |

**States:**
- Default: Light gray background
- Holding: Teal background (#8CBABB)
- Active: Pressed shadow state

**Icons:**
- Copy.svg (default)
- Paste.svg (when holding settings)

---

### Navigation Button (`.nav-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 57px × 57px (fixed width) |
| **Background** | #000 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Text Color** | #fff |
| **Font Size** | 22px |
| **Font Weight** | 700 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.5)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `none` |
| **Icon Size** | 32px × 32px |
| **Icon Filter** | `brightness(0) invert(1)` (white) |

**Variants:**
- Previous Button (Arrow Left)
- Next Button (Arrow Right)

**Disabled State:**
- `transform: translateY(5px)` (pressed position)
- `box-shadow: 0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.5)`
- Icon opacity: 0.25
- `pointer-events: none`

---

### Top Settings Button (`.settings-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 40px × 40px |
| **Background** | Default: #D4CEC8, Active: #000 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Padding** | 5px |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `none` |
| **Icon Filter** | Default: none, Active: `brightness(0) invert(1)` |

**Special States:**
- **Hold Button Active:** Background #6355B5 (purple), white icon
- **Has Settings:** Background #3897AF (turquoise), white icon

**Buttons:**
- Clear (Clear.svg)
- Hold (Unlocked.svg / Locked.svg)
- Intensity (Intensity.svg)
- CMYK (CMYK.svg)
- Brightness (Brightness.svg)
- Download (Download.svg)

---

### Gallery/Hamburger Icon (`.gallery-icon`)

| Property | Value |
|----------|-------|
| **Dimensions** | 40px × 40px |
| **Position** | Fixed, top-left (15px + safe-area) |
| **Background** | Default: #D4CEC8, Active: #000 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **SVG Size** | 20px × 20px |
| **SVG Stroke** | Default: #000, Active: #fff |
| **SVG Stroke Width** | 2 |

**SVG Elements:**
- Three horizontal lines at y: 6, 12, 18
- x: 4 to 20

---

### Slider Button (`.slider-btn`)

| Property | Value |
|----------|-------|
| **Height** | 57px (min-height) |
| **Background** | #B3B3B3 |
| **Border** | 3px solid #000 |
| **Border Radius** | 6px |
| **Font Size** | 35px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `all 0s` |
| **Icon Size** | 28px × 28px (Plus.svg, Minus.svg) |

**Usage:**
- Used for Bloom and Grain adjustments
- Part of 3-column grid: [- Button] [Value Display] [+ Button]

---

### CMYK Arrow Button (`.cmyk-arrow-btn`)

| Property | Value |
|----------|-------|
| **Height** | 48px |
| **Flex** | 1 (equal width in container) |
| **Background** | #B3B3B3 |
| **Border** | 3px solid #000 |
| **Border Radius** | 6px |
| **Font Size** | 26px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `all 0s` |
| **Icon Size** | 22px × 22px (Plus.svg, Minus.svg) |

**Usage:**
- Used in CMYK and Brightness slider controls
- Two buttons per slider (minus/plus)

---

### Intensity Arrow Button (`.intensity-arrow-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 54px × 54px |
| **Background** | #B3B3B3 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Transition** | `all 0s` |
| **Icon Size** | 22px × 22px |

---

### Guide Button (`.guide-btn`, `.guide-chapter-btn`)

**Standard Guide Button:**

| Property | Value |
|----------|-------|
| **Font** | 'PP Neue Bit', monospace |
| **Background** | Default: #B3B3B3, Primary: #3897AF |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font Size** | 22px |
| **Font Weight** | 700 |
| **Text Color** | Default: #000, Primary: #fff |
| **Padding** | 10px 20px |
| **Box Shadow** | Default: `0 6px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 2px 3px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(3px)` |

**Chapter Button:**

| Property | Value |
|----------|-------|
| **Font Size** | 26px |
| **Padding** | 16px |
| **Width** | 100% |
| **Text Align** | left |
| **Display** | block |
| **Margin Bottom** | 16px |

---

### Contact Sheet Close Button (`.contact-sheet-close`)

| Property | Value |
|----------|-------|
| **Dimensions** | 40px × 40px |
| **Background** | linear-gradient(180deg, #707070 0%, #505050 100%) |
| **Border** | 3px solid #3A3A3A |
| **Border Radius** | 4px |
| **Text Color** | #fff |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Icon Size** | 20px × 20px (Close.svg) |
| **Icon Filter** | `brightness(0) invert(1)` |

---

### GIF Close Button (`.gif-close-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 44px × 44px |
| **Background** | #1a1a1a |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 20px |
| **Font Weight** | 700 |
| **Text Color** | #B3B3B3 |
| **Content** | "✕" |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |

---

### Download Card Button (`.download-card-btn`)

| Property | Value |
|----------|-------|
| **Width** | 100% |
| **Background** | #B3B3B3 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Font Size** | 16px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Padding** | 8px 16px |
| **Line Height** | 1 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |

**Button Labels:**
- "SAVE CURRENT"
- "SAVE ALL"
- "SAVE GIF"

---

### Nav Dialog Button (`.nav-dialog-btn`)

| Property | Value |
|----------|-------|
| **Background** | #B3B3B3 |
| **Border** | 3px solid #000 |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Font Size** | 22px |
| **Font Weight** | 700 |
| **Text Color** | #000 |
| **Padding** | 6px |
| **Line Height** | 1.2 |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Layout** | Flexbox, centered |

**Grid Layout:**
- 3 columns (repeat(3, 1fr))
- Column gap: 8px
- Row gap: 16px

**Button Labels:**
- "EXIT"
- "GUIDE"
- "NEW ORDER"

---

### Contact Sheet Button (`.contact-sheet-btn`)

| Property | Value |
|----------|-------|
| **Background** | linear-gradient(180deg, #707070 0%, #505050 100%) |
| **Border** | 3px solid #3A3A3A |
| **Border Radius** | 4px |
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Font Size** | 16px |
| **Font Weight** | 700 |
| **Text Color** | #fff |
| **Padding** | 8px 16px |
| **Height** | 44px |
| **Box Shadow** | Default: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **White Space** | nowrap |

**Special Variants:**
- **Select Mode:** Background #000, transform translateY(5px), pressed shadow
- **Delete:** Background linear-gradient(180deg, #C84B4B 0%, #A03030 100%), border #8B2020

---

## Modal & View Components

### Contact Sheet View (`#contactSheetView`)

**Container:**
- Position: fixed, full viewport
- Background: #000
- Display: flex, column direction
- Z-index: 9999
- Overflow-y: auto

**Header (`.contact-sheet-header`):**
- Position: sticky, top: 0
- Background: #000
- Padding: 15px 15px 30px 15px
- Border-bottom: 2px solid #333
- Z-index: 10

**Logo:**
- Width: 160px
- Height: auto

**Grid (`.contact-sheet-grid`):**
- Grid: `repeat(auto-fill, minmax(150px, 1fr))`
- Gap: 15px
- Padding: 15px
- Padding-bottom: `calc(90px + env(safe-area-inset-bottom, 0px))`
- Responsive: `minmax(120px, 1fr)` on screens ≤360px

**Item (`.contact-sheet-item`):**
- Background: #1a1a1a
- Border: 2px solid #333 (default), 3px solid #3897AF (selected)
- Border-radius: 4px
- Overflow: hidden
- Transition: all 0s

**Item States:**
- **Active:** Bottom-right label "ACTIVE" (11px, #FF8C00)
- **Selected:** Border #3897AF (3px), checkmark badge (top-right, 24px circle)

**Item Image:**
- Width: 100%
- Aspect ratio: 10/8
- Object-fit: cover

**Label (`.contact-sheet-label`):**
- Padding: 10px 8px
- Font: 'PP Neue Bit', 'PP Fuji', monospace
- Font size: 16px
- Color: #999 (filename), #fff (bold)
- Background: #1a1a1a

**Footer (`.contact-sheet-footer`):**
- Position: fixed, bottom: 0
- Background: #000
- Padding: 15px + safe-area-inset-bottom
- Border-top: 2px solid #333
- Z-index: 10
- Layout: flex, centered, gap 10px

---

### GIF Preview Modal (`.gif-preview-modal`)

**Container:**
- Position: fixed, full viewport
- Background: #000
- Z-index: 200
- Display: none (flex when active)
- Flex direction: column
- Opacity: 0 (1 when active)
- Transition: opacity 0.3s ease

**Header (`.gif-preview-header`):**
- Padding: 20px
- Background: #000
- Z-index: 202
- Layout: flex, space-between

**Logo:**
- Width: 160px
- Height: auto

**Content (`.gif-preview-content`):**
- Flex: 1
- Layout: flex, centered
- Overflow: hidden

**Canvas (`.gif-preview-canvas`):**
- Max-width: 100%
- Max-height: 100%
- Width: auto
- Height: auto
- Background: #000
- Object-fit: contain

**Footer (`.gif-preview-footer`):**
- Padding: 16px 24px + safe-area-inset-bottom
- Background: #000
- Z-index: 201

**Credit (`.gif-preview-credit`):**
- Font: 'PP Neue Bit', monospace
- Font size: 24px
- Font weight: 700
- Color: #B3B3B3
- Content: "@OTISWEEKLY®"

---

### CMYK Slider Panel (`#cmykControls`)

**Container:**
- Position: fixed, below top nav
- Background: #6A6A6A
- Padding: 10px, padding-bottom: 18px
- Box-shadow: `inset 0 2px 0 rgba(0,0,0,0.3), inset 0 3px 0 rgba(255,255,255,0.1), inset 0 -2px 0 rgba(0,0,0,0.3)`
- Border-bottom: 3px solid rgba(0,0,0,0.5)
- Z-index: 148
- Transform: `translateY(calc(-100% - 78px - env(safe-area-inset-top)))` (hidden)
- Transform (active): `translateY(0)`
- Transition: transform 0.3s ease, opacity 0.3s ease

**Layout (`.cmyk-sliders`):**
- Grid: `1fr 1fr 36px 1fr 1fr`
- Gap: 8px
- Align items: start

**Slider Column (`.cmyk-slider`):**
- Display: flex, column
- Gap: 4px

**Value Display (`.cmyk-value`):**
- Min-height: 57px
- Background: `linear-gradient(180deg, #E8F0E8 0%, #F0F8F0 100%)`
- Border: 3px solid #000
- Border-radius: 6px 6px 0 0 (top corners)
- Font: 'PP Neue Bit', 'PP Fuji', monospace
- Font size: 26px (number), 10px (label)
- Font weight: 700
- Color: #000
- Box-shadow: `0 8px 0 #222222, inset 0 2px 4px rgba(0,0,0,0.15), inset 0 -1px 0 rgba(255,255,255,0.8)`

**Color Bar (`.cmyk-color-bar`):**
- Height: 10px
- Border-radius: 0 0 3px 3px (bottom corners)
- Border: 2px solid rgba(0,0,0,0.2)
- Background colors:
  - Cyan: #00FFFF
  - Magenta: #FF00FF
  - Yellow: #FFFF00
  - Density: #000

**Arrows Container (`.cmyk-arrows`):**
- Display: flex
- Gap: 4px

**Link Button (`.cmyk-link-btn`):**
- Dimensions: 36px × 36px
- Background: Default #B3B3B3, Active #3897AF
- Border: 3px solid #000
- Border-radius: 4px
- Padding: 5px
- Box-shadow: Default `0 6px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)`
- Active shadow: `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)`
- Icon filter (active): `brightness(0) invert(1)`
- Self-align: center

**Labels:**
- CYAN, MAGENTA, YELLOW, DENSITY

---

### Brightness Slider Panel (`#brightnessControls`)

**Structure:** Identical to CMYK Controls

**Layout (`.brightness-sliders`):**
- Grid: `1fr 1fr 36px 1fr 1fr`
- Gap: 8px

**Labels:**
- BRIGHT, CONTRAST, SHADOWS, HIGHLIGHT

**Auto Button (`.brightness-auto-btn`):**
- Same specs as `.cmyk-link-btn`
- Active background: #3897AF
- Icon: auto-off.svg (default), auto-on.svg (active)

---

### Intensity Slider Panel (`#intensityControls`)

**Container:**
- Same positioning and styling as CMYK/Brightness panels
- Min-height: 150px
- Display: flex, centered

**Layout (`.intensity-slider-container`):**
- Display: flex
- Align items: center
- Gap: 10px
- Justify content: center

**Value Display (`.intensity-value-display`):**
- Background: #4A4A4A
- Border: 3px solid #000
- Border-radius: 4px
- Height: 54px
- Padding: 0 25px
- Min-width: 140px
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)`
- Layout: flex column, centered

**Value Number:**
- Font: 'PP Neue Bit', 'PP Fuji', monospace
- Font size: 32px
- Font weight: 700
- Color: #fff
- Line height: 1

**Value Label:**
- Font: 'PP Neue Bit', 'PP Fuji', monospace
- Font size: 11px
- Color: #999
- Margin-top: 2px
- Letter-spacing: 1px
- Text: "INTENSITY"

---

### Download Options Panel (`#downloadOptions`)

**Container:**
- Same base styling as other panels
- Grid: `repeat(3, 1fr)`
- Gap: 10px
- Min-height: 150px

**Download Card (`.download-card`):**
- Display: flex, column
- Align items: center
- Gap: 6px

**Preview (`.download-preview`):**
- Width: 100%
- Aspect ratio: 10/8
- Background: #4A4A4A
- Border: 2px solid #222
- Border-radius: 4px
- Object-fit: cover

**Cards:**
1. Save Current (current photo preview)
2. Save All (contact sheet preview)
3. Save GIF (animated preview)

---

### Nav Dialog (`#navDialog`)

**Container:**
- Same base styling as other panels
- Grid: `repeat(3, 1fr)`
- Column gap: 8px
- Row gap: 16px
- Min-height: 150px

**Just Opened State:**
- Class `.just-opened` prevents interaction
- Pointer-events: none on container and buttons

**Buttons:**
- EXIT
- GUIDE
- NEW ORDER

---

### More Dialog (`#moreDialog`)

**Container:**
- Same base styling as other panels
- Grid: `repeat(2, 1fr)`
- Column gap: 8px
- Row gap: 16px
- Min-height: 150px

---

### History Panel (`#historyPanel`)

**Container:**
- Same base styling as other panels
- Max-height: `calc(100vh - 78px - env(safe-area-inset-top) - 230px - env(safe-area-inset-bottom, 20px) - 20px)`
- Overflow-y: auto
- Display: flex, column

**List (`.history-list`):**
- Display: flex, column
- Gap: 6px
- Flex: 1
- Overflow-y: auto

**Item (`.history-item`):**
- Display: flex
- Align items: center
- Justify content: space-between
- Font: 'PP Neue Bit', 'PP Fuji', monospace
- Font size: 18px
- Color: #fff
- Padding: 8px 0
- Border-bottom: 1px solid rgba(255,255,255,0.1)

**Item (Undone):**
- Opacity: 0.5

**Item Button (`.history-item-btn`):**
- Dimensions: 32px × 32px
- Background: #D4CEC8
- Border: 2px solid #000
- Border-radius: 4px
- Box-shadow: `0 4px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)`
- Active shadow: `0 2px 0 #222222, inset 0 2px 3px rgba(0,0,0,0.3)`
- Transform (active): `translateY(2px)`
- Icon size: 20px × 20px
- Margin-left: 6px

**Clear All Button (`.history-clear-all`):**
- Margin-top: 10px
- Padding: 12px
- Background: #D4CEC8
- Border: 3px solid #000
- Border-radius: 6px
- Font size: 16px
- Box-shadow: `0 6px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)`
- Active shadow: `0 3px 0 #222222, inset 0 2px 3px rgba(0,0,0,0.3)`
- Transform (active): `translateY(3px)`

**Done Button (`.history-done-btn`):**
- Margin-top: 10px
- Padding: 14px + safe-area-inset-bottom
- Background: #000
- Border: 3px solid #000
- Border-radius: 6px
- Font size: 18px
- Color: #fff
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)`
- Active shadow: `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.5)`
- Transform (active): `translateY(5px)`

---

### Download Progress Panel (`#downloadProgress`)

**Container:**
- Position: fixed, below top nav
- Background: #6A6A6A
- Padding: 10px, padding-bottom: 18px
- Z-index: 99999
- Same box-shadow and border as other panels
- Transform: hidden by default, `translateY(0)` when active
- Transition: transform 0.3s ease, opacity 0.3s ease

**Content (`.progress-content`):**
- Display: flex
- Align items: center
- Gap: 6px

**Bar Container (`.progress-bar-container`):**
- Flex: 1
- Height: 44px
- Background: #4A4A4A
- Border: 3px solid #000
- Border-radius: 4px
- Overflow: hidden
- Position: relative
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)`

**Bar Fill (`.progress-bar-fill`):**
- Height: 100%
- Background: #3897AF
- Transition: width 0.3s ease
- Box-shadow: `inset 0 1px 0 rgba(255,255,255,0.3)`
- Position: relative
- Z-index: 1

**Text (`.progress-text`):**
- Position: absolute, centered vertically
- Left: 15px, right: 15px
- Font: 'PP Neue Bit', monospace
- Font size: 20px
- Font weight: 700
- Color: #fff
- Text-shadow: `0 1px 2px rgba(0,0,0,0.5)`
- Z-index: 2
- White-space: nowrap
- Overflow: hidden
- Text-overflow: ellipsis

**Cancel Button (`.progress-cancel`):**
- Dimensions: 44px × 44px
- Background: #B3B3B3
- Border: 3px solid #000
- Border-radius: 4px
- Font: 'PP Neue Bit', monospace
- Font size: 20px
- Font weight: 700
- Color: #000
- Content: "✕"
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)`
- Active shadow: `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)`
- Transform (active): `translateY(5px)`

---

### Guide View (`#guidePanel`)

**Container:**
- Position: fixed, full viewport
- Background: #000
- Z-index: 250
- Transform: `translateY(100%)` (hidden), `translateY(0)` (active)
- Transition: transform 0.3s ease
- Overflow-y: auto
- Padding: 20px
- Padding-top: `calc(env(safe-area-inset-top, 0px) + 120px)`
- Padding-bottom: `calc(env(safe-area-inset-bottom, 20px) + 40px)`

**Logo:**
- Position: fixed
- Top: `calc(env(safe-area-inset-top, 0px) + 20px)`
- Left: 20px
- Width: 160px
- Z-index: 251

**Close Button:**
- Position: fixed
- Top: `calc(env(safe-area-inset-top, 0px) + 20px)`
- Right: 20px
- Dimensions: 44px × 44px
- Background: `linear-gradient(180deg, #707070 0%, #505050 100%)`
- Border: 3px solid #3A3A3A
- Border-radius: 4px
- Font: 'PP Neue Bit', monospace
- Font size: 24px
- Font weight: 700
- Color: #fff
- Content: "✕"
- Z-index: 251
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)`
- Active: `translateY(5px)`, `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)`

**Content (`.guide-content`):**
- Max-width: 800px
- Margin: 0 auto
- Font: 'PP Neue Bit', monospace
- Font size: 34px
- Line height: 1.1
- Color: #3897AF

**Section Heading:**
- Font size: 38px
- Margin: 0 0 15px 0
- Color: #3897AF
- Text-transform: uppercase

**Section Paragraph:**
- Font size: 34px
- Line height: 1.1
- Color: #999
- Margin: 0 0 15px 0

**Section List:**
- Font size: 34px
- Line height: 1.1
- Color: #999
- Margin: 12px 0
- Padding-left: 24px
- List item prefix: "> " (in #3897AF)

---

## Layout Components

### Upload Screen (`#uploadSection`)

**Container:**
- Display: flex, column, centered
- Width: 100%
- Height: 100vh
- Padding: 40px 20px
- Background: `linear-gradient(135deg, #37A4A4 0%, #258B8B 100%)`
- Position: relative

**Decorative Element (::after):**
- Content: empty string
- Position: absolute, full coverage
- Background: SVG noise filter (fractalNoise, baseFrequency 0.9)
- Opacity: 0.15
- Pointer-events: none
- Z-index: 1

**Decorative Stripes (::before):**
- Content: empty string
- Position: absolute
- Top: 20px
- Width: 100%
- Height: 132px
- Background: Complex linear gradient (horizontal stripes)
  - Pattern: #0D626E / #1D727E alternating bars
  - Spacing: 12px bars, 18px gaps, repeating 4 times
- Box-shadow: `inset 0 3px 6px rgba(0,0,0,0.4), inset 0 -3px 6px rgba(255,255,255,0.1)`
- Z-index: 0

**Content Container:**
- Transform: `translateY(-15%)`
- Position: relative
- Z-index: 2

**Hidden State:**
- Display: none

---

### Logo Container (`.logo-container`)

| Property | Value |
|----------|-------|
| **Position** | relative |
| **Margin Bottom** | 24px |
| **Padding** | 50px 50px 40px 50px |
| **Border** | 4px solid #0D626E |
| **Border Radius** | 4px |
| **Background** | rgba(13, 98, 110, 0.3) |
| **Width** | min(400px, 85vw) |
| **Box Shadow** | `inset 0 2px 0 rgba(255,255,255,0.1), inset 0 -2px 0 rgba(0,0,0,0.3), 0 4px 0 rgba(0,0,0,0.2)` |
| **Layout** | Flex column, centered, gap 8px |

**Logo Image:**
- Width: 100%
- Max-width: 280px
- Height: auto
- Image-rendering: crisp-edges
- Filter: contrast(1.1)

---

### Edit Section (`#editSection`)

**Container:**
- Display: none (flex when active)
- Flex direction: column
- Width: 100vw
- Height: 100vh (100dvh for dynamic viewport)
- Background: #6A6A6A
- Position: fixed, top-left corner

**Active State:**
- Display: flex

---

### Top Nav Bar (`.top-nav-bar`)

| Property | Value |
|----------|-------|
| **Position** | fixed, full width top |
| **Height** | `calc(78px + env(safe-area-inset-top))` |
| **Padding Top** | `env(safe-area-inset-top)` |
| **Background** | #6A6A6A |
| **Z-index** | 149 |
| **Box Shadow** | `inset 0 2px 0 rgba(0,0,0,0.3), inset 0 3px 0 rgba(255,255,255,0.1)` |
| **Border Bottom** | 2px solid rgba(0,0,0,0.4) |
| **Isolation** | isolate |

---

### Edit Footer (`.edit-footer`)

**Container:**
- Background: #6A6A6A
- Padding: 10px
- Padding-bottom: `calc(env(safe-area-inset-bottom, 20px) + 20px)`
- Display: flex, column
- Gap: 10px
- Position: fixed, bottom
- Overflow-y: auto
- Touch-action: manipulation
- Z-index: 150
- Box-shadow: `inset 0 2px 0 rgba(0,0,0,0.3), inset 0 3px 0 rgba(255,255,255,0.1)`
- Transition: transform 0.3s ease

**Panel Open States:**
- When any panel is open (CMYK, brightness, intensity, more, download, history):
  - Transform: `translateY(100%)` (hides footer)

**Content Structure:**
1. Profile Buttons Row (4-column grid, 8px gap)
2. Slider Controls Row (2-column grid, 8px gap)
   - Bloom slider (3-column: minus, value, plus)
   - Grain slider (3-column: minus, value, plus)
3. Footer Bottom (nav controls)

---

### Canvas Container (`.canvas-container`)

**Base State:**
- Flex: 1
- Display: flex, centered
- Padding-top: `calc(78px + env(safe-area-inset-top) + 8px)`
- Padding-left: 15px
- Padding-right: 15px
- Padding-bottom: `calc(230px + env(safe-area-inset-bottom, 0px) + 15px)`
- Overflow: hidden
- Position: relative
- Transition: all 0.3s ease
- Min-height: 0
- Touch-action: none
- Background: #4A4A4A
- Z-index: 1

**Panel Open States:**

| State | Padding Top | Padding Bottom |
|-------|-------------|----------------|
| `.cmyk-open` | `calc(78px + safe-area + 140px)` | 15px |
| `.brightness-open` | `calc(78px + safe-area + 140px)` | 15px |
| `.intensity-open` | `calc(78px + safe-area + 170px)` | 15px |
| `.more-open` | `calc(78px + safe-area + 170px)` | 15px |
| `.download-options-open` | `calc(78px + safe-area + 190px)` | 15px |
| `.history-open` | `calc(78px + safe-area + 30vh)` | 15px |
| `.download-open` | `calc(78px + safe-area + 90px)` | 15px |

**Canvas Element (`#canvas`):**
- Max-width: `calc(100vw - 30px)`
- Max-height: `calc(100vh - 340px - env(safe-area-inset-top) - env(safe-area-inset-bottom))`
- Width: auto
- Height: auto
- Object-fit: contain
- Cursor: pointer
- Transform-origin: center
- Will-change: transform
- Transition: `transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease`
- Position: relative
- Z-index: 100
- Touch-action: none

**Canvas Height Adjustments (for each panel state):**
- Dynamically calculated based on panel height
- Example: `.cmyk-open #canvas` has `max-height: calc(100vh - 78px - safe-area-top - 140px - 30px)`

---

### Background Toggle Bar (`.background-toggle-bar`)

**Container:**
- Position: fixed
- Bottom: `calc(230px + env(safe-area-inset-bottom, 20px) + 20px)`
- Full width
- Background: #6A6A6A
- Padding: 8px 15px
- Display: none (flex when needed)
- Align items: center
- Justify content: center
- Gap: 8px
- Z-index: 149
- Box-shadow: `inset 0 2px 0 rgba(0,0,0,0.3), inset 0 3px 0 rgba(255,255,255,0.1)`
- Touch-action: manipulation

**Toggle Buttons (`.bg-toggle-btn`):**
- Dimensions: 40px × 40px
- Border: 3px solid #000
- Border-radius: 4px
- Box-shadow: Default `0 6px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.2)`
- Active shadow: `0 2px 0 #222222, inset 0 2px 4px rgba(0,0,0,0.2)`
- Transform (active): `translateY(4px)`
- Position: relative

**Button Variants:**
- `.white` - Background: #fff
- `.grey` - Background: #4A4A4A
- `.black` - Background: #000

**Active Indicator (::after):**
- Content: empty string
- Position: absolute, top-right (-3px, -3px)
- Dimensions: 12px × 12px
- Background: #3897AF
- Border: 2px solid #fff
- Border-radius: 50%
- Box-shadow: `0 0 6px rgba(56,151,175,0.8)`
- Animation: indicatorGlow 2s ease-in-out infinite

---

### Footer Bottom (`.footer-bottom`)

**Container:**
- Width: 100%

**Nav Controls (`.nav-controls`):**
- Display: flex
- Align items: stretch
- Gap: 8px
- Min-height: 57px
- Width: 100%

**Layout:**
```
[Photo Counter (flex:1)] [Copy/Paste (57px)] [Prev (57px)] [Next (57px)]
```

---

### Top Controls (`.top-controls`)

**Container:**
- Position: fixed
- Top: `calc(15px + env(safe-area-inset-top))`
- Right: 10px
- Display: flex
- Gap: 6px
- Z-index: 150
- Touch-action: manipulation

**Buttons (6 total):**
1. Clear (`#clearBtn`)
2. Hold (`#holdBtn`)
3. Intensity (`#intensityBtn`)
4. CMYK (`#cmykToggle`)
5. Brightness (`#brightnessToggle`)
6. Download (`#downloadBtn`)

**Layout:**
- Horizontal flex row
- 6px gap between buttons
- Fixed positioning in top-right corner

---

## Special Components

### Status Lights (Upload Screen)

**Container (`.status-lights`):**
- Position: absolute
- Right: 15px
- Top: 50%
- Transform: `translateY(-50%)`
- Display: flex, column
- Gap: 10px

**Light (`.status-light`):**

| Property | Value |
|----------|-------|
| **Dimensions** | 12px × 12px |
| **Border Radius** | 50% |
| **Border** | 2px solid #0D626E |
| **Opacity** | 0.4 (default), 1 (active) |

**Active State:**
- Opacity: 1
- Box-shadow: `0 0 12px currentColor`
- Border: 1px solid rgba(255,255,255,0.2)
- Animation: varies by color

**Colors & Animations:**

| Color | Hex | Animation | Duration |
|-------|-----|-----------|----------|
| Green | #4ADE80 | pulse-green-gentle | 3s |
| Turquoise | #3897AF | pulse-turquoise | 2s |
| Orange | #FF8C00 | flash-orange | 600ms |
| Red | #EF4444 | blink-red | 800ms |

---

### Status Lights (Edit Screen)

**Light (`.edit-status-light`):**

| Property | Value |
|----------|-------|
| **Dimensions** | 8px × 8px (smaller than upload) |
| **Position** | Fixed, `calc(15px + env(safe-area-inset-top))` top, 61px left |
| **Border Radius** | 50% |
| **Border** | 1.5px solid #4A4A4A |
| **Opacity** | 0.4 (default), 1 (active) |
| **Z-index** | 151 |

**Colors & Animations:**
- Same as upload screen status lights
- Additional: pulse-orange-steady (1.5s) and pulse-turquoise-fast (1s)

---

### Photo Counter (`.photo-counter`)

| Property | Value |
|----------|-------|
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Min Width** | 66px |
| **Flex** | 1 (fills available space) |
| **Background** | `linear-gradient(180deg, #E8F0E8 0%, #F0F8F0 100%)` |
| **Border** | 3px solid #000 |
| **Border Radius** | 6px |
| **Box Shadow** | `0 8px 0 #222222, inset 0 2px 4px rgba(0,0,0,0.15), inset 0 -1px 0 rgba(255,255,255,0.8)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.15)` |
| **Text Color** | #000 |
| **Padding** | 12px |
| **Gap** | 6px |
| **Transition** | none |
| **Layout** | Flex row, centered |

**Icon (`.contact-icon`):**
- Height: 100%
- Width: auto
- Object-fit: contain
- Flex-shrink: 0
- Source: Contact.svg

**Number (`.photo-counter-number`):**
- Font size: 26px
- Font weight: 700
- Line height: 1
- Text align: center
- Width: 100%
- Format: "X/Y" (e.g., "1/36")

**Label (`.photo-counter-label`):**
- Font size: 9px
- Font weight: 700
- Color: #666
- Margin-top: 2px
- Letter-spacing: 0.5px

---

### Slider Value Display (`.slider-value`)

| Property | Value |
|----------|-------|
| **Font** | 'PP Neue Bit', 'PP Fuji', monospace |
| **Min Height** | 57px |
| **Background** | `linear-gradient(180deg, #E8F0E8 0%, #F0F8F0 100%)` |
| **Border** | 3px solid #000 |
| **Border Radius** | 6px |
| **Font Size** | 26px (number) |
| **Font Weight** | 700 |
| **Color** | #000 |
| **Box Shadow** | `0 8px 0 #222222, inset 0 2px 4px rgba(0,0,0,0.15), inset 0 -1px 0 rgba(255,255,255,0.8)` |
| **Active Shadow** | `0 3px 0 #222222, inset 0 3px 5px rgba(0,0,0,0.3)` |
| **Transform (Active)** | `translateY(5px)` |
| **Layout** | Flex column, centered, gap 2px |
| **User Select** | none |

**Number (`.slider-value-number`):**
- Width: 100%
- Text align: center
- Line height: 1
- Pointer-events: none

**Label (`.slider-value-label`):**
- Font size: 10px
- Font weight: 700
- Color: #666
- Letter-spacing: 0.5px
- Line height: 1
- Pointer-events: none

**Usage:**
- BLOOM value
- GRAIN value

---

### Intensity Indicator (`.intensity-indicator`)

| Property | Value |
|----------|-------|
| **Position** | absolute |
| **Z-index** | 9999 |
| **Pointer Events** | none |
| **Opacity** | 0 (default), 1 (active) |
| **Transition** | opacity 0s ease |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 72px |
| **Font Weight** | 700 |
| **Text Color** | #fff |
| **Text Align** | center |
| **Text Shadow** | `0 2px 8px rgba(0,0,0,0.8), 0 0 4px rgba(0,0,0,0.9)` |
| **Transform** | `translate(-50%, -50%)` (centered on canvas) |

**Usage:**
- Displays percentage overlay during intensity adjustments
- Content: "0%" to "100%"
- Positioned at canvas center

---

### Film Interframe (`.film-interframe`)

| Property | Value |
|----------|-------|
| **Position** | absolute, full coverage |
| **Background** | #000 |
| **Z-index** | 50 |
| **Opacity** | 0 (default), 1 (active) |
| **Pointer Events** | none |
| **Transition** | Default: `opacity 0.15s ease-out`, Active: `opacity 0.05s ease-in` |

**Usage:**
- Black flash between photo navigation
- Simulates film strip inter-frame behavior

---

### Hold Flash (`.hold-flash`)

| Property | Value |
|----------|-------|
| **Position** | absolute, centered (50%, 50%) |
| **Transform** | `translate(-50%, -50%)` |
| **Z-index** | 100 |
| **Opacity** | 0 (default), 1 (active) |
| **Pointer Events** | none |
| **Transition** | Default: `opacity 0.2s ease-out`, Active: `opacity 0.1s ease-in` |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 28px |
| **Font Weight** | 700 |
| **Text Color** | #E0E0E0 |
| **Text Align** | center |
| **Text Shadow** | `0 0 12px rgba(224,224,224,0.6), 0 2px 4px rgba(0,0,0,0.9)` |

**Content:**
- "SETTINGS HELD • TAP AGAIN TO RELEASE"

---

### Fullscreen Hint (`.fullscreen-hint`)

| Property | Value |
|----------|-------|
| **Position** | fixed, bottom-center |
| **Bottom** | 20px |
| **Transform** | `translateX(-50%)` |
| **Z-index** | 9999 |
| **Pointer Events** | none |
| **Opacity** | 0 (default), 1 (when `body.fullscreen-preview`) |
| **Transition** | opacity 0.3s ease |
| **Font** | 'PP Neue Bit', monospace |
| **Font Size** | 20px |
| **Font Weight** | 400 |
| **Text Color** | rgba(255,255,255,0.9) |
| **Text Align** | center |
| **Text Shadow** | `0 2px 6px rgba(0,0,0,0.9)` |

**Icon:**
- Shrink.svg (16px height)
- Filter: `brightness(0) invert(1) drop-shadow(0 2px 6px rgba(0,0,0,0.9))`
- Vertical align: middle
- Margin-right: 8px

**Usage:**
- Appears in fullscreen preview mode
- Hints at exit gesture/button

---

### Progress Bar

**Container (`.progress-bar-container`):**
- Flex: 1
- Height: 44px
- Background: #4A4A4A
- Border: 3px solid #000
- Border-radius: 4px
- Overflow: hidden
- Position: relative
- Box-shadow: `0 8px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.1)`

**Fill (`.progress-bar-fill`):**
- Height: 100%
- Background: #3897AF
- Transition: width 0.3s ease
- Box-shadow: `inset 0 1px 0 rgba(255,255,255,0.3)`
- Position: relative
- Z-index: 1
- Width: 0%-100% (dynamically set)

**Text (`.progress-text`):**
- Position: absolute, centered
- Font: 'PP Neue Bit', monospace
- Font size: 20px
- Font weight: 700
- Color: #fff
- Text-shadow: `0 1px 2px rgba(0,0,0,0.5)`
- Z-index: 2
- White-space: nowrap
- Overflow: hidden
- Text-overflow: ellipsis

**Content Examples:**
- "Exporting..."
- "Rendering frame X/Y..."
- "Encoding GIF..."

---

### Control Tabs (`.control-tab`)

| Property | Value |
|----------|-------|
| **Background** | Default: #B3B3B3, Active: #000 |
| **Border** | 2px solid #000 |
| **Border Radius** | 3px |
| **Font Size** | 7px (label), 9px (value) |
| **Font Weight** | 700 |
| **Text Color** | Default: #000, Active: #fff |
| **Box Shadow** | Default: `0 2px 0 #222222` |
| **Active Shadow** | `0 1px 0 #222222` |
| **Transform (Active)** | `translateY(1px)` |
| **Transition** | `all 0s` |
| **Layout** | Flex column, centered, gap 1px |

**Grid Layout:**
- Grid: `repeat(4, 1fr)`
- Gap: 4px
- Height: 40px

---

### CMYK Color Bars (`.cmyk-color-bar`)

| Property | Value |
|----------|-------|
| **Height** | 10px |
| **Border Radius** | 0 0 3px 3px (bottom corners only) |
| **Border** | 2px solid rgba(0,0,0,0.2) |

**Color Values:**

| Class | Background | Usage |
|-------|------------|-------|
| `.cyan` | #00FFFF | Cyan slider |
| `.magenta` | #FF00FF | Magenta slider |
| `.yellow` | #FFFF00 | Yellow slider |
| `.density` | #000 | Density/Black slider |
| `.brightness` | #000 | Brightness slider |
| `.contrast` | #000 | Contrast slider |
| `.shadows` | #000 | Shadows slider |
| `.highlights` | #000 | Highlights slider |

---

### Contact Sheet Edit Button (`.contact-sheet-edit-btn`)

| Property | Value |
|----------|-------|
| **Dimensions** | 24px × 24px |
| **Background** | #D4CEC8 |
| **Border** | 2px solid #000 |
| **Border Radius** | 4px |
| **Box Shadow** | Default: `0 4px 0 #222222, inset 0 1px 0 rgba(255,255,255,0.3)` |
| **Active Shadow** | `0 2px 0 #222222, inset 0 2px 3px rgba(0,0,0,0.2)` |
| **Transform (Active)** | `translateY(2px)` |
| **SVG Size** | 14px × 14px |
| **Layout** | Flex, centered |
| **Flex Shrink** | 0 |

---

### Media Queries

**Small Screens (≤360px):**
- Action buttons: font-size 9px, padding 6px 10px
- Save button: padding 8px 16px, font-size 11px
- Control tab: font-size 8px, padding 6px 4px
- Preset button: font-size 8px, padding 8px 3px
- Contact sheet grid: `minmax(120px, 1fr)`, gap 10px

**Standalone Mode (`body.standalone-mode`):**
- Adjusts safe-area-inset handling for installed PWA
- Reduces bottom padding to 10px for edit footer
- Increases canvas container padding-bottom
- Adjusts various panel max-heights

---

## Usage Guidelines

### Button Interaction Pattern

All buttons follow consistent interaction patterns:

1. **Visual Feedback:**
   - No transition delay (`transition: all 0s`)
   - Instant press response
   - Shadow changes to indicate depth
   - Transform translateY to simulate physical press

2. **Active States:**
   - Shadow reduces (e.g., 8px → 3px)
   - translateY(5px) for most buttons
   - translateY(3px) for smaller buttons
   - translateY(1px) for tabs

3. **Touch Optimization:**
   - `-webkit-tap-highlight-color: transparent`
   - `touch-action: manipulation`
   - `will-change: transform, box-shadow` for performance

### Color State Indicators

- **Default state:** Light neutral colors (#D4CEC8, #B3B3B3)
- **Active/Selected:** Black background, white text
- **Has Settings:** Turquoise (#3897AF) with white icon
- **Special Hold:** Purple (#6355B5)
- **Holding Clipboard:** Teal (#8CBABB)

### Panel Animation Pattern

All dropdown panels follow this structure:
- Transform: `translateY(calc(-100% - 78px - env(safe-area-inset-top)))` (hidden)
- Transform (active): `translateY(0)`
- Transition: `transform 0.3s ease, opacity 0.3s ease`
- Opacity: 0 (hidden), 1 (active)
- Pointer-events: none (hidden), auto (active)

### Responsive Behavior

- Upload button: `min(400px, 85vw)` width
- Logo container: `min(400px, 85vw)` width
- Safe area insets: All fixed elements respect `env(safe-area-inset-*)`
- Dynamic viewport height: Uses `100dvh` where appropriate
- Grid layouts: Auto-fill with minimum sizing

---

## Z-Index Hierarchy

| Layer | Z-index | Components |
|-------|---------|------------|
| Base | 0-1 | Upload decorations, canvas container |
| Film Interframe | 50 | Black flash between photos |
| Canvas | 100 | Main canvas element |
| Hold Flash | 100 | Settings held message |
| Panels | 148 | CMYK, Brightness, Intensity, Nav, Download, History, More dialogs |
| Nav Bar/Footer | 149-150 | Top nav, edit footer, gallery icon, top controls, bg toggle |
| Edit Status Light | 151 | Small status light in edit view |
| GIF Preview | 200-202 | GIF preview modal and contents |
| Guide Panel | 250-251 | Full-screen guide view |
| Intensity Indicator | 9999 | Large percentage overlay |
| Contact Sheet | 9999 | Full-screen contact sheet view |
| Progress Bar | 99999 | Download progress (highest priority) |
| Debug Toggle | 100000 | Mobile debug console (dev only) |

---

## Font Loading

**PP Fuji:**
- Formats: woff2, woff, ttf
- Weights: 400, 500, 700
- font-display: swap

**PP Neue Bit:**
- Formats: woff, ttf
- Weights: 400, 700
- font-display: swap

**Fallbacks:**
- PP Fuji → -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- PP Neue Bit → monospace

---

## Accessibility Notes

1. **Touch Targets:** All interactive elements meet minimum 40px × 40px (nav buttons 57px)
2. **Visual Feedback:** Clear active/pressed states with shadow and transform
3. **Text Contrast:** High contrast ratios (black on light backgrounds, white on dark)
4. **Safe Areas:** All fixed elements respect iOS safe area insets
5. **No Transitions:** Instant button feedback for responsive feel

---

## Performance Optimizations

1. **will-change:** Applied to frequently animated elements (transform, box-shadow)
2. **Transitions:** Disabled on buttons (0s) for instant feedback
3. **Transform Only:** Layout changes use transform (not top/left) for GPU acceleration
4. **Image Rendering:** Crisp-edges for logo, optimize-contrast where appropriate
5. **Touch Action:** Manipulation or none to prevent default behaviors

---

## Design Principles

1. **Physical Skeuomorphism:** Buttons simulate physical depth with shadows and press animations
2. **Instant Feedback:** No transition delays on interactive elements
3. **Film Lab Aesthetic:** Turquoise/teal brand color, vintage equipment styling
4. **Clear Hierarchy:** Consistent sizing, spacing, and visual weight
5. **Mobile-First:** Optimized for touch, safe areas, and small screens

---

**End of Design System Specification**
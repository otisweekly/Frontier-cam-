# SVG Icon Inventory - Frontier Digi Processor

## Overview
This document provides a comprehensive inventory of all SVG icons used in the Frontier Digi Processor application. Each icon is documented with its technical specifications and usage context for Figma reference.

---

## Quick Reference Table

| Icon Name | ViewBox | Category | Colors | Stroke Width | Primary Use | Display Size |
|-----------|---------|----------|--------|--------------|-------------|--------------|
| Arrow Left | 36x36 | Navigation | Black | 3px | Left navigation | 24-36px |
| Arrow Right | 36x36 | Navigation | Black | 3px | Right navigation | 24-36px |
| Arrow Up | 24x24 | Navigation | Black | 2px | Vertical navigation | 24px |
| Arrow Down | 24x24 | Navigation | Black | 2px | Vertical navigation | 24px |
| Plus | 36x36 | Controls | Black | 3px | Add/Create | 36px |
| Minus | 36x36 | Controls | Black | 3px | Remove/Decrease | 36px |
| Close | 36x36 | Controls | Black | 3px | Close dialog/modal | 36px |
| Delete | 36x36 | Controls | Black | 3px | Remove item | 36px |
| Copy | 36x36 | Controls | Black | 3px | Duplicate content | 36px |
| Paste | 36x36 | Controls | Black | 3px | Insert clipboard | 36px |
| Edit | 36x36 | Tools | Black | 3px | Edit mode | 36px |
| Preview | 36x36 | Tools | Black | 3px | View/Preview | 36px |
| Download | 36x36 | Tools | Black | 3px | Export/Save file | 36px |
| Resize | 36x36 | Tools | Black | 3px | Adjust dimensions | 36px |
| Brightness | 36x36 | Adjustments | Black | 3px | Brightness control | 36px |
| Lighting | 36x36 | Adjustments | Black | 3px | Lighting adjustment | 36px |
| Intensity | 36x36 | Adjustments | Black | 3px | Intensity control | 36px |
| Light | 36x36 | Adjustments | Black | 3px | Light/Day mode | 36px |
| Angle | 36x36 | Adjustments | Black | 3px | Angle/Rotation | 36px |
| S Curve | 36x36 | Adjustments | Black | 3px | Curves adjustment | 36px |
| CMYK | 36x36 | Color Modes | Black | 3px | CMYK color space | 36px |
| Contact | 36x36 | States | Black | 3px | Contact/Layer lock | 36px |
| More | 36x36 | Controls | Black | 3px | More options menu | 36px |
| Fast Forward | 36x36 | Playback | Black | 3px | Forward action | 36px |
| Rewind | 36x36 | Playback | Black | 3px | Backward action | 36px |
| Redo | 36x36 | History | Black | 3px | Redo action | 36px |
| Undo | 36x36 | History | Black | 3px | Undo action | 36px |
| Shrink | 36x38 | Transform | Black | 3px | Shrink/Scale down | 36px |
| Clear | 36x36 | Controls | Black | 3px | Clear selection | 36px |
| Borders | 36x36 | Tools | Black | 3px | Border settings | 36px |
| Picker | 36x36 | Tools | Black | 3px | Color picker | 36px |
| Logo | 122x70 | Branding | Multi-color | N/A | App branding | 122x70px |
| Auto | 36x36 | States | Black | 3px | Automatic mode | 36px |
| Auto Light | 36x36 | States | Black | 3px | Auto light detection | 36px |
| Auto CMYK | 36x36 | States | Black | 3px | Auto CMYK mode | 36px |
| Auto-Off | 36x36 | Toggle States | Black | 3px | Auto disabled | 36px |
| Auto-On | 36x36 | Toggle States | Black | 3px | Auto enabled | 36px |
| Active Linked | 36x36 | States | Black | 3px | Link active state | 36px |
| Default Unlinked | 36x36 | States | Black | 3px | Link inactive state | 36px |
| Hold | 36x36 | States | Black | 3px | Hold/Preserve state | 36px |
| Locked | 36x36 | Lock States | Black | 3px | Layer locked | 36px |
| Unlocked | 36x36 | Lock States | Black | 3px | Layer unlocked | 36px |

---

## Icon Categories

### Navigation Icons
Used for directional navigation and movement through the application.

#### Arrow Left
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Arrow Left.svg`
- **ViewBox:** 36x36
- **Description:** Left-pointing arrow with filled triangular head
- **Colors:** Black fill
- **Stroke Width:** N/A (filled path)
- **Usage:** Navigate to previous item, back button in workflows
- **Display Size:** 24-36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M21.5858 30L24 30L24 6L21.5858 6L9.5858 18L21.5858 30Z" fill="black"/>
</svg>
```

#### Arrow Right
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Arrow right.svg`
- **ViewBox:** 36x36
- **Description:** Right-pointing arrow with filled triangular head
- **Colors:** Black fill
- **Stroke Width:** N/A (filled path)
- **Usage:** Navigate to next item, forward button in workflows
- **Display Size:** 24-36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M14.4142 6L12 6V30H14.4142L26.4142 18L14.4142 6Z" fill="black"/>
</svg>
```

#### Arrow Up
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Arrow up.svg`
- **ViewBox:** 24x24
- **Description:** Upward-pointing chevron/polyline
- **Colors:** Black stroke
- **Stroke Width:** 2px
- **Stroke Linecap:** Square
- **Usage:** Move up in lists, collapse, or increase value
- **Display Size:** 24px
- **SVG Code:**
```xml
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <polyline points="6,15 12,9 18,15" stroke="black" stroke-width="2" stroke-linecap="square"/>
</svg>
```

#### Arrow Down
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Arrow down.svg`
- **ViewBox:** 24x24
- **Description:** Downward-pointing chevron/polyline
- **Colors:** Black stroke
- **Stroke Width:** 2px
- **Stroke Linecap:** Square
- **Usage:** Move down in lists, expand, or decrease value
- **Display Size:** 24px
- **SVG Code:**
```xml
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <polyline points="6,9 12,15 18,9" stroke="black" stroke-width="2" stroke-linecap="square"/>
</svg>
```

---

### Control Icons
Primary interaction controls for user actions.

#### Plus
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Plus.svg`
- **ViewBox:** 36x36
- **Description:** Plus sign with horizontal and vertical strokes
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Add new item, increase value, open add dialog
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M18 7V29" stroke="black" stroke-width="3"/>
  <path d="M7 18H29" stroke="black" stroke-width="3"/>
</svg>
```

#### Minus
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Minus.svg`
- **ViewBox:** 36x36
- **Description:** Horizontal minus/dash line
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Remove/decrease value, collapse sections
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M7 18H29" stroke="black" stroke-width="3"/>
</svg>
```

#### Close
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Close.svg`
- **ViewBox:** 36x36
- **Description:** X symbol formed by two diagonal strokes
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Close dialogs, cancel operations, dismiss panels
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M28 8L8 28" stroke="black" stroke-width="3"/>
  <path d="M8 8L28 28" stroke="black" stroke-width="3"/>
</svg>
```

#### Delete
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Delete.svg`
- **ViewBox:** 36x36
- **Description:** Trash can icon with lid and items
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Remove item, trash action
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M6 12H30" stroke="black" stroke-width="3"/>
  <path d="M9 12H27L24 29H12L9 12Z" stroke="black" stroke-width="3"/>
  <path d="M14 12V11C14 8.79086 15.7909 7 18 7C20.2091 7 22 8.79086 22 11V12" stroke="black" stroke-width="3"/>
</svg>
```

#### Copy
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Copy.svg`
- **ViewBox:** 36x36
- **Description:** Two overlapping document/clipboard squares
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Duplicate content, copy to clipboard
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M23.25 12.75H9.25V26.75H23.25V12.75Z" stroke="black" stroke-width="3"/>
  <path d="M10.8125 8.1875H15.8125" stroke="black" stroke-width="3"/>
  <path d="M22.8125 8.1875H17.8125" stroke="black" stroke-width="3"/>
  <path d="M24.8125 8.1875H27.8125V11.1875" stroke="black" stroke-width="3"/>
  <path d="M27.8125 18.1875V13.1875" stroke="black" stroke-width="3"/>
  <path d="M27.8125 25.1875V20.1875" stroke="black" stroke-width="3"/>
</svg>
```

#### Paste
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/paste.svg`
- **ViewBox:** 36x36
- **Description:** Document with checkmark indicating paste/insert action
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Insert clipboard content
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M22 26.2667L25.3158 30L31.5 24.5" stroke="black" stroke-width="3"/>
  <path d="M8.1875 25.1875L8.1875 20.1875" stroke="black" stroke-width="3"/>
  <path d="M8.1875 13.1875L8.1875 18.1875" stroke="black" stroke-width="3"/>
  <path d="M8.1875 11.1875L8.1875 8.1875L11.1875 8.1875" stroke="black" stroke-width="3"/>
  <path d="M18.1875 8.1875L13.1875 8.1875" stroke="black" stroke-width="3"/>
  <path d="M25.1875 8.1875L20.1875 8.1875" stroke="black" stroke-width="3"/>
  <path d="M18.3846 27H13V13H27V22.6923" stroke="black" stroke-width="3"/>
</svg>
```

#### More
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/More.svg`
- **ViewBox:** 36x36
- **Description:** Three horizontal dots (kebab menu)
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Open context menu, show more options
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M11.4999 17.5H10.4995V18.5004H11.4999V17.5Z" stroke="black" stroke-width="3"/>
  <path d="M18.5001 17.5H17.4998V18.5004H18.5001V17.5Z" stroke="black" stroke-width="3"/>
  <path d="M25.5005 17.5H24.5002V18.5004H25.5005V17.5Z" stroke="black" stroke-width="3"/>
</svg>
```

#### Clear
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Clear.svg`
- **ViewBox:** 36x36
- **Description:** Circular refresh icon with curved arrows
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Reset/clear selection or values
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M29 18C29 15.0826 27.8411 12.2847 25.7782 10.2218C23.7153 8.15893 20.9174 7 18 7C12 7 9.5 11.25 7 14M18 29C15.0826 29 12.2847 27.8411 10.2218 25.7782C8.15892 23.7153 7 20.9174 7 18" stroke="black" stroke-width="3"/>
  <path d="M7 10V14H11" stroke="black" stroke-width="3"/>
  <path d="M18 11V18H23" stroke="black" stroke-width="3"/>
  <path d="M29 21L21 29" stroke="black" stroke-width="3"/>
  <path d="M29 29L21 21" stroke="black" stroke-width="3"/>
</svg>
```

---

### Tool Icons
Icons representing specific editing and adjustment tools.

#### Edit
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Edit.svg`
- **ViewBox:** 36x36
- **Description:** Pencil/pen editing tool with diagonal line
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Edit mode, modify properties, text editing
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M25.5 17.5L18.5 10.5L21.5 7.5L28.5 14.5L25.5 17.5Z" stroke="black" stroke-width="3"/>
  <path d="M25.5 17.5L15 28H8V21L18.5 10.5L25.5 17.5Z" stroke="black" stroke-width="3"/>
</svg>
```

#### Preview
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Preview.svg`
- **ViewBox:** 36x36
- **Description:** Eye symbol for preview/view action
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Preview result, show/hide visibility
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M7 26.0625V20.0625C7 13.9874 11.9249 9.0625 18 9.0625C24.0751 9.0625 29 13.9874 29 20.0625V26.0625" stroke="black" stroke-width="3"/>
  <path d="M11 26.0625V20.0625C11 16.1965 14.134 13.0625 18 13.0625C21.866 13.0625 25 16.1965 25 20.0625V26.0625" stroke="black" stroke-width="3"/>
  <path d="M15 26.0625V20.0625C15 18.4056 16.3431 17.0625 18 17.0625C19.6569 17.0625 21 18.4056 21 20.0625V26.0625" stroke="black" stroke-width="3"/>
</svg>
```

#### Download
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Download.svg`
- **ViewBox:** 36x36
- **Description:** Download arrow pointing down to tray
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Download/export file
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M8 23V28H28V23" stroke="black" stroke-width="3"/>
  <path d="M12 16L18 22L24 16" stroke="black" stroke-width="3"/>
  <path d="M18 22V7" stroke="black" stroke-width="3"/>
</svg>
```

#### Resize
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Resize.svg`
- **ViewBox:** 36x36
- **Description:** Expand/resize arrows with search circle and corner marks
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Adjust dimensions, scale objects
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M20 16V24" stroke="black" stroke-width="3"/>
  <path d="M16 20H24" stroke="black" stroke-width="3"/>
  <path d="M27 20C27 23.866 23.866 27 20 27C16.134 27 13 23.866 13 20C13 16.134 16.134 13 20 13C23.866 13 27 16.134 27 20Z" stroke="black" stroke-width="3"/>
  <path d="M28.9995 29L24.9492 24.9497" stroke="black" stroke-width="3"/>
  <path d="M8 23.5V28H12.5" stroke="black" stroke-width="3"/>
  <path d="M8 14.5V21.5" stroke="black" stroke-width="3"/>
  <path d="M8 12.5V8H12.5" stroke="black" stroke-width="3"/>
  <path d="M14.5 8H21.5" stroke="black" stroke-width="3"/>
  <path d="M23.5 8H28V12.5" stroke="black" stroke-width="3"/>
</svg>
```

#### Borders
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/borders.svg`
- **ViewBox:** 36x36
- **Description:** Rectangle with border/frame lines
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Border/frame settings
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M26 9L10 9" stroke="black" stroke-width="3"/>
  <path d="M26 27L10 27" stroke="black" stroke-width="3"/>
  <path d="M11 14L25 14L25 22L11 22L11 14Z" stroke="black" stroke-width="3"/>
</svg>
```

#### Picker
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/picker.svg`
- **ViewBox:** 36x36
- **Description:** Eyedropper/color picker tool with angle lines
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Color selection, sample colors
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M13.6069 7.93726L28.0628 22.3931" stroke="black" stroke-width="3"/>
  <path d="M24.3892 5.71332C27.6461 5.71332 30.2864 8.35359 30.2864 11.6105C30.2864 13.1745 29.665 14.6745 28.5592 15.7805L17.4984 26.8411H11.9386L9.06561 29.7133L6.28564 26.9334L9.15859 24.0611V18.5012L20.2193 7.44057C21.3251 6.33463 22.8251 5.71332 24.3892 5.71332Z" stroke="black" stroke-width="3"/>
</svg>
```

---

### Adjustment Icons
Icons for image and color adjustments.

#### Brightness
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Brightness.svg`
- **ViewBox:** 36x36
- **Description:** Sun icon with rays radiating from center
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Brightness control, exposure adjustment
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M18 3V7.5" stroke="black" stroke-width="3"/>
  <path d="M18 28.5V33" stroke="black" stroke-width="3"/>
  <path d="M28.7285 7.27197L25.5465 10.454" stroke="black" stroke-width="3"/>
  <path d="M10.4547 25.5457L7.27271 28.7277" stroke="black" stroke-width="3"/>
  <path d="M33 18H28.5" stroke="black" stroke-width="3"/>
  <path d="M7.5 18H3" stroke="black" stroke-width="3"/>
  <path d="M28.7285 28.7277L25.5465 25.5457" stroke="black" stroke-width="3"/>
  <path d="M10.4547 10.454L7.27271 7.27197" stroke="black" stroke-width="3"/>
  <path d="M10.5 18C10.5 22.1421 13.8579 25.5 18 25.5V10.5C13.8579 10.5 10.5 13.8579 10.5 18Z" stroke="black" stroke-width="3"/>
</svg>
```

#### Lighting
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Lighting.svg`
- **ViewBox:** 36x36
- **Description:** Lightbulb icon indicating illumination
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Lighting adjustment, lamp/illumination control
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M18 7C13.0294 7 9 11.0294 9 16C9 19.5337 11.0366 22.5918 14 24.0645V25.5H22V24.0645C24.9634 22.5918 27 19.5337 27 16C27 11.0294 22.9706 7 18 7Z" stroke="black" stroke-width="3"/>
  <path d="M15 30H21" stroke="black" stroke-width="3"/>
</svg>
```

#### Light
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Light.svg`
- **ViewBox:** 36x36
- **Description:** Lightbulb with lightning bolt indicating brightness/light mode
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Light mode, illuminate effect
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M18 7C13.0294 7 9 11.0294 9 16C9 19.5337 11.0366 22.5918 14 24.0645V25.5H22V24.0645C24.9634 22.5918 27 19.5337 27 16C27 11.0294 22.9706 7 18 7Z" stroke="black" stroke-width="3"/>
  <path d="M15 30H21" stroke="black" stroke-width="3"/>
  <path d="M19.0529 11L15.3687 15.9845H20.6318L16.9476 21" stroke="black" stroke-width="3"/>
</svg>
```

#### Intensity
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Intensity.svg`
- **ViewBox:** 36x36
- **Description:** Circular dial with surrounding dots showing intensity levels
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Intensity/strength adjustment
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M12.1461 13.338C8.91314 16.571 8.91314 21.8127 12.1461 25.0456C15.3791 28.2786 20.6207 28.2786 23.8537 25.0456C27.0867 21.8127 27.0867 16.571 23.8537 13.338C20.6207 10.1051 15.3791 10.1051 12.1461 13.338Z" stroke="black" stroke-width="3"/>
  <path d="M17.8531 10.919L17.8531 17.3456" stroke="black" stroke-width="3"/>
  <path d="M3.80835 19.1918H6.76496" stroke="black" stroke-width="3"/>
  <path d="M7.96484 9.15674L10.0555 11.2474" stroke="black" stroke-width="3"/>
  <path d="M29.2351 19.1918H32.1917" stroke="black" stroke-width="3"/>
  <path d="M25.9446 27.1363L28.0351 29.227" stroke="black" stroke-width="3"/>
  <path d="M18 5V7.95662" stroke="black" stroke-width="3"/>
  <path d="M28.0353 9.15674L25.9446 11.2474" stroke="black" stroke-width="3"/>
  <path d="M10.0555 27.1363L7.96484 29.227" stroke="black" stroke-width="3"/>
</svg>
```

#### Angle
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Angle.svg`
- **ViewBox:** 36x36
- **Description:** Diamond shape with lines indicating angle/rotation
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Angle adjustment, rotation control
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M21.4981 9.49816L18 6L14.5019 9.49816H9.49816V14.5019L6 18L9.49816 21.4981V26.5019H14.5019L18 30L21.4981 26.5019H26.5019V21.4981L30 18L26.5019 14.5019V9.49816H21.4981Z" stroke="black" stroke-width="3"/>
  <path d="M15.3327 19.41H20.6672M14 23L17.2725 14H18.7274L22 23" stroke="black" stroke-width="3"/>
</svg>
```

#### S Curve
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/S curve.svg`
- **ViewBox:** 36x36
- **Description:** S-shaped curve indicating curves adjustment
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Curves adjustment, tone mapping
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <g clip-path="url(#clip0_40_938)">
    <path d="M22.6666 13.3334L13.3333 22.6667" stroke="black" stroke-width="3"/>
    <path d="M15.6667 12.1667L22.0834 5.75L30.2501 13.9167L23.8334 20.3333" stroke="black" stroke-width="3"/>
    <path d="M20.3333 23.8333L13.9167 30.25L5.75 22.0833L12.1667 15.6666" stroke="black" stroke-width="3"/>
  </g>
</svg>
```

---

### Color Mode Icons

#### CMYK
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/CMYK.svg`
- **ViewBox:** 36x36
- **Description:** CMYK color separation indicator with four separated lines
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** CMYK color mode indication
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M12 6V20M12 30V23" stroke="black" stroke-width="3"/>
  <path d="M24 30V16M24 6V13" stroke="black" stroke-width="3"/>
  <path d="M7 23H17" stroke="black" stroke-width="3"/>
  <path d="M19 13H29" stroke="black" stroke-width="3"/>
</svg>
```

---

### Transform Icons

#### Shrink
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Shrink.svg`
- **ViewBox:** 36x38
- **Description:** Shrink/compress arrows pointing inward
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Drop Shadow:** Yes (filter applied)
- **Usage:** Scale down, shrink objects
- **Display Size:** 36px
- **Note:** Contains shadow filter effect

---

### Playback Icons

#### Fast Forward
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Fast forward.svg`
- **ViewBox:** 36x36
- **Description:** Double right arrows indicating forward/skip ahead
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Skip forward, fast forward action
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M16.5 7.5L27 18L16.5 28.5" stroke="black" stroke-width="3"/>
  <path d="M20 18L9 7H8V29H9L20 18Z" stroke="black" stroke-width="3"/>
</svg>
```

#### Rewind
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Rewind.svg`
- **ViewBox:** 36x36
- **Description:** Double left arrows indicating backward/rewind
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Rewind, go back in sequence
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M19.5 28.5L9 18L19.5 7.5" stroke="black" stroke-width="3"/>
  <path d="M16 18L27 29L28 29L28 7L27 7L16 18Z" stroke="black" stroke-width="3"/>
</svg>
```

---

### History Icons

#### Undo
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Undo.svg`
- **ViewBox:** 36x36
- **Description:** Curved arrow pointing left (undo action)
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Undo last action, revert changes
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M7.5 15L21 15C25.4183 15 29 18.5817 29 23L29 28" stroke="black" stroke-width="3"/>
  <path d="M13.5 21L7.5 15L13.5 9" stroke="black" stroke-width="3"/>
</svg>
```

#### Redo
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Redo.svg`
- **ViewBox:** 36x38
- **Description:** Curved arrow pointing right (redo action)
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Drop Shadow:** Yes (filter applied)
- **Usage:** Redo action, restore changes
- **Display Size:** 36px
- **Note:** Contains shadow filter effect

---

### State Icons
Icons indicating various application states and modes.

#### Contact
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Contact.svg`
- **ViewBox:** 36x36
- **Description:** Multiple rectangular layers with connection lines
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Contact/layer indication, grouped layers
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M7.5 10.125H21.5" stroke="black" stroke-width="3"/>
  <path d="M7.5 25.875H21.5" stroke="black" stroke-width="3"/>
  <path d="M9.25 25.875V10.125H19.75V25.875H9.25Z" stroke="black" stroke-width="3"/>
  <path d="M23.25 11.875H27.625V18.875L25.875 20.625V24.125H23.25" stroke="black" stroke-width="3"/>
</svg>
```

#### Auto
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/auto.svg`
- **ViewBox:** 36x36
- **Description:** Diamond with "auto" text indicator
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Automatic mode indication
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M21.4981 9.49816L18 6L14.5019 9.49816H9.49816V14.5019L6 18L9.49816 21.4981V26.5019H14.5019L18 30L21.4981 26.5019H26.5019V21.4981L30 18L26.5019 14.5019V9.49816H21.4981Z" stroke="black" stroke-width="3"/>
  <path d="M15.3327 19.41H20.6672M14 23L17.2725 14H18.7274L22 23" stroke="black" stroke-width="3"/>
</svg>
```

#### Auto Light
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/auto_light.svg`
- **ViewBox:** 36x36
- **Description:** Sun with auto-adjustment indicator
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Automatic light/brightness adjustment
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <g clip-path="url(#clip0_40_951)">
    <path d="M18.0002 24.7696C21.7388 24.7696 24.7695 21.7389 24.7695 18.0003C24.7695 14.2618 21.7388 11.2311 18.0002 11.2311C14.2617 11.2311 11.231 14.2618 11.231 18.0003C11.231 21.7389 14.2617 24.7696 18.0002 24.7696Z" stroke="black" stroke-width="3"/>
    <path d="M24.4106 20.18C23.7266 20.4125 22.9933 20.5386 22.2307 20.5386C18.4921 20.5386 15.4614 17.5079 15.4614 13.7694C15.4614 13.0067 15.5875 12.2735 15.8201 11.5895C13.151 12.4968 11.2307 15.0242 11.2307 18.0001C11.2307 21.7386 14.2614 24.7693 18 24.7693C20.9759 24.7693 23.5033 22.849 24.4106 20.18Z" stroke="black" stroke-width="3"/>
    <path d="M18 6V11.231" stroke="black" stroke-width="3"/>
    <path d="M26.4855 9.51465L22.7866 13.2135" stroke="black" stroke-width="3"/>
    <path d="M30 18H24.769" stroke="black" stroke-width="3"/>
    <path d="M22.7866 22.7865L26.4851 26.485" stroke="black" stroke-width="3"/>
    <path d="M18 24.7695V30" stroke="black" stroke-width="3"/>
    <path d="M13.2134 22.7865L9.51489 26.485" stroke="black" stroke-width="3"/>
    <path d="M11.2305 18H6" stroke="black" stroke-width="3"/>
    <path d="M9.51489 9.51465L13.2137 13.2135" stroke="black" stroke-width="3"/>
  </g>
</svg>
```

#### Auto CMYK
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/auto_cmyk.svg`
- **ViewBox:** 36x36
- **Description:** Auto icon with CMYK color indicator
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Automatic CMYK mode
- **Display Size:** 36px

#### Auto-Off
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/auto-off.svg`
- **ViewBox:** 36x36
- **Description:** Disabled/inactive auto mode indicator
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Auto mode is disabled
- **Display Size:** 36px

#### Auto-On
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/auto-on.svg`
- **ViewBox:** 36x36
- **Description:** Enabled/active auto mode indicator
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Auto mode is enabled
- **Display Size:** 36px

#### Active Linked
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/active_linked.svg`
- **ViewBox:** 36x36
- **Description:** Chain link in active/connected state
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Layers/properties are linked
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <g clip-path="url(#clip0_40_968)">
    <path d="M22.6666 13.3334L13.3333 22.6667" stroke="black" stroke-width="3"/>
    <path d="M15.6667 12.1667L22.0834 5.75L30.2501 13.9167L23.8334 20.3333" stroke="black" stroke-width="3"/>
    <path d="M20.3333 23.8333L13.9167 30.25L5.75 22.0833L12.1667 15.6666" stroke="black" stroke-width="3"/>
    <path d="M8.08325 8.08337L10.4166 10.4167" stroke="black" stroke-width="3"/>
    <path d="M13.9167 5.75V8.66667" stroke="black" stroke-width="3"/>
    <path d="M5.75 13.9166H8.66667" stroke="black" stroke-width="3"/>
    <path d="M27.9166 27.9167L25.5833 25.5834" stroke="black" stroke-width="3"/>
    <path d="M22.0833 30.25V27.3334" stroke="black" stroke-width="3"/>
    <path d="M30.2499 22.0834H27.3333" stroke="black" stroke-width="3"/>
  </g>
</svg>
```

#### Default Unlinked
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/default_unlinked.svg`
- **ViewBox:** 36x36
- **Description:** Broken chain link indicating unlinked state
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Layers/properties are unlinked
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <g clip-path="url(#clip0_40_938)">
    <path d="M22.6666 13.3334L13.3333 22.6667" stroke="black" stroke-width="3"/>
    <path d="M15.6667 12.1667L22.0834 5.75L30.2501 13.9167L23.8334 20.3333" stroke="black" stroke-width="3"/>
    <path d="M20.3333 23.8333L13.9167 30.25L5.75 22.0833L12.1667 15.6666" stroke="black" stroke-width="3"/>
  </g>
</svg>
```

#### Hold
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/hold.svg`
- **ViewBox:** 36x36
- **Description:** Hand/palm symbol indicating hold state
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Hold/preserve current state
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M27 17H9V29H27V17Z" stroke="black" stroke-width="3"/>
  <path d="M18 21V25" stroke="black" stroke-width="3"/>
  <path d="M13 17V12C13 9.23858 15.2386 7 18 7C20.7614 7 23 9.23858 23 12" stroke="black" stroke-width="3"/>
</svg>
```

---

### Lock State Icons

#### Locked
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/locked.svg`
- **ViewBox:** 36x36
- **Description:** Closed padlock indicating locked state
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Layer/property is locked and cannot be edited
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <rect x="10" y="16" width="16" height="12" stroke="black" stroke-width="3"/>
  <path d="M13 16V12C13 9.23858 15.2386 7 18 7C20.7614 7 23 9.23858 23 12V16" stroke="black" stroke-width="3"/>
  <circle cx="18" cy="22" r="1.5" fill="black"/>
</svg>
```

#### Unlocked
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/unlocked.svg`
- **ViewBox:** 36x36
- **Description:** Open padlock indicating unlocked state
- **Colors:** Black stroke
- **Stroke Width:** 3px
- **Usage:** Layer/property is unlocked and can be edited
- **Display Size:** 36px
- **SVG Code:**
```xml
<svg width="36" height="36" viewBox="0 0 36 36" fill="none">
  <path d="M27 17H9V29H27V17Z" stroke="black" stroke-width="3"/>
  <path d="M13 17V12C13 9.23858 15.2386 7 18 7C20.7614 7 23 9.23858 23 12V17" stroke="black" stroke-width="3"/>
  <path d="M18 21V25" stroke="black" stroke-width="3"/>
</svg>
```

---

### Branding Icons

#### Logo
- **File:** `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/Logo.svg`
- **ViewBox:** 122x70
- **Description:** Frontier Digi Processor brand logo with colored geometric shapes and text
- **Colors:** Multi-color (Red #BC1D2E, Green #3D765D, Purple #6355B5, Beige #EEEDF0)
- **Stroke Width:** N/A (filled paths and text)
- **Usage:** Application branding, header logo
- **Display Size:** 122x70px (use at original size)
- **Note:** Contains company name and styling elements

---

## Usage Guidelines

### General Recommendations

1. **Sizing:**
   - Navigation arrows: 24-36px
   - Control icons: 36px (standard)
   - Adjustment icons: 36px
   - Logo: Use at 122x70px or maintain aspect ratio

2. **Color Implementation:**
   - Primary icons use black stroke (stroke-width: 3px for 36px icons, 2px for 24px icons)
   - Maintain consistent stroke width within the same UI context
   - Consider dark/light mode theming for accessibility

3. **Spacing:**
   - Allow minimum 8px padding around icons in buttons
   - In toolbars, use 4-6px spacing between adjacent icons
   - Maintain consistent visual weight across icon sets

4. **Accessibility:**
   - Always provide descriptive alt text for icons
   - Use icons with accompanying labels when possible
   - Ensure sufficient contrast in dark/light modes
   - Consider colorblind-friendly alternatives for multi-colored icons

5. **Animation:**
   - Icons with transform/rotation concepts can use smooth transitions
   - Undo/Redo arrows work well with spin animations
   - Avoid animations that interfere with readability

### Implementation Notes

- All stroke-based icons use `stroke="black"` and can be easily recolored via CSS
- Filter effects (drop shadows) are included in Shrink and Redo icons for depth
- Clip paths are used for cleaner viewBox boundaries in complex icons
- ViewBox dimensions should be preserved to maintain aspect ratios

---

## Related Files

- Source Directory: `/Users/otis/Library/Mobile Documents/com~apple~CloudDocs/Frontier-digi-processor/`
- All SVG files use standard SVG 2.0 format
- Compatible with modern web browsers and design tools

---

## Version History

- **Created:** 2025-11-06
- **Total Icons:** 42
- **Status:** Complete inventory with technical specifications


# 4-Button Macropad

A compact 4-button macropad built around the Seeed XIAO microcontroller, designed for Hack Club.

<img width="665" height="313" alt="Screenshot_20260306_114448" src="https://github.com/user-attachments/assets/107bcbab-87aa-4499-9171-1bba361745d8" />
<img width="591" height="286" alt="Screenshot_20260306_114620" src="https://github.com/user-attachments/assets/1c0ca893-4961-4cb2-a10c-8eb63faf440c" />
<img width="909" height="574" alt="Screenshot_20260306_120633" src="https://github.com/user-attachments/assets/a8a75710-cf4b-437b-a06d-e7ad2d3e722e" />



## Overview

A minimal, hackable macropad that fits in the palm of your hand. Program it as a shortcuts board, game controller, stream deck, or whatever you can think of.

## Hardware

- **MCU:** Seeed Studio XIAO (SAMD21 / RP2040)
- **Switches:** Cherry MX pushbuttons (x4)
- **Form factor:** 94 × 49 mm

## How It Works

Each Cherry MX switch is wired to a GPIO pin on the XIAO. When pressed, the XIAO sends a keycode (or custom HID command) over USB. The XIAO's built-in USB support means no extra chips needed — just plug in and go.

## Getting Started

1. Flash your XIAO with CircuitPython or QMK
2. Wire each switch between a GPIO pin and GND
3. Edit the key mappings in `code.py` (CircuitPython) or `keymap.c` (QMK)
4. Plug in via USB — it shows up as a keyboard instantly

## Possible Uses

- Shortcuts for Photoshop, VS Code, or any app
- PTT / mute toggle for calls
- Volume / media controls
- Game macros

# USB-HID-Mouse-Using-Raspberry-Pi-Pico-2W
A custom USB HID mouse built using Raspberry Pi Pico 2W, joystick, and push buttons. Supports cursor movement, left/right clicks, Page Up/Page Down navigation, and works with PCs as well as Android devices through a USB OTG adapter.

## Features
- Cursor movement using joystick
- Left and right click
- Page Up / Page Down buttons
- USB HID plug-and-play
- Android OTG support

## Components
- Raspberry Pi Pico 2W
- Joystick Module
- Push Buttons
- Breadboard
- Jumper Wires
- Micro USB Cable


## Wiring
| Component   | Pico Pin |
| VRx         | GP26     |
| VRy         | GP27     |
| Left Click  | GP14     |
| Right Click | GP15     |
| Page Up     | GP16     |
| Page Down   | GP17     |

## Usage
1. Install CircuitPython.
2. Copy required libraries.
3. Upload `code.py`.
4. Connect to PC or Android using OTG.

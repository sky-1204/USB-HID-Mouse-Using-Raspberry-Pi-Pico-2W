import time
import board
import analogio
import digitalio
import usb_hid

from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

# Joystick
x_axis = analogio.AnalogIn(board.GP26)
y_axis = analogio.AnalogIn(board.GP27)

# Mouse buttons
left_btn = digitalio.DigitalInOut(board.GP14)
left_btn.direction = digitalio.Direction.INPUT
left_btn.pull = digitalio.Pull.UP

right_btn = digitalio.DigitalInOut(board.GP15)
right_btn.direction = digitalio.Direction.INPUT
right_btn.pull = digitalio.Pull.UP

# Page buttons
page_up_btn = digitalio.DigitalInOut(board.GP16)
page_up_btn.direction = digitalio.Direction.INPUT
page_up_btn.pull = digitalio.Pull.UP

page_down_btn = digitalio.DigitalInOut(board.GP17)
page_down_btn.direction = digitalio.Direction.INPUT
page_down_btn.pull = digitalio.Pull.UP

def read_axis(pin):
    return pin.value

while True:
    x = read_axis(x_axis)
    y = read_axis(y_axis)

    move_x = int((x - 32768) / 10000)
    move_y = int((y - 32768) / 10000)

    mouse.move(x=move_x, y=move_y)

    if not left_btn.value:
        mouse.click(Mouse.LEFT_BUTTON)

    if not right_btn.value:
        mouse.click(Mouse.RIGHT_BUTTON)

    # Page Up
    if not page_up_btn.value:
        keyboard.send(Keycode.PAGE_UP)
        time.sleep(0.2)

    # Page Down
    if not page_down_btn.value:
        keyboard.send(Keycode.PAGE_DOWN)
        time.sleep(0.2)

    time.sleep(0.01)
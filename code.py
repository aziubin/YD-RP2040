
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

layout.write("aJEF($g;A$qgkjJg9jW;GW;", delay=0.01)

# keyboard.send(Keycode.A)
# keyboard.send(Keycode.B)
# keyboard.send(Keycode.F)


#  Set up a pin (e.g., button press) to send key presses
# button = digitalio.DigitalInOut(board.GP0)
# button.direction = digitalio.Direction.INPUT
# button.pull = digitalio.Pull.DOWN

#  Continuously check for button press and send a key
# while True:
#    if button.value:
#        keyboard.send(Keycode.A)

from time import sleep

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)


def main():
    press_and_release()
    while True:
        led.value = not led.value
        print("asdf")
        sleep(0.5)


def press_and_release():
    print("pressing key")
    kbd.press(Keycode.RIGHT_ARROW)
    sleep(0.5)
    kbd.release(Keycode.RIGHT_ARROW)


if __name__ == "__main__":
    main()

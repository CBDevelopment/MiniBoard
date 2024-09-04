
import neopixel
import machine


NUM_PIXELS = 512
PIXEL_GPIO = 22
BRIGHTNESS = 0.1


PIXELS = neopixel.NeoPixel(machine.Pin(PIXEL_GPIO), NUM_PIXELS)


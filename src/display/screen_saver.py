
from .lights import *
from .neopixel_setup import NUM_PIXELS


def snake():
    try:
        while True:
            for i in range(NUM_PIXELS):
                draw_pixel(i, (0, 250, 255))
                sleep(0.0001)
            for i in range(NUM_PIXELS):
                draw_pixel(i, (0, 0, 0))
                sleep(0.0001)
    except KeyboardInterrupt:
        clear_display()
        return

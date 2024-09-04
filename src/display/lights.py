
from .neopixel_setup import PIXELS, BRIGHTNESS
from time import sleep


def clear_display():
    print('Clearing display...')
    PIXELS.fill((0, 0, 0))
    PIXELS.write()
    sleep(0.01)  # Short delay to ensure the change is registered
    PIXELS.fill((0, 0, 0))
    PIXELS.write()


def draw_pixel(pixel_id, color, brightness=BRIGHTNESS):
    PIXELS[pixel_id] = tuple(int(brightness * c) for c in color)
    PIXELS.write()

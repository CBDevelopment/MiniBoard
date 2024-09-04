
from src.networking.connection import disconnect, connect
from src.display.lights import clear_display, draw_pixel
from src.display.screen_saver import snake

INTERNET = False

if __name__ == '__main__':

    if INTERNET:
        try:
            disconnect()
            ip = connect()
        except Exception as e:
            print(e)
            clear_display()
            raise e

    clear_display()
    snake()

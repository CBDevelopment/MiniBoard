import network
from time import sleep
from . import secrets

from src.display.lights import draw_pixel

NETWORK_NAME = secrets.NETWORK_NAME
NETWORK_PASSWORD = secrets.NETWORK_PASSWORD
WIFI_INDICATOR_LED_IDX = 7


def disconnect():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print('Disconnecting...')
        wlan.disconnect()
        wlan.active(False)


def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_NAME, NETWORK_PASSWORD)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        draw_pixel(WIFI_INDICATOR_LED_IDX, (255, 0, 0))
        sleep(0.5)
        draw_pixel(WIFI_INDICATOR_LED_IDX, (0, 0, 0))
        sleep(0.5)
    ip = wlan.ifconfig()[0]
    draw_pixel(WIFI_INDICATOR_LED_IDX, (0, 255, 255))
    print(f'Connected on {ip}')
    return ip

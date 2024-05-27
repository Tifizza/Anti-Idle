import win32api
import time
import pyautogui as pg
IDLE_TIME = 120


def get_idle_time():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def is_idle():
    return get_idle_time() > IDLE_TIME


while True:
    if is_idle():
        pg.typewrite(['ctrl'])
    time.sleep(IDLE_TIME-2)

import keyboard
import pyautogui
import globalVariables
import time
import multiThread


def turn_on_off():
    if globalVariables.start_loop:
        globalVariables.start_loop = False
    else:
        globalVariables.start_loop = True

        multiThread.initiate(loop)


def loop():
    while True:
        if globalVariables.start_loop:
            keyboard.press_and_release("e")

            pyautogui.mouseDown(button="left")

            pyautogui.mouseUp(button="left")

            time.sleep(0.00001)
        else:
            break

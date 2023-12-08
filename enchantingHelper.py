import keyboard
import pyautogui
import globalVariables
import time
import multiThread

tick = 0.2


def turn_on_off():
    if globalVariables.start_loop:
        globalVariables.start_loop = False
    else:
        globalVariables.start_loop = True

        multiThread.initiate(loop)


def loop():
    while True:
        if globalVariables.start_loop:
            key_sequence_1()

            key_sequence_1()

            key_sequence_2()
        else:
            break


def key_sequence_1():
    if globalVariables.start_loop:
        keyboard.press_and_release("s")

        time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("e")

        time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("d")

        time.sleep(tick)


def key_sequence_2():
    keyboard.press_and_release("s")

    time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("e")

        time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("r")

        time.sleep(tick)

    if globalVariables.start_loop:
        pyautogui.mouseDown(button="left")

        pyautogui.mouseUp(button="left")

        pyautogui.mouseDown(button="left")

        pyautogui.mouseUp(button="left")

        time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("d")

        time.sleep(tick)

    if globalVariables.start_loop:
        keyboard.press_and_release("d")

        time.sleep(tick)

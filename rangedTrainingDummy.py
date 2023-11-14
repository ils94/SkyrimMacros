import pyautogui
import globalVariables
import readFile
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

            readFile.read_text_file()

            pyautogui.mouseDown(button="left")

            if globalVariables.bow_drawing:

                time.sleep(globalVariables.bow_drawing)

            pyautogui.mouseUp(button="left")

            if globalVariables.bow_drawing:

                time.sleep(globalVariables.bow_drawing)
        else:
            break

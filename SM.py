import craftingHelper
import rangedTrainingDummy
import meleeTrainingDummy
import keyboard
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Skyrim Macro")

keyboard.register_hotkey("*", craftingHelper.turn_on_off)
keyboard.register_hotkey("-", rangedTrainingDummy.turn_on_off)
keyboard.register_hotkey("+", meleeTrainingDummy.turn_on_off)

print("""Skyrim Macro is up and running!

Press * to start the Crafting Macro.
Press - to start the Ranged Training Dummy Macro.
Press + to start the Melee Training Dummy Macro.

You can change your Bow Drawing time in the "bow_drawing.txt" file, default value is 1.5.
""")

while True:
    user_input = input("Type exit to close this program: ")

    if user_input == "exit":
        break

    time.sleep(0.1)

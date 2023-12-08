import craftingHelper
import enchantingHelper
import rangedTrainingDummy
import meleeTrainingDummy
import keyboard
import ctypes
import time

ctypes.windll.kernel32.SetConsoleTitleW("Skyrim Macro")

keyboard.register_hotkey("*", craftingHelper.turn_on_off)
keyboard.register_hotkey("-", enchantingHelper.turn_on_off)
keyboard.register_hotkey("+", rangedTrainingDummy.turn_on_off)
keyboard.register_hotkey(".", meleeTrainingDummy.turn_on_off)

print("""Skyrim Macro is up and running!

Press * to start the Crafting Helper.
Press - to start the Enchanting Helper.
Press + to start the Ranged Training Dummy Macro.
Press . to start the Melee Training Dummy Macro.

You can change your Bow Drawing time in the "bow_drawing.txt" file, default value is 1.5.
""")

while True:
    user_input = input("Type exit to close this program: ")

    if user_input == "exit":
        break

    time.sleep(0.5)

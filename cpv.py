from pynput.keyboard import Key, Controller
from time import sleep

Keyboard = Controller()

def macro():
    text = input("> ")
    print("Performing macro in 3 seconds...")
    sleep(3)
    Keyboard.type(text)
    print("Macro performed!")

while True:
    macro()

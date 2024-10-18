from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (10,20)
controlMouse()

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Yooooo")
controlKeyboard()
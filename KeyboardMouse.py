from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

def on_press(key):
 
    if key == keyboard.Key.ctrl_l:
        mouse.press(Button.left)  
        try:
            print("alphanumeric key {0} pressed".format(key.char))
        except AttributeError:
            print("Special key {0} pressed".format(key))

    if key == keyboard.Key.alt_l:
        mouse.press(Button.right)  
        try:
            print("alphanumeric key {0} pressed".format(key.char))
        except AttributeError:
            print("Special key {0} pressed".format(key))

    if key == keyboard.Key.up:
        mouse.move(0,-30)
        print(mouse.position)
    
    if key == keyboard.Key.down:
        mouse.move(0,30)
        print(mouse.position)
    
    if key == keyboard.Key.right:
        mouse.move(30,0)
        print(mouse.position)

    if key == keyboard.Key.left:
        mouse.move(-30,0)
        print(mouse.position)

def on_release(key):

    if key == keyboard.Key.ctrl_l:
            mouse.release(Button.left)
    if key == keyboard.Key.alt_l:
            mouse.release(Button.right)         
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


    


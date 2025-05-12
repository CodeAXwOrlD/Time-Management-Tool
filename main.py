import os
import time
import threading
import subprocess
from Notify_me import Alert
from Speak import speak
from offline_speak import Ospeak
from online_check import is_Online
from test import intro
import threading
from input_take import input_manage
from os import getcwd

def load_schedule(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

def check_schedule(file_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_schedule(file_path)
            
            if current_time in schedule:
                text = schedule[current_time]
                if is_Online():
                    t1 = threading.Thread(target=Alert, args=(text,))
                    t2 = threading.Thread(target=speak, args=(text,))
                else:
                    t1 = threading.Thread(target=Alert, args=(text,))
                    t2 = threading.Thread(target=Ospeak, args=(text,))
                
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)


intro("TMA - Tool")
if  is_Online():
    print("Welcome To the Time Management Assistant Tool")
    speak("Welcome To the Time Management Assistant Tool")
    print("@Credit:CodeAXwOrlD")
else:
    print("Welcome To the Time Management Assistant Tool")
    Ospeak("Welcome To the Time Management Assistant Tool")
    print("©️Credit: CodeAXwOrlD")

print("Welcome To the Time Management Assistant Tool")
print("Available Commands:")
print("1. show - to show the Schedule file")
print("2. tell me - try like 'tell me to sleep at 09:00pm'")
print("3. exit - to exit the application")

# Example usage:
file_path = os.path.join(getcwd(), 'schedule.txt')

def Modifier():
    while True:
        pass_key = input()
        if "show" in pass_key:
            subprocess.run(["xdg-open", file_path])
        elif pass_key.startswith("tell me"):
            input_manage(pass_key)
        elif pass_key == "exit":
            print("Exiting the application. Goodbye!")
            break
        else:
            if is_Online():
                speak("Invalid Command")
                print('''
                      ______ Available commands _____
                      1. show - to show the Schedule file
                      2. tell me - try like "tell me to sleep at 09:00pm"
                      3. exit - to exit the application
                      ''')
            else:
                Ospeak("Invalid Input")

t1 = threading.Thread(target=check_schedule,args=(file_path,))
t2 = threading.Thread(target=Modifier)
t1.start()
t2.start()
t1.join()

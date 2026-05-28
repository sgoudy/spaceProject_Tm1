"""@Authors: Charles, Jordan, Shelby, Robert, Jon
Date: 26 May
Purpose: To seize the best spaceships in all the lands
"""
from homebase import bases
from ships import table

import sys
import time

import sys
import time

def slow_progress_bar():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", 
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    # Change 0.1 to 0.5 for half a second per frame (5x slower)
    delay = 0.50 

    for item in animation:
        sys.stdout.write(f"\rLoading: {item}")
        sys.stdout.flush()
        time.sleep(delay)
    
    sys.stdout.write("\rLoading: Complete!      \n")

 


q1 = input("Who dare....what's the secret passphrase?"  )
if q1 == "Open Sesame" or q1 == "open sesame":
    print("Access granted. Welcome to the space game!")
    print("...Building your galactic empire...") 
    slow_progress_bar()  
    print("You have a mission...would you like to accept it? (yes/no)")
    mission = input()
    if mission.lower() == "yes":
        print("Great! Let's get started, commander! The clock will start ticking once you enter the Death Star. \
You have 10 minutes to complete your mission before the Death Star blows up. Good luck!")
    
        print("Would you like to enter the Death Star and start your mission? (yes/no)")
        q2 = input()
    if q2.lower() == "yes":
        print("Entering the Death Star... Good luck, commander!")
    else:
        print("Mission aborted. Maybe next time, commander.")
else:
    print("Too bad, so sad. Incorrect passphrase. Access denied. ")



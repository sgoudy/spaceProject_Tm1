"""This is the codebase that takes parameters from the user and uses them to create homebase, and 
capture spaceships for the space game.
"""
from homebase import hb
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
    print(table)
else:
    print("Too bad, so sad. Incorrect passphrase. Access denied. ")

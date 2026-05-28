"""@Authors: Charles, Jordan, Shelby, Robert, Jon
Date: 26 May
Purpose: To seize the best spaceships in all the lands
"""
# imports
from homebase import bases
from ships import table
from animation import slow_progress_bar, texttime
from missionClock import countdown

texttime("Welcome to the Space Game! \n")

# Script

prompt = "Who dare....what's the secret passphrase?"
texttime(prompt)
q1 = input()

if q1 == "Open Sesame" or q1 == "open sesame":
    prompt=("Access granted.\n...Building your galactic empire...\n")
    texttime(prompt)
    slow_progress_bar()  
    prompt1 = "\nYou are the commander of a space fleet. Your mission is to seize the best spaceships in all the lands and build your galactic empire. Are you ready to accept your mission? (yes/no)"
    texttime(prompt1)
    mission = input()

    if mission.lower() == "yes":
        prompt = "\nGreat! Let's get started, commander! \nThe clock will start ticking once you enter the Death Star. \nYou have 10 minutes to complete your mission before the Death Star blows up. Good luck!"
        texttime(prompt) 
        prompt1 = "\nWould you like to enter the Death Star and start your mission? (yes/no)"
        texttime(prompt1)
        q2 = input()
        
        if q2.lower() == "yes":
            prompt2="\nEntering the Death Star... Good luck, commander!\n The clock starts now!"
            texttime(prompt2)
            # countdown(600)  # Start the mission clock for 10 minutes
            #list the spaceships and their stats. Offer the user which ship they want to attack first. Remote the Death Star from the list of ships.
            prompt3 = "\nHere are the spaceships you can attack:\n"
            texttime(prompt3)   
            print(table)
        else:
            print("Mission aborted. Maybe next time, commander.")

    else:
        print("Mission aborted. Maybe next time, commander.")

else:
    print("Too bad, so sad. Incorrect passphrase. Access denied. ")



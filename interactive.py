"""This is the codebase that takes parameters from the user and uses them to create homebase, and 
capture spaceships for the space game.
"""
from homebase import hb
from ships import fleet

# Create a loop that prints "-" and "^" to the screen for 10 iterations to create a loading screen effect
# for i in range(100):
#     print("----------------" * (i + 1) + "^" * (100- i))


q1 = input("What's the secret passphrase?")
if q1 == "Open Sesame" or q1 == "open sesame":
    print("Access granted. Welcome to the space game!")
    print("...Building your galactic empire...") 
    print(fleet)
else:
    print("Access denied. Incorrect passphrase.")

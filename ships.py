"""Ships for the space game. This file contains the classes and functions related to 
spaceships that players can command in the game.
"""

# PrettyTable example
from prettytable import PrettyTable
from homebase import bases

shipNames = ("the Death Star", "Enterprise", "Eleanor", "Tardis", "Serenity")
shipCodenames = ("the Death Star", "Top Gun", "Andromeda", "Tesla", "Firefly")
shipDefenses = ("Shields", "Cloaking Device", "Energy Absorbers", "Deflector Shields", "Stealth Technology")
shipWeapons = ("Photon Torpedoes", "Laser Cannons", "Plasma Guns", "Railguns", "Missiles")
shipCrew = ("5", "1", "1", "1", "1")
shipFuel = ("1000 liters", "1500 liters", "500 liters", "750 liters", "600 liters")

class ship: 
    """A class for ships.
    Attributes:        
        name (str): The name of the spaceship.
        codename (str): The codename of the spaceship.
        distance (str): The distance of the spaceship from Earth.
        defenses (str): The defenses of the spaceship.
        weapons (str): The weapons of the spaceship.
        crew (str): The crew of the spaceship.
        fuel (str): The fuel of the spaceship.
    """
    def __init__(self, name, codename, location, distance, defenses, weapons, crew, fuel):    
        self.name = name
        self.codename = codename
        self.baseLocation = location
        self.baseDistance = distance
        self.defenses = defenses
        self.weapons = weapons
        self.crew = crew
        self.fuel = fuel

def buildShips():
    """Builds a list of ship objects using the attributes defined above.
    Returns:
        list: A list of ship objects.
    """
    ships = []
    for i in range(len(shipNames)):
        eachShip = ship(shipNames[i], shipCodenames[i], bases[i].location, bases[i].distance, shipDefenses[i], shipWeapons[i], shipCrew[i], shipFuel[i])
        ships.append(eachShip)
    return ships

fleet = buildShips()

table = PrettyTable()
# Set the top row of the table to the attributes of the ship class
table.field_names = list(ship.__init__.__code__.co_varnames[1:])  # Set the field names to the attributes of the ship class

for ship in fleet:
        if ship.name != "the Death Star":  # Exclude the Death Star from the table
            table.add_row([ship.name, ship.codename, ship.baseLocation, ship.baseDistance, ship.defenses, ship.weapons, ship.crew, ship.fuel])
        
# print(table)   
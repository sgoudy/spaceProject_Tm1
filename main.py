"""@Authors: Charles, Jordan, Shelby, Robert, Jon
Date: 26 May
Purpose: To seize the best spaceships in all the lands
"""
enemyTargetNames = ("Enterprise", "Eleanor", "Tardis", "Serenity")
enemyCodename = ("Top Gun", "Andromeda", "Tesla", "Firefly")
enemyLocation = ("Planet Vulcan", "Planet Vega", "Moon Io", "Moon Titan")

class enemyTarget: 
    """A class representing a homebase for spaceships.
    Attributes:        
        name (str): The name of the homebase.
        location (str): The location of the homebase.
        SOB (str): The state of being of the homebase.
    """
    def __init__(self, name, location, SOB):
        self.name = name
        self.location = location
        self.SOB = SOB


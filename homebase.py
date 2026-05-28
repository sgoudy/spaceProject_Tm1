"""Homebase module
"""
shipLocation = ("Planet Viltrum", 
                           "Planet Vulcan", 
                            "Planet Vega", 
                            "Moon Io", 
                            "Moon Titan")

shipDistance = ("0 light years", "1000000 light years", "2000000 light years", "500000 light years", "800000 light years")

class base:
    """Homebase class
    Attributes:
        name (str): The name of the homebase.
        type (str): The type of the homebase.
    """
    def __init__(self, location: str, distance: str):
        self.location = location
        self.distance = distance

bases = []
def buildBase(location, distance):
    """Builds a base object and adds it to the list of bases.
    Args:
        name (str): The name of the homebase.
        location (str): The location of the homebase.
        distance (str): The distance of the homebase from Earth.
    Returns:
        base: A base object.
    """
    for i in range(len(shipLocation)):
        newBase = base(shipLocation[i], shipDistance[i])    
        bases.append(newBase)
   

buildBase(shipLocation, shipDistance)
# print(bases)
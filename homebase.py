"""Homebase module
"""

class Homebase:
    """Homebase class
    Attributes:
        name (str): The name of the homebase.
    """
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Homebase(name={self.name}, location={self.location})"
    
hb = Homebase("Alpha Base", "Earth")
print(hb)
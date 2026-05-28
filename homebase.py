"""Homebase module
"""

class base:
    """Homebase class
    Attributes:
        name (str): The name of the homebase.
        type (str): The type of the homebase.
    """
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __str__(self):
        return f"Homebase(name={self.name}, type={self.type})"
    
hb = base("Alpha Base", "Earth")
# print(hb)
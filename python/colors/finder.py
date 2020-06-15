# Finder class from the `python.colors` module.

class Finder:
    def __init__(self):
        self.pyblue = 0x3474a5
        self.pyyellow = 0xffd947
        self.pycolors = [self.pyblue, self.pyyellow]
    
    def ispycolor(self, color):
        """Returns True if the given hex is one of the two Python colors.
        
        @param color: An hex code prefixed by 0x"""

        if color == self.pyblue:
            return True
        elif color == self.pyyellow:
            return True
        else:
            return False
    
    def getpycolor(self, colname):
        """Gets the hex code for a color name. It must be a color from Python. If you're looking for ALL colors, you might want to use `Finder.getcolor(colname)`
        
        @param colname: A Python color name ("blue" or "yellow")."""

        if colname.lower() == "blue":
            return "3474a5"
        elif colname.lower() == "yellow":
            return "ffd947"
        else:
            return "This only works using Python colors. You might want to use 'Finder.getcolor(colname)'"
    
    def getcolor(self, colname):
        """Gets the hex code for ANY basic color. Blue and yellow do not return the Python ones. If you want that you might want to use `Finder.getpycolor(colname)`
        
        @param colname: A basic color name."""

        if colname.lower() == "red":
            return "ff0000"
        elif colname.lower() == "yellow":
            return "ffff00"
        elif colname.lower() == "green":
            return "00ff00"
        elif colname.lower() == "turquoise":
            return "00ffff"
        elif colname.lower() == "blue":
            return "0000ff"

Finder = Finder()
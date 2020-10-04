# Finder class from the `python.colors` module.

class Finder:
    """The Finder class from the `python.colors` module.

    Available functions:\n
    `Finder.ispycolor(color)` - Returns a boolean from given hex code.\n
    `Finder.getpycolor(colname)` - Returns a hex code from given Python color name.\n
    `Finder.getcolor(colname)` - Returns a hex code from given color name.
    `Finder.colors` - Returns a list of colors"""

    pyblue = 0x3474a5
    pyyellow = 0xffd947
    pycolors = [pyblue, pyyellow]
    colors = ["red", "yellow", "green", "turquoise", "blue", "orange",
              "tomato", "dark orange", "coral", "vermilion", "gold", "chartreuse"]

    @classmethod
    def ispycolor(cls, color):
        """Returns True if the given hex is one of the two Python colors.

        @param color: An hex code prefixed by 0x"""

        return color in cls.pycolors

    @classmethod
    def getcolors(cls):
        """Returns all the colors of the class. No arguments are required."""
        return cls.colors

    @staticmethod
    def getpycolor(colname):
        """Gets the hex code for a color name. It must be a color from Python. If you're looking for ALL colors, you might want to use `Finder.getcolor(colname)`

        @param colname: A Python color name ("blue" or "yellow")."""

        if colname.lower() == "blue":
            return "3474a5"
        elif colname.lower() == "yellow":
            return "ffd947"
        else:
            return "This only works using Python colors. You might want to use 'Finder.getcolor(colname)'"

    @staticmethod
    def getcolor(colname):
        """Gets the hex code for ANY basic color. Blue and yellow do not return the Python ones. If you want that you might want to use `Finder.getpycolor(colname)`

        @param colname: A basic color name ("red", "yellow", "green", "turquoise" or "blue"). For a full list of color names, use `Finder.getcolors()`"""

        color_without_formatting = colname.replace(' ', '').lower()

        if color_without_formatting == "red":
            return "ff0000"
        elif color_without_formatting == "yellow":
            return "ffff00"
        elif color_without_formatting == "green":
            return "00ff00"
        elif color_without_formatting == "turquoise":
            return "00ffff"
        elif color_without_formatting == "blue":
            return "0000ff"
        elif color_without_formatting == "orange":
            return "ffa500"
        elif color_without_formatting == "tomato":
            return "ff6347"
        elif color_without_formatting == "darkorange":
            return "ff8c00"
        elif color_without_formatting == "coral":
            return "ff7f50"
        elif color_without_formatting == "vermilion":
            return "ff4500"
        elif color_without_formatting == "gold":
            return "ffd700"
        elif color_without_formatting == "chartreuse":
            return "7fff00"
        elif color_without_formatting == "indianred":
            return "cd5c5c"
        elif color_without_formatting == "firebrick":
            return "b22222"
        elif color_without_formatting == "crimson":
            return "dc143c"
        elif color_without_formatting == "deeppink":
            return "ff1493"

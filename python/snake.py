# The Snake class from the `python` module. Play with the Python!

from random import randint

class Snake:
    """The Snake class from the `python` module. Play with the Python!
    
    Available functions:\n
    `Snake.boop()` - boop!\n
    `Snake.play(activity)` - Play with the Python."""

    python = "https://wildcard.is-for.me/i/6spp.png"

    @staticmethod
    def boop():
        """Boop the snake's nose!
        
        Requested by Alexis#0097 on Discord ([Wumpus' Universe](https://discord.gg/wump))"""

        boop1 = "He liked it very much!"
        boop2 = "Oh no! He didn't like it and it bite you!"

        choose = randint(1, 2)
        
        if choose == 1:
            return f"You booped the Python's nose... {boop1}"
        if choose == 2:
            return f"You booped the Python's nose... {boop2}"
    
    @staticmethod
    def play(activity):
        """Play with the Python!
        
        @param activity: An activity ("sing", "code")."""

        if activity == "sing":
            return "You sang with the Python!"
        if activity == "code":
            return "You coded with the Python. He knows a lot more than you do!"
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
        boop2 = "Oh no! He didn't like it and he bit you in retaliation!"
        boop3 = "\"Don't touch me!\" it hissed!"
        boop4 = "He wants you to boop his head again!"
        boop5 = "The Python is sleeping now, come back tomorrow."
        boop6 = "Oops! The Python mistook your hand for food."
        boop7 = "The Python is hungry. Feed it first."
        boop8 = "The Python is bored. Take it to the rain forest for a while."

        choose = randint(1, 8)

        boop_message = "You booped the Python's nose..."

        if choose == 1:
            return f"{boop_message} {boop1}"
        if choose == 2:
            return f"{boop_message} {boop2}"
        if (choose == 3):
            return f"{boop_message} {boop3}"
        if (choose == 4):
            return f"{boop_message} {boop4}"
        if (choose == 5):
            return f"{boop_message} {boop5}"
        if (choose == 6):
            return f"{boop_message} {boop6}"
        if (choose == 7):
            return f"{boop_message} {boop7}"
        if (choose == 8):
            return f"{boop_message} {boop8}"

    @staticmethod
    def play(activity):
        """Play with the Python!

        @param activity: An activity ("sing", "code", "adventure")."""

        if activity == "sing":
            return "You sang with the Python!"
        if activity == "code":
            return "You coded with the Python. He knows a lot more than you do!"
        if (activity == "adventure"):
            return "You went onto a rainforest adventure with the Python. You met his family and you ventured into his habitat!"
        if (activity == "feed"):
            return "You fed the Python. He's very happy now!"

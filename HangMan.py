import random

Words = [
    "Amulet", "Asteroid", "Badger", "Basket", "Bicycle", "Blanket", "Blizzard", 
    "Bounce", "Breeze", "Bucket", "Button", "Cactus", "Camera", "Candle", 
    "Canyon", "Castle", "Chatter", "Cheese", "Clatter", "Coding", "Compass", 
    "Crystal", "Cushion", "Cyborg", "Cyclone", "Deceive", "Dragon", "Drift", 
    "Eclipse", "Feather", "Forest", "Freeze", "Galaxy", "Giggle", "Glacier", 
    "Glance", "Goblin", "Gossip", "Grumble", "Guitar", "Hammer", "Hangman", "Jacket", 
    "Juggle", "Jumble", "Keyhole", "Kingdom", "Kitchen", "Lantern", "Laser", 
    "Laughter", "Levitate", "Lizard", "Meadow", "Meteor", "Mirror", "Mutant", 
    "Newcomer", "Orchard", "Pancake", "Pathway", "Pebble", "Pencil", 
    "Playful", "Polishing", "Portal", "Potion", "Puzzle", "Quiver", "Robot", 
    "Rocket", "Runaway", "Scatter", "Scramble", "Shield", "Skater", "Sketch", 
    "Snooze", "Spaceship", "Spoon", "Sprint", "Stroll", "Summit", "Swamp", 
    "Thunder", "Tickle", "Toaster", "Treasure", "Trinket", "Tumble", 
    "Vanishing", "Volcano", "Voyage", "Wallet", "Waterfall", "Whisper", "Wildcard", 
    "Willow", "Window", "Wizard", "X-ray", "Xenon", "Xylophone", "Yacht", 
    "Yellow", "Young", "Zebra", "Zipper"
]

def Hangman():

    Word = random.choice(Words)
    Letters = len(Word)
    Line = []

    for i in range(Letters):
        Line.append("_")

    print(" ".join(Line))
    return Word, Line, Letters

Word, Line, Letters = Hangman()

print("Welcome to Hangman!")
guess_letter = input("Enter a Letter. ")

if guess_letter in Word:
    print()

for i in range(0,Letters):
    [] = guess_letter
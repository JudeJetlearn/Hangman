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
    "Rocket", "Runaway", "Scattetr", "Scramble", "Shield", "Skater", "Sketch", 
    "Snooze", "Spaceship", "Spoon", "Sprint", "Stroll", "Summit", "Swamp", 
    "Thunder", "Tickle", "Toaster", "Treasure", "Trinket", "Tumble", 
    "Vanishing", "Volcano", "Voyage", "Wallet", "Waterfall", "Whisper", "Wildcard", 
    "Willow", "Window", "Wizard", "X-ray", "Xenon", "Xylophone", "Yacht", 
    "Yellow", "Young", "Zebra", "Zipper"
]

print("Welcome to Hangman!")

def Hangman():

    Word = random.choice(Words).lower()
    Letters = len(Word)
    Line = []

    for i in range(Letters):
        Line.append("_")

    print(" ".join(Line))
    return Word, Line, Letters

Word, Line, Letters = Hangman()
Lives = Letters
WrongLetters = []

while True:

    print("Incorrect Letters: "+", ".join(WrongLetters))

    guess_letter = input("Enter a Letter. ").lower()

    if guess_letter not in Word:
        print("Incorrect Guess!")
        Lives = Lives - 1
        WrongLetters.append(guess_letter)
        print(f"You have {Lives} Lives left.")
    else:
        print("Correct Guess!")

    print()

    for i in range(0,Letters):
        if guess_letter == Word[i]:
            Line[i] = guess_letter

    print(" ".join(Line))

    if "_" not in Line:
        print(f"Congrats! You found the word in {Letters-Lives} Attempts!")
        break

    if Lives == 0:
        print(f"You have ran out of atempts! The word was: {Word}.")
        break

        
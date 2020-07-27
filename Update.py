# This is an outline for if I want to revamp the game with better coding pratcices in place

maxTries = 10

guessedInFull = False
word = "no word yet"
tries = 0

# Helper Functions

def choseWord():
    word = "chosen word"
    print ("Shh: I chose the word: " + word)

def drawGameBoard():
    print ("-- pretty game board --")

def askForGuess():
    print ("Hey Man, I'm asking for a guess!")
    return False

######### MAIN ##########
choseWord()

while guessedInFull == False and tries < maxTries:
    tries += 1
    drawGameBoard()
    guessedInFull = askForGuess()

if guessedInFull == True:
    print("Congratulation!")
else:
    print ("Better luck next time")
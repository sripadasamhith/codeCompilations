'''
(19 - JAN - 2018) manHang - Samhith Sripada.py
Version: 2.5
19 - JAN - 2018
'''

import turtle
import random
import sys
import re

while True:
    name = str(raw_input("Please enter your name: "))
    try:
        name = str(name)
        break
    except Exception:
        print "Please enter your name in letters please!"
        continue
        
print "Greetings, %s! Welcome to manHang!" % (name)
instructions = ("""Instructions: You have to select a difficulty level, this will be considered
when the computer chooses a word for you to guess.
You have to guess what the word is by guessing individual characters.
If you get a letter right, it will pop up, if not, a body part will be drawn.
If the entire body is drawn, then the game is over.
Good luck %s!""") % (name)

print instructions

wordToGuess = ""

userGuessWord = []

userGuessCharacter = ""

guessingCount = 0

# counts how many times user guessed incorrectly 

word = ""

positions = []

# scans the word being guessed to see WHERE the character is (character is guessed by user) based on position

windowHeight = 400
windowWidth = 300

turtle.reset()

turtle.screensize(windowHeight, windowWidth)

pen = turtle

pen.pensize(10)


    
def turtleStart():
    global pen
    
    windowHeight = 400
    windowWidth = 300

    turtle.reset()

    turtle.screensize(windowHeight, windowWidth)

    pen = turtle
    colours  = ["red","green","blue","orange","purple","pink","yellow"]
    colour = random.choice(colours)
    pen.pencolor(colour)
    pen.pensize(10)

    pen.up()
    pen.forward(150)
    pen.right(90)
    pen.forward(450)
    pen.right(90)
    pen.forward(150)
    pen.down()
    pen.right(180)
    pen.forward(300)
    pen.right(180)
    pen.forward(150)
    pen.right(90)
    pen.forward(625)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(100)

turtleStart()

# makes the stand when user enters credentials

def drawHead():
    pen.up()
    pen.right(90)
    pen.forward(20)
    pen.down()
    pen.circle(50)

def drawBody():
    pen.up()
    pen.left(90)
    pen.forward(100)
    pen.down()
    pen.forward(150)

def drawLeftArm():
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.left(90)
    pen.down()
    pen.left(55)
    pen.forward(100)

def drawRightArm():
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.down()
    pen.right(110)
    pen.forward(100)

def drawLeftFoot():
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.left(140)
    pen.forward(100)
    pen.right(15)
    pen.down()
    pen.forward(110)

def drawRightFoot():
    pen.up()
    pen.right(180)
    pen.forward(110)
    pen.right(75)
    pen.down()
    pen.forward(15)
    pen.right(70)
    pen.forward(110)

def startingPoint():
    global wordToGuess
    global userGuessWord
    global userGuessCharacter
    global guessingCount
    global word

    wordToGuess = ""

    userGuessWord = []

    userGuessCharacter = ""

    guessingCount = 0

    # counts how many times user guessed incorrectly 

    word = ""

    positions = []

    while True:
        userPreference = str(raw_input("Please choose a difficulty level you would like to play manHang in: easy (e), medium (m), hard (h): "))
        try:
            if userPreference == "e" or userPreference == "m" or userPreference == "h":
                userPreference = str(userPreference)
                break
            else:
                print "Please enter your difficulty in easy 'e', medium 'm' or hard 'h'"
                pass
        except Exception:
            "Please enter your difficulty in easy 'e', medium 'm' or hard 'h'"
            continue

    # user chooses a difficulty level
    # easy words list

    easyWordsFile = open('easyWordsList.txt', 'r')

    easyList = easyWordsFile.readlines()

    for line in easyList:
        easyWords = line.split()
        
    easyWordsList = [item.rstrip() for item in easyList]

    # medium words list

    mediumWordsFile = open('mediumWordsList.txt', 'r')

    mediumList = mediumWordsFile.readlines()

    for line in mediumList:
        mediumWords = line.split()
        
    mediumWordsList = [item.rstrip() for item in mediumList]

    # hard words list

    hardWordsFile = open('hardWordsList.txt', 'r')

    hardList = hardWordsFile.readlines()

    for line in hardList:
        hardWords = line.split()
        
    hardWordsList = [item.rstrip() for item in hardList]

    # gets list for words (easy, medium, hard), then splites lines and removes 
    # from each element in the list, called by new variable

    def loadDifficultyWords(wordsLevel):
        global wordToGuess
        wordToGuess = random.choice(wordsLevel)
        return wordToGuess

    if userPreference == "e":
        loadDifficultyWords(wordsLevel = easyWordsList)
    elif userPreference == "m":
        loadDifficultyWords(wordsLevel = mediumWordsList)
    else:
        loadDifficultyWords(wordsLevel = hardWordsList)

    word = wordToGuess
    wordToGuess = list(wordToGuess)

    # make word being guessed into a list 

    # print wordToGuess

    for letters in wordToGuess:
        userGuessWord.append("__")

    # creates "blanks" based on characters in the word being guessed

    print userGuessWord
            
def insertLetters():
    userGuessedWordCorrectly = False
        
    def runAgain():
        if userGuessedWordCorrectly == True:
            print "HOORAY!! You did it!!"
        else:
            print "Whoops!! You lost this round, the word was '%s' and you guess %s" % (word, "".join(userGuessWord))

        answer = str(raw_input("Would like to play another game of manHang? Click a button on the keyboard to play again, or type DONE to exit: "))
        if answer == "DONE":
            print "Thanks for playing manHang! Have a great day ahead!"
            sys.exit()
            # function above monitors to see if the user has guessed the word correctly &
            # gives user option to play again   
        else:
            pass
            turtleStart()
            startingPoint()
            insertLetters()
            runAgain()

    if "".join(userGuessWord) == word:
        userGuessedWordCorrectly = True
        runAgain()
    else:
        userGuessedWordCorrectly = False

        
    global userGuessWord
    global userGuessCharacter
    global positions

    while True:
        userGuessCharacter = str(raw_input("Please enter a character you think is in the word: "))
        try:
            userGuessCharacter == None
        except Exception:
            print "Please enter a valid letter"
            pass
        else:
            try:
                userGuessCharacter = str(userGuessCharacter)
                break
            except Exception:
                print "Please enter a valid letter"
                continue

    if userGuessCharacter in word:
        positions = positions = [letter.start() for letter in re.finditer(userGuessCharacter, word)]
        # print positions
        if len(positions) > 1:
            i = 0
            while i < len(positions):
                del userGuessWord[positions[i]]
                userGuessWord.insert(positions[i], userGuessCharacter)
                print userGuessWord
                i += 1
            insertLetters()

                # if the user guesses a letter that appears more than once in a word
                # the system will automatically insert both letters to their correct spots

        else:
            del userGuessWord[positions[0]]
            userGuessWord.insert(positions[0], userGuessCharacter)
            print userGuessWord
            insertLetters()
            runAgain()  
        # matching the right letter to its corressponding spot in the word
    elif userGuessCharacter not in word:
        
        global guessingCount
        guessingCount = guessingCount + 1
        # print guessingCount

        if guessingCount == 1:
            drawHead()
            print "Sorry that was a wrong letter, please try again!"
            insertLetters()
        elif guessingCount == 2:
            drawBody()
            print "Sorry that was a wrong letter, please try again!"
            insertLetters()
        elif guessingCount == 3:
            drawLeftArm()
            print "Sorry that was a wrong letter, please try again!"
            insertLetters()
        elif guessingCount == 4:
            drawRightArm()
            print "Sorry that was a wrong letter, please try again!"
            insertLetters()
            
        elif guessingCount == 5:
            drawLeftFoot()
            print "Sorry that was a wrong letter, please try again!"
            insertLetters()
        else:
            drawRightFoot()
            print "Sorry that was a wrong letter, please try again!"
            print "Sorry you lost this round!"
            runAgain()    

startingPoint()
insertLetters()






'''
Sources:
https://mail.python.org/pipermail/tutor/2010-February/074305.html
http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
https://www.hangmanwords.com/words
http://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
'''

import simplegui
import random

# helper function to start and restart the game
def new_game(whichstart):
    # initialize global variables used in your code here
    global which
    which = whichstart
    
    if which == 1:
        range100()
    elif which == 2:
        range1000()

        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret
    global which
    global i
    which = 1
    i = 7
    
    secret = random.randrange(0, 99)
    print "Time to guess a number less than 100!"
    print "You have %s guesses to go." % (i)


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret
    global i
    global which
    which = 2
    i = 10
    
    secret = random.randrange(0, 999)
    print "Time to guess a number less than 1000!"
    print "You have %s guesses to go." % (i)

    
def input_guess(guess):
    # main game logic goes here
    global i
    global which
    guess_int = int(guess)
    
    print "Your guess was " + guess + "."
    
    if guess_int > secret:
        i  -= 1
        print "The secret number is lower!"
        print "You have %s guesses left!" % (i)
    elif guess_int < secret:
        i  -= 1
        print "The secret number is higher!"
        print "You have %s guesses left!" % (i)
    elif guess_int == secret:
        print "You guessed the secret number!"
    
    if i == 0:
        print "You lose! Ready to play again?"
        print
        new_game(which)

        
# create frame
frame = simplegui.create_frame("Guess the number", 50, 250)
frame.add_input("Your guess", input_guess, 50)
frame.add_button("New Game", new_game, 50)
frame.add_button("Less than 100", range100, 50)
frame.add_button("Less than 1000", range1000, 50)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game(1)

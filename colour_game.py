import Tkinter
import random

# The list of possible colours in the game
possible_colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','White', 'Brown']

# The player's score
player_score=0

# The time left of the game
time_left=30

# Function that starts the game.
def startGame(event):

    # If at the beginning of the game, start the countdown
    if time_left == 30:
        countdown()
        
    # Get the next colour from the list of possible colours
    nextColour()

# Function that chooses and displays the next colour.
def nextColour():

    # Use the globally declared 'player_score' and 'time_left' variables
    global player_score
    global time_left

    # If there is still time left in the game make the input box active
    if time_left > 0:
        input_box.focus_set()

        # If the colour typed is equal to the colour of the text, increase the player's score
        if input_box.get().lower() == possible_colours[1].lower():
            player_score += 1

        # Clear the input box.
        input_box.delete(0, Tkinter.END)

        # Shuffle the list of colours.
        random.shuffle(possible_colours)

        # Change the colour to type, by changing the text and the colour of the text to a random colour value
        label.config(fg=str(possible_colours[1]), text=str(possible_colours[0]))
        
        # Update the player's score
        scoreLabel.config(text="Score: " + str(player_score))

# Countdown timer function. 
def countdown():

    # Use the globally declared 'time_left' variable
    global time_left

    # If there is still time left in the game
    if time_left > 0:
        time_left -= 1 # decrement the timer
        timeLabel.config(text="Time left: " + str(time_left)) # update the time left label
        timeLabel.after(1000, countdown) # run the function again after 1 second
    
# Create GUI window
root = Tkinter.Tk()

# Set the background of the window
root.configure(background='lightblue')

# Set the title of the window
root.title("Colour game")

# Set the window size.
root.geometry("800x500")

# Add an instructions label, describing what to do
game_title = Tkinter.Label(root, text=" The awesome colour game", fg="darkblue", font=('Arial 46 bold'))
game_title.pack()
game_title.configure(background='lightblue')

# Add an instructions label, describing what to do
instructions = Tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Calibri 24'))
instructions.pack()
instructions.configure(background='lightblue') 

# Add a score label for the player's score
scoreLabel = Tkinter.Label(root, text="Press enter to start", font=('Calibri 24 bold'))
scoreLabel.pack()
scoreLabel.configure(background='lightblue')

# Add a label displaying the time left 
timeLabel = Tkinter.Label(root, text="Time left: " + str(time_left), fg="red", font=('Calibri 20 bold'))
timeLabel.pack()
timeLabel.configure(background='lightblue') 

# Add a label that displays the colours.
label = Tkinter.Label(root, font=('Arial 60 bold'))
label.pack()
label.configure(background='lightblue')

# Add a text input box for typing in colours.
input_box = Tkinter.Entry(root)

# Call the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
input_box.pack()

# Set focus on the input box.
input_box.focus_set()

# Start the GUI
root.mainloop()




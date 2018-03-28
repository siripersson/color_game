
import Tkinter as tk
import random

# The list of possible colors in the game
possible_colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','White', 'Brown']

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
    nextColor()

# Function that chooses and displays the next colour.
def nextColor():

    # Use the globally declared 'player_score' and 'time_left' variables
    global player_score
    global time_left

    # If there is still time left in the game
    if time_left > 0:
        input_box.focus_set() # make the input box active

        # If the colour typed is equal to the colour of the text
        if input_box.get().lower() == possible_colors[1].lower():
            player_score += 1 # increase the player's score

        # Clear the input box.
        input_box.delete(0, tk.END)

        # Shuffle the list of colours.
        random.shuffle(possible_colors)

        # Change the colour to type, by changing the text and the colour of the text to a random colour value
        colorLabel.config(fg=str(possible_colors[1]), text=str(possible_colors[0]))
        
        # Update the player's score
        scoreLabel.config(text="Score: " + str(player_score))

# Countdown function. 
def countdown():

    # Use the globally declared 'time_left' variable
    global time_left

    # If there is still time left in the game
    if time_left > 0:
        time_left -= 1 # decrement the timer
        timeLabel.config(text="Time left: " + str(time_left)) # update the time left label
        timeLabel.after(1000, countdown) # run the function again after 1 second

    # If the game is over
    if time_left == 0:
        timeLabel.config(text="Game over! ", font=('Verdana 38 bold')) 
        scoreLabel.config(text="Your score: " + str(player_score), font=('Verdana 30 bold'))
        input_box.pack_forget() # remove input box
        colorLabel.pack_forget() #remove colourLabel
        
# Create GUI window
root = tk.Tk()
root.configure(background='lightblue') # set the background of the window
root.title("Color game") # set the title of the window
root.geometry("800x500") # set the window size.

# Add a game title
game_title = tk.Label(root, text=" The awesome color game", fg="darkblue", font=('Verdana 46 bold'))
game_title.pack()
game_title.configure(background='lightblue')

# Add an instructions label, describing what to do
instructionLabel = tk.Label(root, text="Type in the color of the words, and not the word text!", font=('Verdana 20'))
instructionLabel.pack()
instructionLabel.configure(background='lightblue') 

# Add a score label for the player's score
scoreLabel = tk.Label(root, text="Press enter to start", font=('Verdana 20 bold'))
scoreLabel.pack()
scoreLabel.configure(background='lightblue')

# Add a label displaying the time left 
timeLabel = tk.Label(root, text="Time left: " + str(time_left), fg="red", font=('Verdana 16 bold'))
timeLabel.pack()
timeLabel.configure(background='lightblue') 

# Add a label that displays the colours
colorLabel = tk.Label(root, font=('Verdana 60 bold'))
colorLabel.pack()
colorLabel.configure(background='lightblue')

# Add a text input box for typing in colours
entryVar = tk.StringVar(value='')
input_box = tk.Entry(root,textvariable=entryVar,font='Calibri 30')
input_box.pack()

# Call the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)

# Set focus on the input box
input_box.focus_set()

# Start the GUI
root.mainloop()





import Tkinter as tk
import random

possible_colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','White', 'Brown']
player_score=0
time_left=30

def startGame(event):
    if time_left == 30:
        countdown()

    nextColor() 

def nextColor():
    global player_score # use global variables
    global time_left

    if time_left > 0:
        input_box.focus_set() # make the input box active

        # If the colour typed is equal to the colour of the text
        if input_box.get().lower() == possible_colors[1].lower():
            player_score += 1 

        input_box.delete(0, tk.END) # clear input box
        random.shuffle(possible_colors) # shuffle the colors

        # Change the colour to type, by changing the text and the colour of the text to a random colour value
        colorLabel.config(fg=str(possible_colors[1]), text=str(possible_colors[0]))
        scoreLabel.config(text="Score: " + str(player_score)) # update the player's score

def countdown():
    global time_left # use global variable

    if time_left > 0:
        time_left -= 1 
        timeLabel.config(text="Time left: " + str(time_left))
        timeLabel.after(1000, countdown) # run the function again after 1 second

    if time_left == 0:
        timeLabel.config(text="Game over! ", font=('Verdana 38 bold')) 
        scoreLabel.config(text="Your score: " + str(player_score), font=('Verdana 30 bold'))
        input_box.pack_forget() # remove input box
        colorLabel.pack_forget() #remove colourLabel
        
# Create GUI window
gui = tk.Tk()
gui.configure(background='lightblue') # set the background of the window
gui.title("Color game")
gui.geometry("800x500") 

# Add a game title
game_title = tk.Label(gui, text="Color game", fg="darkblue", font=('Verdana 46 bold'))
game_title.pack()
game_title.configure(background='lightblue')

# Add an instructions label, describing what to do
instructionLabel = tk.Label(gui, text="Type in the color of the words, and not the word text!", font=('Verdana 20'))
instructionLabel.pack()
instructionLabel.configure(background='lightblue') 

# Add a score label for the player's score
scoreLabel = tk.Label(gui, text="Press enter to start", font=('Verdana 20 bold'))
scoreLabel.pack()
scoreLabel.configure(background='lightblue')

# Add a label displaying the time left 
timeLabel = tk.Label(gui, text="Time left: " + str(time_left), fg="red", font=('Verdana 16 bold'))
timeLabel.pack()
timeLabel.configure(background='lightblue') 

# Add a label that displays the colours
colorLabel = tk.Label(gui, font=('Verdana 60 bold'))
colorLabel.pack()
colorLabel.configure(background='lightblue')

# Add a text input box for typing in colours
input_box = tk.Entry(gui, textvariable=tk.StringVar(value=''), font='Calibri 30')
input_box.pack()

# Call the 'startGame' function when the enter key is pressed
gui.bind('<Return>', startGame)
input_box.focus_set() 
gui.mainloop() # start the GUI




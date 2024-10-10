from tkinter import *  #importing all functions, classes, and constants from tkinter
import random  #provides functions to generate random numbers and performs random operations

#this function handles the logic when a player clicks on a button. 
def next_turn(row, column):  #the paramenters represent the coordinates of the grid cell that was clicked
    global player  #ensures that we can modify the player variable inside this function

    # Check if clicked button is empty and ensures that there is no winner yet 
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player  #if both conditions are met then the text of the button is updated to the current players's symbol
        
        #after the player makes a move it checks to see if the current player has won the game by calling this function 
        if check_winner() is True:
            label.config(text=(player + " wins!")) #if they have won then it updates the label with msg saying the current player has won.
        elif empty_spaces() is False:  #if there is no winner, it checks if there are any remaining empty spaces on the board,
            label.config(text="Tie!")  #if not then it declares a tie.
        else:
            # Switching players, players is an array that contains two player names. 
            player = players[1] if player == players[0] else players[0] #it's currently player 1's turns and then switches to player two
            label.config(text=(player + " turn"))  #constucts a string that shows which player's turn it is. 

def check_winner():
    #this iterates over the rows and columns of a 3x3 grid 
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "": #checks if the text of all three buttons in row i is the same and makes sure that it's not empty
            return True                                                                   #and if all this is true then that player has won by creating a horizontal line
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "": #checks if the text of three buttons in column i is the same and makes sure that it's not empty
            return True                                                                   #and if all this is true then that player has won by creating a vertical line
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": #checks if text of all three buttons from top left corner, middle and bottom right corner are same and not empty
        return True                                                                   #and if this is true then the player has won by creating a diagonal line from top left to bottom right corner
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": #checks if the text of all three buttons from top right corner, middle and bottom left corner are same and not empty
        return True                                                                   #and if this is true then the player has won by creating a diagonal line from top right to bottom right corner

    return False  #if none of the above conditions are met then that means no one has won yet.

#this fucntion checks empty spaces left on the board to determine whether the game can continue or not
def empty_spaces():
    for row in buttons:  #loops through each row of the 3x3 grid
        for button in row:  #loops through each button in the current row
            if button['text'] == "":  #checks if the button's text is empty, meaning that particular cell is unoccupied
                return True  #if any button is empty then the function returns true, meaning the game hasn't finished yet.
    return False  #if none of the buttons are empty then the function returns false, meaning the game has finished

#this function resets the game board and starts a new game. 
def new_game():
    global player  #declaring player as a global variable
    player = random.choice(players)  #randomly selects one of the two players to start the new game
    label.config(text=player + " turn") #updates the label and displays a message showing which player's turn it is
    for row in range(3): #loops through each row of the 3x3 grid
        for column in range(3):  #loops through each column of the current row
            buttons[row][column]['text'] = ""  #clears the text for each button on the board by setting it to an empty string

#creating the main application window using tkinter
window = Tk()
window.title("Tic-Tac-Toe")  #giving the window a title 
players = ["x", "o"]  #defines the two players, "x" and "o"
player = random.choice(players)  #randomly selecting the player that will start the game 


buttons = [[0, 0, 0] for _ in range(3)]  #initializes a 3x3 button and each element is initially set to 0 but will be replaced with actual buttons 
label = Label(text=player + " turn", font=('consolas', 40)) #indicates the current player's turn and specifies the font and size of the text
label.pack(side="top") #placing the label at the top of the window using pack() 

reset = Button(text="Restart", font=("consolas", 20), command=new_game) #creating a button widget that will allow users to restart the game and associates the button with new_game function, which will reset the game 
reset.pack(side="top") #placing the label at the top of the window 

frame = Frame(window)  #creating a frame widget, which acts as a container to hold 3x3 grid of the buttons 
frame.pack() #packs the frame into the window using the pack() making it visible in the UI

#nested loops iterate over each row and column of the 3x3 grid to create the buttons 
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,    #frame: buttons are placed inside, text="" button text is initially empty, setting the font and size of the button text along with it's height and width
                                      command=lambda row=row, column=column: next_turn(row, column)) #setting up an event handler to be called when the button is clicked and the lambda functionn captures the current row and
                                                                                                     #column values so that the correct button is passed to next_turn
        buttons[row][column].grid(row=row, column=column) #places the button in the correct position on the grid using the grid(), specifying the row and columns 

window.mainloop() #starts tkinter event loop, waiting for user interactions and keeps the window open and it runs until the user closes the window

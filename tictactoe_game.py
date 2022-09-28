import random
from tkinter import *

def next_player(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            
            buttons[row][column]["text"] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text = (player[0]+" wins"))
            elif check_winner() == "Tie":
                label.config(text = ("Tie"))
        else:
            
            buttons[row][column]["text"] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            elif check_winner() is True:
                label.config(text = (player[1]+" wins"))
            elif check_winner() == "Tie":
                label.config(text = ("Tie"))


def check_winner():
    for row in range (3):
        if buttons[row][0]["text"] == buttons[row][2]["text"] != "":
            return True
    for column in range (3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    elif empty_space() is False:
        return "Tie"
    else:
        return False


def empty_space(): 
    spaces = 9
    for row in range(3):
        for column in range (3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else: 
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text = player+" turn" )
    for row in range(3):
        for column in range (3):
            buttons[row][column].config(text ="", bg = "yellow")

# initialize variables
window = Tk()
window.title("Tic Tac Toe Game ")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0,],
          [0,0,0,],
          [0,0,0,]]
label = Label(text=player + " turn", font=("consoles",40))
label.pack(side = "top")
reset_buttons = Button(text = "restart", font = ("consolas", 20), command = new_game)
reset_buttons.pack(side = "top")
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "",  bg = "yellow", font = ("consolas", 40), width = 5, height = 2, command= lambda row = row, column = column: next_player(row, column))
        buttons[row][column].grid(row = row, column = column)





window.mainloop()
import random
import tkinter as tk
import datetime


class Pexeso:

    def __init__(self, master):
        self.master = master
        self.width = self.master.dimm[0]
        self.height = self.master.dimm[1]
        self.cards = []
        self.imagesx = ["./img/image1.png", "./img/image2.png", "./img/image3.png", "./img/image4.png", "./img/image5.png", "./img/image6.png", "./img/image7.png", "./img/image8.png"]
        random.shuffle(self.imagesx)
        self.images = 2 * self.imagesx
        random.shuffle(self.images)
        self.game_board = []
        self.new_game()
        self.count = 0
        self.first_card = None
        self.second_card = None
        self.current_player = 1
        self.turns_player1 = 0
        self.turns_player2 = 0

    def new_game(self):
        self.cards.clear()
        self.current_player = 1
        self.turns_player1 = 0
        self.turns_player2 = 0
        self.master.clear_frame()
        hlp = self.width * self.height // 2
        random.shuffle(self.imagesx)
        self.images = 2 * self.imagesx[:hlp]
        random.shuffle(self.images)
        self.create_board()
        self.create_game_board()
        
        #set names of the players
        if self.master.entry_name1.get() != "":
            self.master.label_player1.configure(text=f"{self.master.entry_name1.get().upper()}:")
        self.master.label_player1_points.configure(text="0")
        if self.master.entry_name2.get() != "":
            self.master.label_player2.configure(text=f"{self.master.entry_name2.get().upper()}:")
        self.master.label_player2_points.configure(text="0")
        self.master.check_player(self.current_player)

    def create_board(self):
       
        x = 480//self.width
        y = 480//self.height
        for i in range(self.width * self.height):
            image = tk.PhotoImage(file="./img/blank.png")
            button = tk.Button(self.master.pexeso_frame, image=image, width=x, height=y, command=lambda i=i: self.reveal(i))
            button.image = image
            self.cards.append(button) 

    def reveal(self, index):
        button = self.cards[index]
        image = tk.PhotoImage(file=self.images[index])
        button.config(image=image, command=lambda: None)
        button.image = image
        if self.count == 0:
            self.first_card = index
            self.count = 1
        elif self.count == 1:
            self.second_card = index
            self.count = 2
            self.master.master.after(1000, self.check)
           
    def create_game_board(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cards[i * self.width + j].grid(row=i, column=j)
          
    # check if the cards are the same
    def check(self):
        if self.images[self.first_card] == self.images[self.second_card]:
            self.cards[self.first_card].config(state=tk.DISABLED)
            self.cards[self.second_card].config(state=tk.DISABLED)
            if self.current_player == 1:
                self.turns_player1 += 1
                self.master.label_player1_points.configure(text=f"{self.turns_player1}")
            else:
                self.turns_player2 += 1
                self.master.label_player2_points.configure(text=f"{self.turns_player2}")
            if self.is_game_over():
                self.write_to_file()
        else:
            image = tk.PhotoImage(file="./img/blank.png")
            self.cards[self.first_card].config(image=image, command=lambda i=self.first_card: self.reveal(i))
            self.cards[self.second_card].config(image=image, command=lambda i=self.second_card: self.reveal(i))
            self.cards[self.first_card].image = image
            self.cards[self.second_card].image = image
            self.current_player = 2 if self.current_player == 1 else 1
            self.master.check_player(self.current_player)
        self.count = 0
    
    def is_game_over(self):
        for info in self.cards:
            if info["state"] == tk.NORMAL:
                return False
        return True

    def write_to_file(self):
        now = datetime.datetime.now()
        date_to_file = now.strftime("%d. %m. %Y, %H:%M:%S")

        with open("score.txt", 'a') as file:
            file.write("---------------\n")
            file.write(f"{date_to_file}\n")
            file.write(f"{self.master.label_player1.cget('text')} = {self.master.label_player1_points.cget('text')}\n")
            file.write(f"{self.master.label_player2.cget('text')} = {self.master.label_player2_points.cget('text')}\n")

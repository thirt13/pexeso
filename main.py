import random
import tkinter as tk 
from tkinter import scrolledtext
import customtkinter
from pexeso import Pexeso

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


class MyWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Pexeso 4 you")
        self.master.geometry("700x550")
        self.master.resizable(False, False)
        self.master.iconbitmap("./img/blank.ico")
        self.main_font = ("Helvetica", 16, "bold")
        self.dimm = [4, 4]

        # frames 
        self.players_frame = customtkinter.CTkFrame(self.master,
                                                    height=60, 
                                                    fg_color="transparent"
                                                    )
        self.pexeso_frame = customtkinter.CTkFrame(self.master, 
                                                   width=500, 
                                                   height=500, 
                                                   fg_color="transparent"
                                                   )
      
        self.control_frame = customtkinter.CTkFrame(self.master, 
                                                    width=200, 
                                                    height=490,  
                                                    fg_color="transparent"
                                                    )
        self.players_frame.grid(row=0, column=0, sticky="nsew")
        self.pexeso_frame.grid(row=1, column=0, padx=10, pady=(6,0))
        self.control_frame.grid(row=1, column=1, sticky="ns")
       
        #player items
        self.label_player1 = customtkinter.CTkLabel(self.players_frame, 
                                                    text="Player 1: ", 
                                                    font=self.main_font
                                                    )
        self.label_player1_points = customtkinter.CTkLabel(self.players_frame, 
                                                           text=" 0", 
                                                           font=self.main_font
                                                           )
        self.label_player2 = customtkinter.CTkLabel(self.players_frame, 
                                                    text="Player 2: ", 
                                                    font=self.main_font
                                                    )
        self.label_player2_points = customtkinter.CTkLabel(self.players_frame, 
                                                           text=" 0", 
                                                           font=self.main_font
                                                           )
        self.label_player1.grid(row=0,column=0, padx=20)
        self.label_player1_points.grid(row=0,column=1, padx=(10,50))
        self.label_player2.grid(row=0,column=2)
        self.label_player2_points.grid(row=0,column=3, padx=10)

        #control items
        self.entry_name1 = customtkinter.CTkEntry(self.control_frame)
        self.entry_name2 = customtkinter.CTkEntry(self.control_frame)
        self.label_name1 = customtkinter.CTkLabel(self.control_frame, text="name player 1")
        self.label_name2 = customtkinter.CTkLabel(self.control_frame, text="name player 2")
        self.label_option = customtkinter.CTkLabel(self.control_frame, text="level")
        self.label_name1.grid(row=0, column=0)
        self.entry_name1.grid(row=1, column=0, pady=(0,10))
        self.label_name2.grid(row=2, column=0)
        self.entry_name2.grid(row=3, column=0, pady=(0,10))
        self.label_option.grid(row=4, column=0)

        self.first_option = customtkinter.CTkOptionMenu(self.control_frame, 
                                                        values=["2 x 2", "2 x 3", "3 x 2", "4 x 4"], 
                                                        font=self.main_font,  
                                                        command=self.choice_board
                                                        )
        self.first_option.grid(row=5,column=0, pady=(0, 10))
        self.first_option.set("4 x 4")

        self.button_new_game = customtkinter.CTkButton(self.control_frame, 
                                                       text="new game", 
                                                       font=self.main_font, 
                                                       command=self.new_game
                                                       )
        self.button_history = customtkinter.CTkButton(self.control_frame, 
                                                      text="history", 
                                                      font=self.main_font, 
                                                      command=self.show_history
                                                      )
        self.button_close = customtkinter.CTkButton(self.control_frame, 
                                                    text="close", 
                                                    font=self.main_font, 
                                                    command=self.close_window
                                                    )
        self.button_new_game.grid(row=6, column=0, padx=10, pady=(10,60))
        self.button_history.grid(row=7, column=0, padx=10, pady=10)
        self.button_close.grid(row=8, column=0, padx=10, pady=10)

    def close_window(self):
        self.master.destroy()
    
    def choice_board(self, choice):
        self.dimm.clear()
        self.dimm.append(int(choice[0]))
        self.dimm.append(int(choice[-1]))

    def new_game(self):
        Pexeso(self)

    def clear_frame(self):
        for widgets in self.pexeso_frame.winfo_children():
            widgets.destroy()
      
    def check_player(self, current_player):
        if current_player == 1:
            self.label_player1.configure(font=("Helvetica", 28, "bold"))
            self.label_player1_points.configure(font=("Helvetica", 28, "bold"))
            self.label_player2_points.configure(font=("Helvetica", 20))
            self.label_player2.configure(font=("Helvetica", 20))
        else:
            self.label_player2.configure(font=("Helvetica", 28, "bold"))
            self.label_player2_points.configure(font=("Helvetica", 28, "bold"))
            self.label_player1_points.configure(font=("Helvetica", 20))
            self.label_player1.configure(font=("Helvetica", 20))

    def show_history(self):
        with open("score.txt", "r") as file:
            lines = file.read()
        screen = tk.Tk()
        screen.title("history score")
        screen.geometry("260x280")
        text_area = scrolledtext.ScrolledText(screen, 
                                      wrap = tk.WORD,
                                      width=28,
                                      height=15
                                      )
        text_area.grid( column=0, pady = 10, padx = 10)
        text_area.insert(tk.INSERT, lines)
        text_area.configure(state ="disabled")

        screen.mainloop()

window = tk.Tk()
MyWindow(window)

window.mainloop()

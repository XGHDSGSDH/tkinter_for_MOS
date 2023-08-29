from dataloader import Dataloader
from judgement import Judgement
from tkinter import *
import tkinter.ttk
import os
from playsound import playsound


class MOS_window:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dl = Dataloader(dir=file_path)
        if not self.dl.load(file_pth="./config.txt"):
            self.dl.mess_up()
            self.dl.save(file_pth="./config.txt")
        self.button_back_color = "#D3E0F3"
        self.button_fg_color = "#395260"
        self.nowpos = 0
        self.draw_my_window()

    def draw_my_window(self):
        self.window = Tk()
        self.window.title("Turkish worker simulator")
        self.window.state("zoomed")
        self.window.resizable(width=False, height=False)
        #播放按钮
        self.play_sound_btn = Button(
            self.window,
            activeforeground="black",
            text="播放音频",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.play_sound_btn.grid(row=0, column=0)
        self.play_sound_btn.bind("<Button-1>", self.play_snd)

        s = "请评分"
        #看是否有分
        self.now_label=Label(self.window,text=s)
        self.now_label.grid(row=0, column=1)

        self.btn1 = Button(
            self.window,
            activeforeground="black",
            text="1",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn1.grid(row=1, column=0)
        self.btn1.bind("<Button-1>", self.score1)

        self.btn2 = Button(
            self.window,
            activeforeground="black",
            text="2",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn2.grid(row=1, column=1)
        self.btn2.bind("<Button-1>", self.score2)

        self.btn3 = Button(
            self.window,
            activeforeground="black",
            text="3",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn3.grid(row=1, column=2)
        self.btn3.bind("<Button-1>", self.score3)

        self.btn4 = Button(
            self.window,
            activeforeground="black",
            text="4",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn4.grid(row=1, column=3)
        self.btn4.bind("<Button-1>", self.score4)

        self.btn5 = Button(
            self.window,
            activeforeground="black",
            text="5",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn5.grid(row=1, column=4)
        self.btn5.bind("<Button-1>", self.score5)
        self.window.mainloop()

    def play_snd(self):
        playsound(os.path.join(self.file_path,self.dl[self.nowpos]))
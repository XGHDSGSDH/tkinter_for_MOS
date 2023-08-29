from dataloader import Dataloader
from judgement import Judgement
from tkinter import *
import tkinter.ttk
import os
from playsound import playsound


class MOS_window:
    def __init__(self, file_path):
        self.file_path = file_path
        self.judger = Judgement()
        self.judger.load(file_pth='./dic.txt')
        self.dl = Dataloader(dir=file_path)
        if not self.dl.load(file_pth="./config.txt"):
            self.dl.mess_up()
            self.dl.save(file_pth="./config.txt")
        self.button_back_color = "#D3E0F3"
        self.button_fg_color = "#395260"
        self.nowpos = len(self.judger)
        self.draw_my_window()

    def draw_my_window(self):
        self.window = Tk()
        self.window.title("Turkish worker simulator")
        self.window.state("zoomed")
        self.window.resizable(width=400, height=200)
        self.window.bind('<Key 1>',self.score1)
        self.window.bind('<Key 2>',self.score2)
        self.window.bind('<Key 3>',self.score3)
        self.window.bind('<Key 4>',self.score4)
        self.window.bind('<Key 5>',self.score5)
        self.window.bind('<Up>',self.last_audio)
        self.window.bind('<Left>',self.last_audio)
        self.window.bind('<Right>',self.next_audio)
        self.window.bind('<Down>',self.next_audio)

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

        self.label_flush()

        self.btn1 = Button(
            self.window,
            activeforeground="black",
            text="1",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn1.grid(row=1, column=3)
        self.btn1.bind("<Button-1>", self.score1)

        self.btn2 = Button(
            self.window,
            activeforeground="black",
            text="2",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn2.grid(row=1, column=4)
        self.btn2.bind("<Button-1>", self.score2)

        self.btn3 = Button(
            self.window,
            activeforeground="black",
            text="3",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn3.grid(row=1, column=5)
        self.btn3.bind("<Button-1>", self.score3)

        self.btn4 = Button(
            self.window,
            activeforeground="black",
            text="4",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn4.grid(row=1, column=6)
        self.btn4.bind("<Button-1>", self.score4)

        self.btn5 = Button(
            self.window,
            activeforeground="black",
            text="5",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.btn5.grid(row=1, column=7)
        self.btn5.bind("<Button-1>", self.score5)
        self.last_btn = Button(
            self.window,
            activeforeground="black",
            text="上一条",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.last_btn.grid(row=2, column=0)
        self.last_btn.bind("<Button-1>", self.last_audio)

        self.next_btn = Button(
            self.window,
            activeforeground="black",
            text="下一条",
            font=("Microsoft YaHei UI", 16),
            bg=self.button_back_color,
            fg=self.button_fg_color,
        )
        self.next_btn.grid(row=2, column=1)
        self.next_btn.bind("<Button-1>", self.next_audio)
        self.window.mainloop()
    
    
    def play_snd(self,event):
        playsound(os.path.join(self.file_path,self.dl[self.nowpos]))

    def score1(self,event):
        self.judger.change(key = self.dl[self.nowpos], value = 1)
        self.judger.save(file_pth='./dic.txt')
        self.label_flush()
    def score2(self,event):
        self.judger.change(key = self.dl[self.nowpos], value = 2)
        self.judger.save(file_pth='./dic.txt')
        self.label_flush()
    def score3(self,event):
        self.judger.change(key = self.dl[self.nowpos], value = 3)
        self.judger.save(file_pth='./dic.txt')
        self.label_flush()
    def score4(self,event):
        self.judger.change(key = self.dl[self.nowpos], value = 4)
        self.judger.save(file_pth='./dic.txt')
        self.label_flush()
    def score5(self,event):
        self.judger.change(key = self.dl[self.nowpos], value = 5)
        self.judger.save(file_pth='./dic.txt')
        self.label_flush()
    def last_audio(self,event):
        if self.nowpos!=0:
            self.nowpos-=1
        self.label_flush()
        

    def next_audio(self,event):
        if self.nowpos!=len(self.dl):
            self.nowpos+=1
        else :
            self.end = Label(self.window,text="全都评测完了,欢迎下次再来qwq")
            self.end.grid(row=0,column=2)
        self.label_flush()
    
    def label_flush(self):
        self.now_label.grid_forget()
        s = "目前是第"+str(self.nowpos+1)+"条语音请评分"
        if self.judger[self.dl[self.nowpos]]:
            s+=" 目前分数是"+str(self.judger[self.dl[self.nowpos]])
        self.now_label=Label(self.window,text=s)
        self.now_label.grid(row=0, column=1)
        

    
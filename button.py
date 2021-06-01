from tkinter import *
from tkinter import ttk       

win = Tk()
win.geometry("300x400")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")

btn = Button(win, fg = "black", bg = "white", font = "italic")
btn.config(text = "Button")
btn.config(width = 12, height = 1)

btn.pack()

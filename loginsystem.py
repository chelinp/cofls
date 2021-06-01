from selenium import webdriver
import tkinter as tk

window = Tk()
window.title("Automatic login")
window.geometry("400x300")
window.option_add("*Font","맑음 20")

lab1 = Label(window)
lab1.config(text = "id or email", font = "italic 10")
lab1.pack()

ent1 = Entry(window)
ent1.config(show = "")
ent1.pack()

lab2 = Label(window)
lab2.config(text = "Password", font = "italic 10")
lab2.pack()

ent2 = Entry(window)
ent2.config(show = "*")
ent2.pack()

bkakao = Button(window, fg = "white", bg = "black")
bkakao.config(text = '로그인')
bkakao.config(font = '굴림 12')

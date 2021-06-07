from tkinter import *
from tkinter import ttk       
import tkinter as tk
import requests
from bs4 import BeautifulSoup as bs

win = tk.Tk()
win.geometry('300x400')
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")

def chang() :
    win = tk.Tk()
    win.geometry('300x400')
    win.title("자동 로그인")
    win.option_add("*Font", "맑음 10")

    menubar = tk.Menu(win)

    filemenu = tk.Menu(menubar)
    filemenu.add_command(label="아이디 추가하기", command = kakao)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Exit")

    menubar.add_cascade(label="File", menu=filemenu)

    win.config(menu=menubar)

def kakao() :                                                                                                           
    from selenium import webdriver
    import tkinter as tk

    window = Tk()
    window.title("DAUM-KAKAO LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","맑음 10")                                               

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
    bkakao.config(command = cha)
    
    bkakao.pack()

def idid() :
    from selenium import webdriver

    id = ent1.get()
    pw = ent2.get()

    
    url ="https://www.nate.com/"
    driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(5)
    xpath1="//*[@id='ID']"
    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
    driver.implicitly_wait(5)
    xpath2="//*[@id='PASSDM']"
    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
    driver.implicitly_wait(5)
    xpath3="//*[@id='btnLOGIN']"
    driver.find_element_by_xpath(xpath3).click()

    win.mainloop()

        
def cha() :
    win = tk.Tk()
    win.geometry('300x400')
    win.title("자동 로그인")
    win.option_add("*Font", "맑음 10")

    menubar = tk.Menu(win)

    filemenu = tk.Menu(menubar)
    filemenu.add_command(label="아이디 추가하기", command = kakao)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Exit")

    menubar.add_cascade(label="File", menu=filemenu)

    win.config(menu=menubar)

    bkao = Button(win, fg = "black", bg = "white", font = "italic")
    bkao.config(text = "아이디 1")
    bkao.config(width = 12, height = 1)
    bkao.config(command = idid)

    bkao.pack()

    win.mainloop()
    

bka = Button(win, fg = "gray", bg = "yellow", font = "italic")
bka.config(text = "Daum-kakao")
bka.config(width = 12, height = 1)
bka.config(command = chang)

bka.pack()

win.mainloop()
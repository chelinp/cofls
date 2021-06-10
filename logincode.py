﻿from tkinter import *
from tkinter import ttk       
import tkinter as tk
import requests
from bs4 import BeautifulSoup as bs


win = Tk()
win.geometry("300x400")
win = tk.Tk()
win.geometry('300x400')
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")                                                                  
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

def kakao():                                                                                                           
    menubar.add_cascade(label="File", menu=filemenu)

    win.config(menu=menubar)

def kakao() :                                                                                                           
    from selenium import webdriver
    import tkinter as tk

    window = Tk()
    window.title("DAUM-KAKAO LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","맑음 20")
    window.option_add("*Font","맑음 10")                                               

    lab1 = Label(window)
    lab1.config(text = "id or email", font = "italic 10")
@@ -35,282 +54,65 @@ def kakao():
    bkakao = Button(window, fg = "white", bg = "black")
    bkakao.config(text = '로그인')
    bkakao.config(font = '굴림 12')
    def kakaologin():
        url ="https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(5)
        xpath1="//input[@name='email']"
        driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
        driver.implicitly_wait(5)
        xpath2="//input[@name='password']"
        driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
        driver.implicitly_wait(5)
        xpath3="//button[@class='btn_g btn_confirm submit']"
        driver.find_element_by_xpath(xpath3).click()
        lab3.config(text = "[메시지] 로그인 성공!")

    bkakao.config(command=kakaologin)
    bkakao.pack()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()
    bkakao.config(command = cha)

def naver():                                                                                                           
    from selenium import webdriver

    window = Tk()
    window.title("NAVER LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")

    lab1 = Label(window)
    lab1.config(text = "id", font = "italic 10")
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

    bn = Button(window, fg = "white", bg = "black")
    bn.config(text = '로그인', font = "굴림 15")
    bn.config(font = '굴림 12')
    def naverlogin():
        url ="https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(5)
        xpath1="//*[@id='id']"
        driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
        driver.implicitly_wait(5)
        xpath2="//*[@id='pw']"
        driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
        driver.implicitly_wait(5)
        xpath3="//*[@id='log.login']"
        driver.find_element_by_xpath(xpath3).click()
        lab3.config(text = "[메시지] 로그인 성공!")

    bn.config(command=naverlogin)
    bn.pack()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()


def nate():                                                                                                           
    from selenium import webdriver

    window = Tk()
    window.title("NATE LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")

    lab1 = Label(window)
    lab1.config(text = "id", font = "italic 10")
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

    bbnate = Button(window, fg = "white", bg = "black")
    bbnate.config(text = '로그인', font = "굴림 12")
    def natelogin():
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
        lab3.config(text = "[메시지] 로그인 성공!")

    bbnate.config(command=natelogin)
    bbnate.pack()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()
    bkakao.pack()

def facebook():                                                                                                           
def idid() :
    from selenium import webdriver

    window = Tk()
    window.title("FACEBOOK LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")

    lab1 = Label(window)
    lab1.config(text = "phone number or email", font = "italic 10")
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

    bbface = Button(window, fg = "white", bg = "black")
    bbface.config(text = '로그인', font = "굴림 12")
    def facelogin():
        url ="https://www.nate.com/"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(5)
        xpath1="//*[@id='m_login_email']"
        driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
        driver.implicitly_wait(5)
        xpath2="//*[@id='m_login_password']"
        driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
        driver.implicitly_wait(5)
        xpath3="//*[@id='u_0_4_pU']"
        driver.find_element_by_xpath(xpath3).click()
        lab3.config(text = "[메시지] 로그인 성공!")

    bbface.config(command=facelogin)
    bbface.pack()
    id = ent1.get()
    pw = ent2.get()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

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

def insta():                                                                                                           
    from selenium import webdriver

    window = Tk()
    window.title("INSTAGRAM LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")
def cha() :
    win = tk.Tk()
    win.geometry('300x400')
    win.title("자동 로그인")
    win.option_add("*Font", "맑음 10")

    lab1 = Label(window)
    lab1.config(text = "phone number or name or email", font = "italic 10")
    lab1.pack()
    menubar = tk.Menu(win)

    ent1 = Entry(window)
    ent1.config(show = "")
    ent1.pack()
    filemenu = tk.Menu(menubar)
    filemenu.add_command(label="아이디 추가하기", command = kakao)
    filemenu.add_command(label="Save")
    filemenu.add_command(label="Exit")

    lab2 = Label(window)
    lab2.config(text = "Password", font = "italic 10")
    lab2.pack()

    ent2 = Entry(window)
    ent2.config(show = "*")
    ent2.pack()

    binsta = Button(window, fg = "white", bg = "black")
    binsta.config(text = '로그인', font = "굴림 12")
    def instalogin():
        url ="https://www.instagram.com/accounts/login/?source=auth_switcher"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(5)
        xpath1="//*[@id='loginForm']/div/div[1]/div/label/input"
        driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
        driver.implicitly_wait(5)
        xpath2="//*[@id='loginForm']/div/div[2]/div/label/input"
        driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
        driver.implicitly_wait(5)
        xpath3="//*[@id='loginForm']/div/div[3]/button"
        driver.find_element_by_xpath(xpath3).click()
        lab3.config(text = "[메시지] 로그인 성공!")

    binsta.config(command=instalogin)
    binsta.pack()
    menubar.add_cascade(label="File", menu=filemenu)

    lab3 = Label(window)
    lab3.pack()
    win.config(menu=menubar)

    window.mainloop()
    bkao = Button(win, fg = "black", bg = "white", font = "italic")
    bkao.config(text = "아이디 1")
    bkao.config(width = 12, height = 1)
    bkao.config(command = idid)

    lab3 = Label(window)
    lab3.pack()
    bkao.pack()

    window.mainloop()
    win.mainloop()


bka = Button(win, fg = "gray", bg = "yellow", font = "italic")
bka.config(text = "Daum-kakao")
bka.config(width = 12, height = 1)
bka.config(command = kakao)

bb = Button(win, fg = "white", bg = "green", font = "italic")
bb.config(text = "Naver")
bb.config(width = 12, height = 1)
bb.config(command = naver)

bnatt = Button(win, fg = "white", bg = "red", font = "italic")
bnatt.config(text = "Nate")
bnatt.config(width = 12, height = 1)
bnatt.config(command = nate)

bface = Button(win, fg = "white", bg = "blue", font = "italic")
bface.config(text = "Facebook")
bface.config(width = 12, height = 1)
bface.config(command = facebook)

bstar = Button(win, fg = "gray", bg = "pink", font = "italic")
bstar.config(text = "Instagram")
bstar.config(width = 12, height = 1)
bstar.config(command = insta)
bka.config(command = chang)

bka.pack()
bb.pack()
bnatt.pack()
bface.pack()
bstar.pack()

win.mainloop()

win.mainloop()

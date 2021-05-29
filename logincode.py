﻿from tkinter import *
from tkinter import ttk       
from matplotlib import font_manager, rc

plt.rcParams['font.family'] = 'NanumMyeongjo'

win = Tk()
win.geometry("500x500")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")                                                                  

def login():                                                                                                           
    from selenium import webdriver
    import tkinter as tk

    window = Tk()
    window.title("DAUM LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","맑음 20")

    lab1 = Label(window)
    lab1.config(text = "id/email", font = "italic")
    lab1.pack()

    ent1 = Entry(window)
    ent1.config(show = "")
    ent1.pack()

    lab2 = Label(window)
    lab2.config(text = "Password", font = "italic")
    lab2.pack()

    ent2 = Entry(window)
    ent2.config(show = "*")
    ent2.pack()

    btn = Button(window, fg = "white", bg = "black")
    btn.config(text = '로그인')
    def log ():
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

    btn.config(command=log)
    btn.pack()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()
    
def lo():                                                                                                           
    from selenium import webdriver
        
    window = Tk()
    window.title("NAVER LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")

    lab1 = Label(window)
    lab1.config(text = "id", font = "italic")
    lab1.pack()

    ent1 = Entry(window)
    ent1.config(show = "")
    ent1.pack()

    lab2 = Label(window)
    lab2.config(text = "Password", font = "italic")
    lab2.pack()

    ent2 = Entry(window)
    ent2.config(show = "*")
    ent2.pack()

    bn = Button(window, fg = "white", bg = "black")
    bn.config(text = '로그인', font = "굴림 15")
    def loo():
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

    bn.config(command=loo)
    bn.pack()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

bt = Button(win, fg = "white", bg = "blue", font = "italic")
bt.config(text = "Daum-kakao")
bt.config(width = 15, height = 2)
bt.config(command = login)

bb = Button(win, fg = "white", bg = "green", font = "italic")
bb.config(text = "Naver")
bb.config(width = 15, height = 2)
bb.config(command = lo)

bt.pack()
bb.pack()

win.mainloop()


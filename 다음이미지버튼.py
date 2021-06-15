from tkinter import *
from tkinter import ttk       


win = Tk()
win.geometry("300x400")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")                                                                  

def kakao():                                                                                                           
    from selenium import webdriver
    import tkinter as tk

    window = Tk()
    window.title("DAUM-KAKAO LOGIN")
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

img = PhotoImage(file = "C:\사이트 사진\daum_logo.png")
img = img.subsample(8)
bka = Button(win, image=img)
bka.config(command = kakao)

bka.pack()

win.mainloop()

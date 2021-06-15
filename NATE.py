
from tkinter import *
import tkinter.font

from selenium import webdriver

 

win = Tk()

win.title("NATE LOGIN")

win.geometry("300x400")

win.option_add("*Font","맑음 10")

'''lab3 = Label(win)
lab3.config(text = "NATE",font="고딕 15", fg = "red", pady = "15")
lab3.pack()'''

titleFont=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
titleLabel = Label(win, text="NATE", font=titleFont, fg="red", pady="15").pack()





lab1 = Label(win)

lab1.config(text = "ID", font = "italic 10")

lab1.pack()

 

ent1 = Entry(win)

ent1.insert(0,"ID or @이하 모두 입력")

def clear(event):
    ent1.delete(0,len(ent1.get()))
    
ent1.bind("<Button-1>",clear)

ent1.config(show = "")

ent1.pack()

 

 

lab2 = Label(win)

lab2.config(text = "Password", font = "italic 10")

lab2.pack()

 

 

ent2 = Entry(win)

ent2.config(show = "*")

ent2.pack()

 

 

btn=Button(win, fg = "black", bg = "light gray")

btn.config(text = '로그인')
btn.config(font = "굴림 12")
btn.config(width = 10, height = 1)

def login ():

    url ="https://www.nate.com/"

    driver = webdriver.Chrome("C:\Temp\chromedriver.exe")

    driver.get(url)

    driver.implicitly_wait(5)

    xpath1="//input[@name='ID']"

    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())

    driver.implicitly_wait(5)

    xpath2="//input[@name='PASSDM']"

    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())

    driver.implicitly_wait(5)

    xpath3="//input[@class='icon_login']"

    driver.find_element_by_xpath(xpath3).click()

btn.config(command=login)

btn.pack()

 

 

 

win.mainloop()

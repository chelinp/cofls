from tkinter import *
from selenium import webdriver
 
win = Tk()
win.title("NATE Log-in")
win.geometry("400x300")
win.option_add("*Font","고딕 20")
 
lab1 = Label(win)
lab1.config(text = "ID")
lab1.pack()
 
ent1 = Entry(win)

ent1.insert(0,"ID or @이하 모두 입력")
def clear(event):
    ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>",clear)

ent1.config(show = "")

ent1.pack()
 
 
lab2 = Label(win)
lab2.config(text = "Password")
lab2.pack()
 
 
ent2 = Entry(win)
ent2.config(show = "*")
ent2.pack()
 
 
btn=Button(win)
btn.config(text = '로그인')
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

    lab3.config(text = "[메시지] 로그인 성공!")

btn.config(command=login)

btn.pack()
 
 
lab3 = Label(win)
lab3.pack()
 
win.mainloop()
 
 
lab3 = Label(win)
lab3.pack()
 
win.mainloop()

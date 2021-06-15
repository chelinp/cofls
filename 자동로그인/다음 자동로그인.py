from tkinter import *
from selenium import webdriver

win = Tk()
win.title("Daum Log-in")
win.geometry("400x300")
win.option_add("*Font","궁서 20")


lab1 = Label(win)
lab1.config(text = "다음 카카오 ID")
lab1.pack()

ent1 = Entry(win)
ent1.insert(0,"")
def clear(event):
    if ent1.get() == "anjfqhk678@naver.com":
        ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>", clear)
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
    url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F"
    driver = webdriver.Chrome("C:/크롬 드라이버/chromedriver.exe")
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
btn.config(command=login)
btn.pack()


lab3 = Label(win)
lab3.pack()

win.mainloop()


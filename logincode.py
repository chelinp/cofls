from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x400")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")
win.configure(bg= 'white')
win.resizable(False, False)

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
def facebook():                                                                                                           
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

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()
def insta():                                                                                                           
    from selenium import webdriver
        
    window = Tk()
    window.title("INSTAGRAM LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")

    lab1 = Label(window)
    lab1.config(text = "phone number or name or email", font = "italic 10")
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

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

img = PhotoImage(file = "C:\\Users\\USER\\cofls\\daum.png")
img = img.subsample(4)
bka = Button(win, image=img, width = 50, height = 50)
bka.config(command = kakao)

labk = Label(win)
labk.config(text = "DAUM", font = "italic 10", relief='ridge', bg='white',bd=0)
labk.pack(side = bottom)

img2 = PhotoImage(file = "C:\\Users\\USER\\cofls\\naver.png")
img2 = img2.subsample(8)
bb = Button(win, image=img2, width = 50, height = 50)
bb.config(command = naver)

img3 = PhotoImage(file = "C:\\Users\\USER\\cofls\\nate.png")
img3 = img3.subsample(3)
bnatt = Button(win, image=img3, width = 50, height = 50)
bnatt.config(command = nate)

img4 = PhotoImage(file = "C:\\Users\\USER\\cofls\\facebook.png")
img4 = img4.subsample(6)
bface = Button(win, image=img4, width = 50, height = 50)
bface.config(command = facebook)

img5 = PhotoImage(file = "C:\\Users\\USER\\cofls\\instagram.png")
img5 = img5.subsample(3)
bstar = Button(win, image=img5, width = 50, height = 50)
bstar.config(command = insta)

bka.pack(pady=4)
bb.pack(pady=4)
bnatt.pack(pady=4)
bface.pack(pady=4)
bstar.pack(pady=4)


win.mainloop()
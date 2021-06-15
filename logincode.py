from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x500")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")
win.iconbitmap('C:\\Users\\USER\\cofls\\icon.ico')
win.configure(bg= 'white')
win.resizable(False, False)

def kakao():
    from selenium import webdriver
    import tkinter as tk

    window = Tk()
    window.title("DAUM-KAKAO LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","맑음 20")
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')

    lab1 = Label(window, text = "id",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)
    
    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()

    lab2 = Label(window, text = "password",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    bkakao = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
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
    bkakao.pack(pady=6)

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
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')

    lab1 = Label(window, text = "id",
                 font = ("Malgun Gothic", "11", "bold"),
                 fg = "black").pack()

    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()
    
    lab1 = Label(window, text = "password",
                 font = ("Malgun Gothic", "11", "bold"),
                 fg = "black").pack()

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    bn = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
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
    bn.pack(pady=6)

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
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')

    lab1 = Label(window, text = "id",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)
    
    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()

    lab2 = Label(window, text = "password",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    bbnate = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
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
    bbnate.pack(pady=6)

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
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')
    
    lab1 = Label(window, text = "phone number or email",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)
    
    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()

    lab2 = Label(window, text = "password",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    bbface = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
    def facelogin():
        url ="https://ko-kr.facebook.com/login/web/"
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
    bbface.pack(pady=6)

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
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')

    lab1 = Label(window, text = "phone number or name or email",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)
    
    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()

    lab2 = Label(window, text = "password",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    binsta = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
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
    binsta.pack(pady=6)

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

def jnu():                                                                                                           
    from selenium import webdriver
        
    window = Tk()
    window.title("JNUCLASS LOGIN")
    window.geometry("400x300")
    window.option_add("*Font","italic 20")
    window.iconbitmap('C:\\Users\\USER\\cofls\\iconn.ico')

    lab1 = Label(window, text = "id",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)
    
    ent1 = Entry(window, show = "",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent1.pack()

    lab2 = Label(window, text = "password",
                 font = ("Malgun Gothic", "12", "bold"),
                 fg = "black").pack(pady=2)

    ent2 = Entry(window, show = "*",
                 font = ("Malgun Gothic", "13"),
                 fg = "black")
    ent2.pack()

    bjnu = Button(window, text = '로그인',
                font = ("한컴 고딕", "12", "bold"),
                fg = "white",
                bg = "black")
    def jnulogin():
        url ="https://jnuclass.jejunu.ac.kr/xn-sso/login.php?auto_login=&sso_only=&cvs_lgn=&return_url=https%3A%2F%2Fjnuclass.jejunu.ac.kr%2Fxn-sso%2Fgw-cb.php%3Ffrom%3D%26login_type%3Dstandalone%26return_url%3Dhttps%253A%252F%252Fjnuclass.jejunu.ac.kr%252Flogin%252Fcallback"
        driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        driver.get(url)
        driver.implicitly_wait(5)
        xpath1="//*[@id='login_user_id']"
        driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
        driver.implicitly_wait(5)
        xpath2="//*[@id='login_user_password']"
        driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
        driver.implicitly_wait(5)
        xpath3="//*[@id='form1']/div[4]"
        driver.find_element_by_xpath(xpath3).click()
        lab3.config(text = "[메시지] 로그인 성공!")

    bjnu.config(command=jnulogin)
    bjnu.pack(pady=6)

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()

    lab3 = Label(window)
    lab3.pack()

    window.mainloop()


lab1 = Label(win, text = "로그인할 사이트를",
             font = ("한컴 고딕 ", "12", "bold"),
             fg = "black",
             bg = "white").pack(pady=2)

lab2 = Label(win, text = "선택해주세요",
             font = ("한컴 고딕", "12", "bold"),
             fg = "black",
             bg = "white").pack(pady=2)

lab3 = Label(win, text = "↓",
             font = ("한컴 고딕", "12", "bold"),
             fg = "black",
             bg = "white").pack(pady=3)

img = PhotoImage(file = "C:\\Users\\USER\\cofls\\daum.png")
img = img.subsample(4)
bka = Button(win, image=img, width = 50, height = 50)
bka.config(command = kakao)

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

img6 = PhotoImage(file = "C:\\Users\\USER\\cofls\\jnu.png")
img6 = img6.subsample(4)
bjnu = Button(win, image=img6, width = 50, height = 50)
bjnu.config(command = jnu)

bka.pack(pady=4)
bb.pack(pady=4)
bnatt.pack(pady=4)
bface.pack(pady=4)
bstar.pack(pady=4)
bjnu.pack(pady=4)

win.mainloop()

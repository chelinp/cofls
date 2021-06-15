from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x500")
win.title("자동 로그인")
win.option_add("*Font", "맑음 10")
win.iconbitmap('C:\\Users\\CafeAlle\\Desktop\\git\\icon.ico')
win.configure(bg= 'white')
win.resizable(False, False)
  

def kakao():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b1.pack()
    b1.config(command = kakao)


def naver():                                                                                                           
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b2.pack()
    b2.config(command = naver)
        
def nate():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://www.nate.com/")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b3.pack()
    b3.config(command = nate)
    
def facebook():                                                                                                           
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://ko-kr.facebook.com/login/web/")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b4.pack()
    b4.config(command = nate)
  
def insta():                                                                                                           
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b4.pack()
    b4.config(command = nate)

def jnu():                                                                                                           
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = '여기에 아이디를 입력해주세요'
    PW = '여기에 비밀번호를 입력해주세요'

    browser = webdriver.Chrome('C:\\Users\\CafeAlle\\Desktop\\git\\chromedriver.exe')
    browser.get("https://jnuclass.jejunu.ac.kr/xn-sso/login.php?auto_login=&sso_only=&cvs_lgn=&return_url=https%3A%2F%2Fjnuclass.jejunu.ac.kr%2Fxn-sso%2Fgw-cb.php%3Ffrom%3D%26login_type%3Dstandalone%26return_url%3Dhttps%253A%252F%252Fjnuclass.jejunu.ac.kr%252Flogin%252Fcallback")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    print("버튼이 눌림")

    b5.pack()
    b5.config(command = jnu) 
    

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

img = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\daum.png")
img = img.subsample(4)
bka = Button(win, image=img, width = 50, height = 50)
bka.config(command = kakao)

img2 = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\naver.png")
img2 = img2.subsample(8)
bb = Button(win, image=img2, width = 50, height = 50)
bb.config(command = naver)

img3 = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\nate.png")
img3 = img3.subsample(3)
bnatt = Button(win, image=img3, width = 50, height = 50)
bnatt.config(command = nate)

img4 = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\facebook.png")
img4 = img4.subsample(6)
bface = Button(win, image=img4, width = 50, height = 50)
bface.config(command = facebook)

img5 = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\instagram.png")
img5 = img5.subsample(3)
bstar = Button(win, image=img5, width = 50, height = 50)
bstar.config(command = insta)

img6 = PhotoImage(file = "C:\\Users\\CafeAlle\\cofls\\jnu.png")
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

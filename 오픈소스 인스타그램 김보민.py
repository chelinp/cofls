#!/usr/bin/env python
# coding: utf-8

# In[72]:


from tkinter import *


# In[91]:


win = Tk()
win.geometry("500x500")
win.title("자동로그인")
win.option_add("*Font", "맑음 10")

def login():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = 'snow_onth'
    PW = 'vnfmfms12^^'

    browser = webdriver.Chrome('./chromedriver')
    browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)
    print("버튼이 눌림")

btn = Button(win)
btn.config(text = "인스타그램")
btn.config(width = 10, height = 5)
btn.config(command = login)

btn.pack()

win.mainloop()


# In[9]:


pip install selenium


# In[89]:


def login()
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    ID = 'snow_onth'
    PW = 'vnfmfms12^^'

    browser = webdriver.Chrome('./chromedriver')
    browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    time.sleep(2)

    login_id = browser.find_element_by_name('username')
    login_id.send_keys(ID)

    login_pw = browser.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)



# In[ ]:





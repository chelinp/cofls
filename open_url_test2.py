from selenium import webdriver

chrome_driver_path = "C:/Users/qjawn/Downloads/chromedriver_win32/chromedriver.exe"
facebook_url = "http://facebook.com"
facebook_id = "01056857486"
facebook_pw = "sswansswan1."

browser = webdriver.Chrome(chrome_driver_path)
browser.get(facebook_url) 


browser.execute_script(f"document.getElementsByName('id')[0].value='{facebook_id}'")
browser.execute_script(f"document.getElementsByName('pw')[0].value='{facebook_pw}'") 

browser.find_element_by_css_selector("#u_0_d_e8").click() 
from selenium import webdriver

brower = webdriver.Chrome(executable_path = 'C:/Users/qjawn/Downloads/chromedriver_win32/chromedriver.exe')
brower.get("http://facebook.com")

facebook_url = "http://facebook.com"
facebook_id = "01056857486"
facebook_pw = "sswansswan1."



input_id = browser.find_element_by_css_selector("#email")
input_pw = browser.find_element_by_css_selector("#pass")

input_id.send_keys(facebook_id)
input_pw.send_keys(facebook_pw)

browser.find_element_by_css_selector("#u_0_d_6n").click()
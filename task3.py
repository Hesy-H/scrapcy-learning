import time
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://mail.163.com/'
browser.get(url)
time.sleep(3)
# open the window
browser.maximize_window()
time.sleep(5)
# find the iframe
browser.switch_to.frame(0)
email = browser.find_element_by_name('email')
email.send_keys('13265923587@163.com')
password = browser.find_element_by_name('password')
password.send_keys('******')
login_em = browser.find_element_by_id('dologin')
login_em.click()

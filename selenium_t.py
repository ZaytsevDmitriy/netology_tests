from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yandex_ import login_, password_
import time

driver = webdriver.Chrome()
driver.get('https://passport.yandex.ru/auth/')
elem = driver.find_element_by_name('login')
elem.send_keys(login_)
elem.send_keys(Keys.RETURN)
elem_password = driver.find_element_by_name('passwd')
elem_password.send_keys(password_)
elem_password.send_keys(Keys.RETURN)

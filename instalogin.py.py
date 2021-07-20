import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#xbayram copyright

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)


username = "your username"
usernameInput = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
time.sleep(2)
usernameInput.send_keys(username)

password = "your password"
passwordInput = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
time.sleep(2)
passwordInput.send_keys(password)

sendForm = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")
sendForm.click()
time.sleep(2)

simdidegil = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
simdidegil.click()
simdidegil1 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
simdidegil1.click()



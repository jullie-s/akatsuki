from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import instagramchat

# open browser
browser = webdriver.Chrome(executable_path="C:\\Users\\shone\\Downloads\\chromedriver.exe")
browser.implicitly_wait(5)

# open instagram in browser
browser.get('https://www.instagram.com/')

# find where to input credentials
username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password")

# input credentials
username_input.send_keys("thevirtualpreservationbot2")
password_input.send_keys("hackHPC2022")
# click login
browser.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
sleep(5)
# by pass any other popups

browser.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/section/div/button").click()
sleep(5)

browser.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]").click()
sleep(5)

# Open Messages
browser.find_element(By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a").click()
sleep(5)

browser.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[1]/a/div").click()
sleep(5)





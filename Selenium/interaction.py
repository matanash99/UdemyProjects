from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Development/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_bar = driver.find_element(By.NAME, "fName")
first_name_bar.send_keys("Matan")
last_name_bar = driver.find_element(By.NAME, "lName")
last_name_bar.send_keys("Ashkenazi")
email_bar = driver.find_element(By.NAME, "email")
email_bar.send_keys("mataniwani1999@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR,"form button")
sign_up_button.click()

wait_input = input("Enter:")

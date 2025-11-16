from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Development/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4296887021&f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&keywords=python%20student%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&spellCorrectionEnabled=true")

time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')

sign_in_button.click()
email_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_input.send_keys("mataniwani1999@gmail.com")
password_input = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_input.send_keys("tainer1!")
sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in_button.click()
time.sleep(3)

easy_apply_button = driver.find_element(By.XPATH, '//*[@id="jobs-apply-button-id"]')
easy_apply_button.click()


phone_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4296887021-23057500068-phoneNumber-nationalNumber"]')
phone_input.send_keys("0548154767")


next_button = driver.find_element(By.XPATH, '//*[@id="ember351"]/span')
next_button.click()
time.sleep(1)
next_button.click()
chinese_level = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4296887021-23057500060-multipleChoice"]')
chinese_level.click()
selection = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4296887021-23057500060-multipleChoice"]/option[2]')
selection.click()
remote_yes_no = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/select')
remote_yes_no.click()
selection = driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4296887021-23057500084-multipleChoice"]/option[3]')
selection.click()
review_button = driver.find_element(By.XPATH, '//*[@id="ember376"]')
review_button.click()
submit_button = driver.find_element(By.XPATH, '//*[@id="ember393"]/span')
submit_button.click()
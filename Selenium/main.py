from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Development/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_time_tags = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name_tags = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

events_dict = {i:{"time":time.text, "name":name.text}
               for i, (time, name) in enumerate(zip(event_time_tags, event_name_tags))}

print(events_dict)


# driver.close()
driver.quit()

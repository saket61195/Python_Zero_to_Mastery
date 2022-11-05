from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

brave_path = '/usr/bin/brave-browser'
options = Options()
options.binary_location = brave_path
chromedriver_path = '/chromedriver'
services = Service(chromedriver_path)
browser = webdriver.Chrome(service=services, options=options)
browser.maximize_window()
browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
assert 'Selenium Easy Demo' in browser.title  # it will give true

show_message_button = browser.find_element(By.CLASS_NAME, "btn-default")
user_message = browser.find_element(By.ID, "user-message")
user_button2 = browser.find_element(By.CSS_SELECTOR, "#get-input > .btn")
# print(user_button2)
user_message.clear()
user_message.send_keys("Hello i am not robot")
show_message_button.click()
output_message = browser.find_element(By.ID, "display")
assert "Hello i am not robot" in output_message.text
browser.close()
# browser.quit()

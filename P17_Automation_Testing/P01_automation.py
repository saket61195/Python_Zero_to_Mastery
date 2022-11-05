# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.binary_location = brave_path
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# browser.maximize_window()
# browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

brave_path = '/usr/bin/brave-browser'
options = Options()
options.binary_location = brave_path
chromedriver_path = '/chromedriver'
services = Service(chromedriver_path)
browser = webdriver.Chrome(service=services,options=options)
# browser.maximize_window()
browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# print('Selenium Easy Demo' in browser.title)
# print('Python Easy Demo' in browser.title)
assert 'Selenium Easy Demo' in browser.title #it will give true 
button_text = browser.find_element(By.CLASS_NAME,"btn-default")
# print(button_text)
print(button_text.get_attribute('innerHTML'))
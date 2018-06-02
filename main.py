from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.implicitly_wait(10) #Setting a max ten second wait time
browser.get('http://www.fakemailgenerator.com')
browser.find_element_by_id("copy-button").click()
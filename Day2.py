## Find the single web eliment by using different locators name using find_element method

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()

# to leave the browser open
chrome_options.add_experimental_option("detach", True)

## try to login with the phone number on airbnb page
## this is a practice to find a single element using a single locator

## creating a class
## you will use a method called: find_element(By.locator_type)

class demofindbyname():
    def find_by_name(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME,"login-input").send_keys("6135564563")
        driver.maximize_window()
        
## create an object of a class with empty arhuments

name1 = demofindbyname()

## call a find_by_name method on this object "name1"

name1.find_by_name()

## the same you can use ID, Xpath, CSS_Selector, Link_text and Partial_link_text as well

## the documentation is here: https://selenium-python.readthedocs.io/locating-elements.html













## Return a list of web eliments by using different locators name using find_elements method


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
## you will user find_elements method, there is s at the end

class demofindelements():
    def find_many(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.yatra.com/holidays")
        list1 = driver.find_elements(By.TAG_NAME,"a") # there are total 275 <a> tags on the page
        print(len(list1)) # this will count and print the number of total <a> tags
        for i in list1:
            print(i.text, end= " ") # this will print all the associated text from the <a> tag
        driver.maximize_window()
        
## create an object of a class with empty arhuments

name1 = demofindelements()

## call a find_many method on this object "name1"

name1.find_many()

## the same you can use ID, Xpath, CSS_Selector, Link_text and Partial_link_text as well

## the documentation is here: https://selenium-python.readthedocs.io/locating-elements.html













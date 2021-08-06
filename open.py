import time
from selenium import webdriver
from pynput.keyboard import *
import ssfunction as ss


driver=webdriver.Chrome(r"C:\Users\harsh\Downloads\chromedriver_win32\chromedriver.exe")   #Location of webdriver
driver.get("https://www.google.com")               #Going to Url
driver.maximize_window()
search_bar = driver.find_element_by_name("q")      #Locating search bar
search_bar.clear()                                 #To clear search bar before inserting any value
search_bar.send_keys("wiki")          #Data to be inserted in search bar

#Pressing enter key
keyboard = Controller()
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(2)

ss.screenshot(driver)                              #Calling the screenshot function

driver.close()                                     #Closing the browser




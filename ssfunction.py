import time
from selenium import webdriver
from pynput.keyboard import *

def browser(driver):
    driver = webdriver.Chrome(r"C:\Users\harsh\Downloads\chromedriver_win32\chromedriver.exe")
    url = "https://accounts.google.com/signin/v2/identifie"
    driver.get(url)  # Going to Url
    driver.maximize_window()
    signin_user = driver.find_element_by_name("identifier")
    signin_user.clear()
    signin_user.send_keys("harshantil")
    kb = Controller()
    kb.press(Key.enter)
    kb.release(Key.enter)
    signin_pass = driver.find_element_by_name("password")
    signin_pass.clear()
    signin_pass.send_keys("12345678")

def screenshot(d):

    folder =r"C:\\Users\\harsh\\Desktop\\testing\\Screenshot\\"
    time_string = time.asctime().replace(":",".")
    file_name = folder + time_string + ".png"
    d.get_screenshot_as_file(file_name)



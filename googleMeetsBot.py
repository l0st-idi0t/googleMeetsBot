from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller


keyboard = Controller()


def pressIt(key):
    keyboard.press(key)
    keyboard.release(key)

def joinMeet(deLink):
    #download chromedriver.exe and put it into your program files (x86)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    #replace below with your own path to your chrome's user data and make sure you are signed into your school account on chrome
    options.add_argument("user-data-dir=C:\\Users\\Account3\\AppData\\Local\\Google\\Chrome\\User Data") 
    driver = webdriver.Chrome(PATH, options = options)
    driver.get(deLink)
    #adjust time below for however long it takes your browser to load
    time.sleep(5)
    for i in range(2):
        pressIt(Key.tab)

    with keyboard.pressed(Key.ctrl):
        pressIt('e')
        pressIt('d') 

    time.sleep(2)

    for i in range(6):
        pressIt(Key.tab)
    pressIt(Key.enter)
    time.sleep(10)
    for i in range(2):
        pressIt(Key.tab)
    pressIt(Key.enter)
    time.sleep(3)
    #comment out below if you don't want to say hi in chat
    keyboard.type("hi")
    time.sleep(1)
    pressIt(Key.enter)
    #adjust below for however long your classes are; 5400 seconds is an hour and a half
    time.sleep(5400)
    driver.quit()


while True:
    now = time.localtime()
    #adjust the times below and add more if you need
    if now.tm_hour == 8 and now.tm_min == 00:
        joinMeet('your meet link here')
    if now.tm_hour == 9 and now.tm_min == 45:
        joinMeet('your meet link here')
    if now.tm_hour == 12 and now.tm_min == 00:
        joinMeet('your meet link here')
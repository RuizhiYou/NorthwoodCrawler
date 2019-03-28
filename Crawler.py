import os
import requests
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 10
#os.environ['MOZ_HEADLESS'] = '1'

def send_message():
    requests.get("https://maker.ifttt.com/trigger/northwood/with/key/bar5hK44JlMubYdeHf7pbP")


def crawler_down_message():
    print("crawler is down")


def login(driver):
    try:
        search = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'login')))
    except TimeoutException:
        return
    search.send_keys("youruizh")
    driver.find_element_by_id("password").send_keys(os.environ['password'])
    # input("enter password")
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(5)
    cur_window = driver.current_window_handle
    driver.switch_to.frame(driver.find_element_by_id("duo_iframe"))
    try:
        css = ".stay-logged-in > label:nth-child(1) > input:nth-child(1)"
        remember = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        return
    remember.click()

    try:
        css = "div.row-label:nth-child(2) > button:nth-child(3)"
        remember = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    except TimeoutException:
        return
    remember.click()
    driver.switch_to.window(cur_window)

def start():
    urls = [
        "https://assignments.housing.umich.edu/studentweb/SelectRoom.asp?Function=7450&fld31590=49&fld31591=Unfurnished&fld31589=August+16",
        "https://assignments.housing.umich.edu/studentweb/SelectRoom.asp?Function=7450&fld31590=49&fld31591=Unfurnished&fld31589=August+1"
    ]
    profile = webdriver.FirefoxProfile("/home/lcsu/.mozilla/firefox/dv38o2et.default/")
    driver = webdriver.Firefox(profile)
    print("firefox has started")
    while True:
        for url in urls:
            driver.get(url)
            login(driver)

            try:
                search = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "btnSubmit")))
            except TimeoutException:
                crawler_down_message()
                return
            search.click()

            try:
                WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Error")))
            except TimeoutError:
                send_message()
                break
            time.sleep(10)
    crawler_down_message()



if __name__ == '__main__':
    start()

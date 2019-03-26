import requests
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

delay = 3


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
    # driver.find_element_by_id("password").send_keys("password")
    input("enter password")
    driver.find_element_by_id("loginSubmit").click()


def start():
    url = "https://assignments.housing.umich.edu/studentweb/SelectRoom.asp?Function=7450&Roommates=152579&fld31590=49&fld31591=Unfurnished&fld31589=August+1"
    profile = webdriver.FirefoxProfile("/Users/Danny/Library/Application Support/Firefox/Profiles/m933xts7.default/")
    driver = webdriver.Firefox(profile)
    while True:
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
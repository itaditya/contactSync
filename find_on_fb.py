from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import json
import time


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--driver", type=str, default="chrome",
                help="which driver to use")

args = vars(ap.parse_args())
choice = args["driver"]
driver = ""
if(choice == "firefox"):
    driver = webdriver.Firefox()
else:
    driver = webdriver.Chrome()
# driver.set_window_size(718, 726)
driver.get("https://m.facebook.com/")
with open('credentials.json') as credentials:
    credData = json.load(credentials)["fb"]
    emailElement = driver.find_element_by_name("email")
    emailElement.send_keys(credData["email"])
    passElement = driver.find_element_by_name("pass")
    passElement.send_keys(credData["password"])
    driver.find_element_by_name("login").click()
    contactsData = {}
    try:
        WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "._2pii a"))
        )
        driver.find_element(
            By.CSS_SELECTOR, "._2pii a").click()
        #For clicking on Not Now btn
        driver.find_element(
            By.CSS_SELECTOR, "._4g34:nth-child(5) a").click()
        #For clicking on Search btn
        searchElement = driver.find_element(By.CSS_SELECTOR, ".mSideSearch input")
        with open('contacts.json') as contacts:
            contactsData = json.load(contacts)
            print(len(contactsData))
            for (index,contact) in enumerate(contactsData):
                # num = "+905496777777"
                num = contact["phno"]
                searchElement.send_keys(num)
                time.sleep(2)
                if(driver.find_elements(By.CSS_SELECTOR, ".jx-result")):
                    userElement = driver.find_element(By.CSS_SELECTOR, ".jx-result a")
                    userData = json.loads(userElement.get_attribute("data-extra"))
                    print(userData["name"])
                    contactsData[index]["name"] = userData["name"]
                    contactsData[index]["fbUri"] = userData["uri"]
                    if(not contactsData[index]["img"]):
                        contactsData[index]["img"] = userData["photo"]
                searchElement.clear()
    finally:
        print("Quitting")
        driver.quit()
        with open("contacts.json", "w") as jsonFile:
            json.dump(contactsData, jsonFile)

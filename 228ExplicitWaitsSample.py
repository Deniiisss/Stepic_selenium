import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import def_math_x
import os
import pyperclip

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
if WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
):
    browser.find_element(By.ID,"book").click()
x=browser.find_element(By.CSS_SELECTOR,"#input_value").text
browser.find_element(By.ID,"answer").send_keys(def_math_x.calc(x))
browser.find_element(By.CSS_SELECTOR,"#solve").click()
pyperclip.copy(browser.switch_to.alert.text.split()[-1])
print(pyperclip.paste())
# browser.switch_to.alert.text.split()[-1]

# assert "successful" in message.text

# button2=WebDriverWait(browser,5).until(EC.element_to_be_clickable(By.ID,"verify"))
WebDriverWait.until(EC.text_to_be_present_in_element("",""))
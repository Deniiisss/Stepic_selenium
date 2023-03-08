import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium import webdriver
import win10toast
try:
    word=input("Введите слово для перевода: \n")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)
    # browser=webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('headless') )
    browser.implicitly_wait(5)
    browser.get("https://translate.google.com/?hl=ru")
    browser.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys(word)
    translate=browser.find_element(By.XPATH,"/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span")
    translate=translate.text
    print(translate)
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(f'Слово {word} переводиться как:', translate)
finally:
    browser.quit()
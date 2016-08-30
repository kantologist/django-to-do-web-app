from selenium import webdriver
import os

chromedriver = r'C:\Users\Oluwafemi\Downloads\chromedriver_win32\chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get('http://127.0.0.1:8000/')

assert 'Django' in browser.title

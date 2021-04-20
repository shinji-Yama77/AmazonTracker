from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

PATH = '/Users/shinjiy/Desktop/chromedriver'


def get_html(ask):
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.amazon.com/")

    driver.find_element_by_id("twotabsearchtextbox").send_keys(ask)

    driver.find_element_by_id("nav-search-submit-button").click()

    time.sleep(5)

    return driver.page_source

def main():

    ask = input("What do you want to search for on Amazon? ")

    html = get_html(ask)

    soup = BeautifulSoup(html, "lxml")

    items = soup.find_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})

    for item in items:
        print(item.h2.text)

        try:
            price = item.find('span', class_='a-price-whole').text
            print(price)
        except:
            price = None
            print(price)
        


if __name__ == '__main__':
    main()
    
    




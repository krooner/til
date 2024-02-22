from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import pickle
import tqdm
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--query', default=None, type=str)

args = parser.parse_args()

if __name__ == "__main__":
    if args.query == None:
        raise ValueError("Wrong query!")

    driver = webdriver.Chrome()

    driver.get("https://shopping.naver.com/home")

    element = driver.find_element(By.CLASS_NAME, "_searchInput_search_text_3CUDs")
    element.send_keys(args.query)
    element.send_keys(Keys.ENTER)

    product_divs = driver.find_element(By.CLASS_NAME, "basicList_list_basis__uNBZx")
    product_titles = driver.find_elements(By.XPATH, "//div[starts-with(@class, 'product_title')]")

    first_item_title = product_titles[0].find_element(By.TAG_NAME, 'a').get_attribute('title')

    print(first_item_title)

    driver.close()
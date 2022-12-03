from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
item = 'shoes'
prods = []

driver = webdriver.Chrome()
driver.get('https://www.myntra.com/')
search_bar = driver.find_element(By.CLASS_NAME, 'desktop-searchBar')
search_bar.send_keys(item)
driver.find_element(By.CLASS_NAME, 'desktop-submit').click()

pg = 1
while True:
    products = driver.find_elements(By.CLASS_NAME, 'product-base')
    for prod in products:
        if 'Sneakers' in prod.find_element(By.CLASS_NAME, 'product-product').get_attribute('innerHTML'):
            prods.append(prod.find_element(By.CLASS_NAME, 'product-brand').get_attribute('innerHTML'), prod.find_element(By.CLASS_NAME, 'product-product').get_attribute('innerHTML'), prod.find_element(By.CLASS_NAME, 'product-ratingsContainer').get_attribute('innerHTML'))
    if pg == 4:
        break
    else:
        driver.find_element(By.CLASS_NAME, 'pagination-next').click()
        pg += 1

f = open('MyntraData.csv','w')
w = csv.writer(f)
for product_data in prods:
    w.writerow(product_data)
f.close()
        

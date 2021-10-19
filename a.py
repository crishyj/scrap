
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from openpyxl import Workbook
from openpyxl import load_workbook
from os.path import expanduser
from os import path
import os
import csv
import urllib.request
import xlsxwriter
import xlrd
import string
from openpyxl import load_workbook
from csv import writer 
import logging
import threading
import time

driver = webdriver.Chrome()
url = "https://www.leboncoin.fr/equipement_auto/1961642965.htm"
driver.get(url)
for index in range(75):
    driver.set_window_position(-10000,0)
    first_items = driver.find_element_by_class_name('fap-results__list')
    items = first_items.find_elements_by_tag_name('li')
    for item in items:
        company_name = item.find_element_by_class_name('ui-text-t4').text    
        address = item.find_element_by_class_name('fap-agent-card__address').text
        phone_number = item.find_element_by_class_name('fap-agent-card__telephone-link').get_attribute('data-telephone-number')
        List = [company_name, address, phone_number]
        with open('new1.csv', 'a', encoding='utf-8-sig', newline='') as f_object: 
            writer_object = writer(f_object) 
            writer_object.writerow(List) 
            f_object.close() 
        time.sleep(1)

    driver.find_elements_by_class_name('ui-pagination__link')[1].click()
    


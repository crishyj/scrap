
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

def thread_function(start):
    driver = webdriver.Chrome()
    # driver.set_window_position(-10000,0)
    url = "https://www.zoopla.co.uk/find-agents/croydon-london-borough/?q=Croydon%2C%20London&radius=10"
    driver.get(url)
    check = driver.find_element_by_name('disclaimer')
    time.sleep(0.5)
    check.click()
    time.sleep(0.5)
    accept = driver.find_element_by_name('action')
    time.sleep(0.5)
    accept.click()
    time.sleep(0.5)
    end = int(start)+5000
    for i in range(start,end):   
        caseId = driver.find_elements_by_name('caseId')[0]
        caseId.clear()
        caseId.send_keys(casenumbers[i])
        time.sleep(0.5)
        getBtn = driver.find_elements_by_xpath('/html/body/div/form[2]/table/tbody/tr[3]/td[2]/input[1]')[0]
        getBtn.click()
        time.sleep(1)   
        page = driver.find_element_by_tag_name('html')
        List = [casenumbers[i], page.get_attribute('innerHTML')]
        with open('new1.csv', 'a') as f_object: 
            writer_object = writer(f_object) 
            writer_object.writerow(List) 
            f_object.close() 
        driver.back()
    driver.quit()
   

if __name__ == "__main__":
    invalidChars = set(string.punctuation.replace(".0", ""))
    casenumbers = []
    loc1 = ("1.xlsx")
    wb = xlrd.open_workbook(loc1)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        if any(char in invalidChars for char in str(sheet.cell_value(i, 0))):
            casenumbers.append(int(sheet.cell_value(i, 0)))
        else:
            casenumbers.append(str(sheet.cell_value(i, 0)))
    start = [1, 10001, 20001, 30001, 40001]
    threads = list()
    for index in range(5):
        t = threading.Thread(target=thread_function, args=(start[index],))
        threads.append(t)
        t.start()
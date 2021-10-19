
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
url = "https://appalachianflooring.com/product-category/flooring/?lang=en&offset=18"
driver.get(url)
for index in range(18):
    # driver.set_window_position(-10000,0)
    products = driver.find_element_by_class_name('products')
    items = products.find_elements_by_tag_name('li')
    for item in items:
        productLink = 
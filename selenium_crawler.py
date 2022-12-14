import csv
import argparse
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

parser = argparse.ArgumentParser()
parser.add_argument("--driver", type=str,
                    default='./chromedriver', help="Google Chrome driver path")
parser.add_argument("--url", type=str, default='http://127.0.0.1:8000', help='Website URL')
args = parser.parse_args()

chrome_options = Options()
driver = webdriver.Chrome(f'./{args.driver}', chrome_options=chrome_options)
driver.get(args.url)

data = []

while True:
    content = driver.find_element(by=By.TAG_NAME, value='tbody')
    student_records = content.find_elements(by=By.TAG_NAME, value='tr')

    for record in student_records:
        attributes = record.find_elements(by=By.TAG_NAME, value='td')[:-1]
        data.append([e.text for e in attributes])

    # go to next page
    next_button = driver.find_element(by=By.ID, value='next')
    try:
        next_button.click()
        # wait for data to load
        time.sleep(1)
    except selenium.common.exceptions.ElementNotInteractableException:
        break

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow(d)

driver.stop_client()
driver.close()
driver.quit()

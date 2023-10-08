import time
import uuid
import os
import cv2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup chrome driver
chrome_opt = Options()
chrome_opt.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_opt, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(2000, 1000)

whitelisted_countries = open('whitelisted').read().split("\n")

# Navigate to the url
while True:
    driver.get('https://randomstreetview.com/')

    elem = driver.find_element(by=By.ID, value="address")
    country = elem.text.split(', ')[-1]
    print(country)

    if country in whitelisted_countries:
        time.sleep(5)
        # Saving screenshot of the browser
        filename = f'{country}-{uuid.uuid4()}.png'
        driver.save_screenshot('tmp/' + filename)
        image = cv2.imread('tmp/' + filename)  # Read Input Image
        cv2.imwrite('images/' + filename, image[50:-50, 350:])
        os.remove('tmp/' + filename)
        break
    else:
        f = open('found', 'a')
        f.write(country + '\n')
        f.flush()
        f.close()

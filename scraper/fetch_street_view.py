import time
from PIL import Image 
import uuid
import os
import cv2


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# Setup chrome driver
chrome_opt = Options()
chrome_opt.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_opt, service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.set_window_size(1280, 720)

whitelisted_countries = open('whitelisted').read().split("\n")

# Navigate to the url
while True:
    driver.get('https://randomstreetview.com/')
    
    elem = driver.find_element(by=By.ID, value="address")
    print("element full: ", elem)
    country = elem.text.split(', ')[-1].strip()
    
    for id in ['cmpwrapper', 'map_canvas', 'address', 'controls', 'minimaximize', 'adnotice', 'smallad', 'share', 'intro']:
        elems = driver.find_elements(by=By.ID, value=id)
        for elem in elems:
            driver.execute_script('''
                    var element = arguments[0];
                    element.parentNode.removeChild(element)
                ''', elem)
        
    selectors = [
        '.gmnoprint',
        '.gm-style-cc',
        '.gmnoscreen',
        '.gmnoprint.gm-style-cc',
        '.intro_splash'
        
    ]
    # for cls in ['intro_splash']:
    for cls in selectors:
        elems = driver.find_elements(by=By.CSS_SELECTOR, value=cls)
        for elem in elems:
            driver.execute_script('''
                        var element = arguments[0];
                        element.parentNode.removeChild(element)
                    ''', elem)
    
    if country in whitelisted_countries:
        # Saving screenshot of the browser
        filename = f'{country}-{uuid.uuid4()}.png'
        driver.save_screenshot('tmp/' + filename)
        image = cv2.imread('tmp/' + filename)  # Read Input Image
        inverted = abs(255-image)
        cv2.imwrite('images/' + filename, inverted)
        os.remove('tmp/' + filename)
        break
    else:
        with open('found', 'a') as f:
            f.write(country + '\n')

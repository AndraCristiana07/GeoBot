from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import numpy as np
from requests import get
import xmltodict
import time, uuid, json, os

# # # Setup chrome driver
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # driver.set_window_size(2000, 1000)
# #
# #
# # # Navigate to the url
# # driver.get('https://neal.fun/wonders-of-street-view/')
# #
# #
# # import time, uuid
# # time.sleep(3)
# #
# # elem = driver.find_element(by=By.CLASS_NAME, value="info-location")
# # country = elem.text.split(', ')[1]
# #
# # # Saving screenshot of the browser
# # driver.save_screenshot(f"{uuid.uuid4()}.png")
# #
# # # Close the driver
# # driver.quit()
#


option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

# Setup chrome driver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=option)
driver.set_window_size(2000, 1000)


# Navigate to the url
with open('out', mode='a') as out:
    country_names = set()
    for i in range(1000):
        driver.get('https://randomstreetview.com/')

        time.sleep(5)

        elem = driver.find_element(by=By.ID, value="address")
        country = elem.text.split(', ')[-1]
        country_names.add(country)
        # Saving screenshot of the browser
        driver.save_screenshot(f"{country}-{uuid.uuid4()}.png")

    for country in country_names:
        out.write(country + "\n")
#
#
#
#
# # Close the driver
# driver.quit()
#
#
# #
# # # Setup chrome driver
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# # driver.set_window_size(1000, 800)
# #
#
# #
# # # Navigate to the url
# # for i in range(1000):
# #
# #     coords = []
# #     while not coords:
# #         response = get('https://api.3geonames.org/?randomland=yes')
# #         data_dict = xmltodict.parse(response.text)
# #         if data_dict.get('geodata'):
# #             if data_dict['geodata'].get('nearest'):
# #                 if data_dict['geodata']['nearest']['latt']:
# #                     coords = [float(data_dict['geodata']['nearest']['latt']), float(data_dict['geodata']['nearest']['longt'])]
# #
# #
# # #     driver.get(f'https://www.google.com/maps/@?api=1&map_action=pano&viewpoint=68.62713%2C58.15545&heading=-45&pitch=0&fov=80')
# # #     driver.get(f'http://maps.google.com/maps?q=&layer=c&cbll={coords[0]},{coords[1]}')
# # #     driver.get(f'http://maps.google.com/maps?q={coords[0]},{coords[1]}')
# # #     # time.sleep(3000)
# # #
# # #     buttons = driver.find_elements(by=By.TAG_NAME, value='button')
# # #     print(len(buttons))
# # #     print(buttons)
# # #     buttons[1].click()
# #     print(f'http://maps.google.com/maps?q={coords[0]},{coords[1]}',data_dict)
# #     # time.sleep(10)
# # # Saving screenshot of the browser
# # # driver.save_screenshot(f"{uuid.uuid4()}.png")
# #
# # # Close the driver
# # driver.quit()


""" Some utility functions created. """

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def filter_by_brands(base_url):
    """ For a base url returns all the hrefs of brand filters in a certain category."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(base_url)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "brand-list-container"))
        )
        brands = element.find_elements_by_xpath('div[2]//a')
        urls = [b.get_attribute('href') for b in brands]
        return urls
    finally:
        driver.quit()

if __name__ == "__main__":
    url_list = filter_by_brands("https://www.trendyol.com/kadin?siralama=13&qs=navigation")
    print("The number of links: " + str(len(url_list)))

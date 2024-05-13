from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait

import selectors

base_url = 'https://help.lyft.com'
cases= {
        'query': 'Pick up, renew, and return your Express Drive rental',
        'expected-url': 'https://help.lyft.com/hc/en-us/all/articles/360001562167-Rental-car-pickups-renewals-and-returns',
        'bullet': 'Renew',
        'expected-text': 'Renew'
        }, {
        'query': 'Pick up, renew, and return your Express Drive rental',
        'expected-url': 'https://help.lyft.com/hc/en-us/all/articles/360001562167-Rental-car-pickups-renewals-and-returns',
        'bullet': 'Renew',
        'expected-text': 'Renew'
        }


@pytest.mark.parametrize("case", cases)
def test_LyftExample(case):
    driver = webdriver.Firefox()
    driver.get(base_url)
    driver.find_element(selectors.helppage('closebutton')).click()
    driver.find_element(selectors.helppage('searchField')).click()
    driver.find_element(selectors.helppage('searchField')).send_keys(case['query'])
    driver.find_element(selectors.helppage('searchButton')).click()
    #driver.find_element(By.XPATH, '//*[@aria-label="Pick up, renew, and return your Express Drive renta"]').click()
    WebDriverWait(driver, 100)
    #driver.find_element(By.XPATH, '//*[text()="'+case['bullet']+'"]').click()
    #assert driver.find_element(By.XPATH, '//*[text()="'+case['expected-text']+'"]').is_displayed()
    driver.close()

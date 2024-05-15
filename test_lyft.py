from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import page_selctors

defalut_wait = 10
base_url = 'https://help.lyft.com/hc/en-us'
cases = [
    {
        'query': 'Pick up, renew, and return your Express Drive rental',
        'expected_url': 'Rental-car-pickups-renewals-and-returns',
        'bullet': 'Renew',
        'expected_text': 'Renew'
    }
]


@pytest.fixture(autouse=True, scope='class')
def driver():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()


def wait_for_element(driver, selector):
    WebDriverWait(driver, defalut_wait).until(EC.element_to_be_clickable(selector))
    return driver.find_element(*selector)


def wait_for_element_to_disappear(driver, selector):
    WebDriverWait(driver, defalut_wait).until(EC.invisibility_of_element(selector))
    return True


@pytest.mark.parametrize("case", cases)
def test_lyft_example(case, driver):
    wait_for_element(driver, page_selctors.help_page('closeButton')).click()
    search_field = wait_for_element(driver, page_selctors.help_page('searchField'))
    search_field.click()
    search_field.send_keys(case['query'])
    wait_for_element(driver, page_selctors.help_page('searchButton')).click()
    wait_for_element_to_disappear(driver, page_selctors.help_page('progressBar'))
    wait_for_element(driver, page_selctors.dynamic_help_page('result',case['query'])).click()
    WebDriverWait(driver, defalut_wait).until(EC.url_contains(case['expected_url']))
    wait_for_element(driver, page_selctors.dynamic_help_page('bullet',case['bullet'])).click()
    assert driver.find_element(By.XPATH, '//*[contains(text(),\''+case['expected_text']+'\')]').is_displayed()
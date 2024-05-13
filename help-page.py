from selenium.webdriver.common.by import By


def helppage(selector):
    elements = {
        'closeButton': (By.XPATH, '//*[@aria-label="Close banner"]'),
        'searchField': (By.XPATH, '//*[@id="searchInputForm"]//div[@role="combobox"]//input'),
        'searchButton': (By.XPATH, '//*[@data-testid="core-ui-icon-search"]'),
    }
    return elements[selector]  

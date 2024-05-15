from selenium.webdriver.common.by import By


def help_page(selector):
    elements = {
        'closeButton': (By.XPATH, '//*[@aria-label="Close banner"]'),
        'searchField': (By.XPATH, '//*[@id="searchInputForm"]//div[@role="combobox"]//input'),
        'searchButton': (By.XPATH, '//*[@data-testid="core-ui-icon-search"]'),
        'progressBar': (By.XPATH, '//*[@role="progressbar"]'),
    }
    return elements[selector]


def dynamic_help_page(selector,arg1):
    elements = {
        'result': (By.XPATH,'//*[contains(@aria-label,\''+arg1+'\')]//div'),
        'bullet': (By.XPATH,'//*[contains(text(),\''+arg1+'\')]')
    }
    return elements[selector]
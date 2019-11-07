import pytest


@pytest.fixture(scope='module')
def driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.headless = True
    return webdriver.Chrome(options=options)

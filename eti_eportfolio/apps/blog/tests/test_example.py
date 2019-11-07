from selenium import webdriver


def test_example():
    assert 1 + 1 == 2


def test_web_example():
    options = webdriver.ChromeOptions()

    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get('http://google.com')

    assert 'Google' in driver.title

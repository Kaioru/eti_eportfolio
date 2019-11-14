from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_blog_index_empty(driver, live_server):
    driver.get(live_server.url + '/blogs/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 1


def test_view_blog_index_populated(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 0


def test_view_blog_index_info(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_id('post-title').text == 'A cool title'
    assert driver.find_element_by_id('post-body').text == 'Lorem ipsum' + '...'


def test_view_blog_index_body_overflow(driver, live_server, seed_post):
    seed_post.body = "x" * 450
    seed_post.save()

    driver.get(live_server.url + '/blogs/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_id('post-title').text == 'A cool title'
    assert driver.find_element_by_id('post-body').text == 'x' * 400 + '...'

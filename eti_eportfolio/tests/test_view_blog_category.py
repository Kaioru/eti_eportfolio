from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_blog_category(driver, live_server, seed_category):
    driver.get(live_server.url + '/blogs/' + str(seed_category.name))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_tag_name('h1').text == 'Rants'


def test_view_blog_category_has_posts(driver, live_server, seed_category, seed_post):
    driver.get(live_server.url + '/blogs/' + str(seed_category.name))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 0


def test_view_blog_category_no_posts(driver, live_server, seed_category):
    driver.get(live_server.url + '/blogs/' + str(seed_category.name))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 1


def test_view_blog_category_not_found(driver, live_server):
    driver.get(live_server.url + '/blogs/' + str('Rants'))

    assert len(driver.find_elements_by_tag_name('h1')) == 0

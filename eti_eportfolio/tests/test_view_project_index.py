from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_project_index_empty(driver, live_server):
    driver.get(live_server.url + '/projects/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 1


def test_view_project_index_populated(driver, live_server, seed_project):
    driver.get(live_server.url + '/projects/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 0


def test_view_project_index_info(driver, live_server, seed_project):
    driver.get(live_server.url + '/projects/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_id('project-title').text == 'ETI ePortfolio'
    assert driver.find_element_by_id(
        'project-desc').text == 'a pretty cool example django project to show testcases and stuff.'

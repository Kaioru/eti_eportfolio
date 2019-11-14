from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_project_detail(driver, live_server, seed_project):
    driver.get(live_server.url + '/projects/' + str(seed_project.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_id('project-title').text == 'ETI ePortfolio'


def test_view_blog_detail_not_found(driver, live_server):
    driver.get(live_server.url + '/projects/' + str(1))

    assert len(driver.find_elements_by_id('project-title')) == 0

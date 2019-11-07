from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_blog_index(driver, live_server):
    driver.get(live_server.url + '/blogs')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    elem = driver.find_element_by_tag_name('h1')
    assert elem.text == 'Blog Index'

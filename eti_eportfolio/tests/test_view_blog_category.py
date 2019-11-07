from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from eti_eportfolio.apps.blog.models import Category


def test_view_blog_detail(driver, live_server):
    category = Category(name='personal')
    category.save()

    driver.get(live_server.url + '/blogs/personal')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    elem = driver.find_element_by_tag_name('h1')
    assert elem.text == 'Personal'

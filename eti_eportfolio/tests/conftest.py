import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='module')
def driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.headless = True

    chrome = webdriver.Chrome(options=options)

    yield chrome

    chrome.close()


@pytest.fixture
def admin_login_page(driver, live_server, django_user_model):
    driver.get(live_server.url + '/admin')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "content"))))

    django_user_model.objects.create_superuser(
        username='admin', email='admin@admin.com', password='password')


@pytest.fixture
def admin_page(driver, admin_login_page):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('password')
    driver.find_element_by_name('password').send_keys(Keys.RETURN)

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "user-tools"))))


@pytest.fixture
def admin_change_password_page(driver, live_server, admin_page):
    current_url = driver.current_url

    driver.get(live_server.url + '/admin/password_change/')

    WebDriverWait(driver, 3).until(EC.url_changes(current_url))
    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.NAME, "old_password"))))

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


@pytest.fixture
def admin_login_page(driver, live_server, django_user_model):
    driver.get(live_server.url + '/admin/')

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "content"))))

    django_user_model.objects.create_superuser(
        username='admin', email='admin@admin.com', password='password')


@pytest.fixture
def admin_main_page(driver, admin_login_page):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('password')
    driver.find_element_by_name('password').send_keys(Keys.RETURN)

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "user-tools"))))


def test_view_admin_category_create_valid(driver, live_server, admin_main_page):
    driver.get(live_server.url + '/admin/blog/category/add/')
    driver.find_element_by_name('name').send_keys('Random Category')
    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_category_create_too_long(driver, live_server, admin_main_page):
    driver.get(live_server.url + '/admin/blog/category/add/')
    driver.find_element_by_name('name').send_keys('x' * 25)

    assert driver.find_element_by_name(
        'name').get_attribute("value") == 'x' * 20

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_category_edit_valid(driver, live_server, admin_main_page, seed_category):
    driver.get(live_server.url + '/admin/blog/category/' +
               str(seed_category.id) + '/change/')

    driver.find_element_by_name('name').clear()
    driver.find_element_by_name('name').send_keys('x' * 25)

    assert driver.find_element_by_name(
        'name').get_attribute("value") == 'x' * 20

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_category_edit_too_long(driver, live_server, admin_main_page, seed_category):
    driver.get(live_server.url + '/admin/blog/category/' +
               str(seed_category.id) + '/change/')

    driver.find_element_by_name('name').clear()
    driver.find_element_by_name('name').send_keys('Random Category')
    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_category_delete(driver, live_server, admin_main_page, seed_category):
    driver.get(live_server.url + '/admin/blog/category/')

    select = Select(driver.find_element_by_name('action'))
    select.select_by_value('delete_selected')

    checkbox = driver.find_element_by_xpath(
        "//input[@value='" + str(seed_category.id) + "']")
    checkbox.click()

    driver.find_element_by_name('index').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))))

    driver.find_element_by_xpath("//input[@type='submit']").click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_category_delete_none_selected(driver, live_server, admin_main_page, seed_category):
    driver.get(live_server.url + '/admin/blog/category/')

    select = Select(driver.find_element_by_name('action'))
    select.select_by_value('delete_selected')

    driver.find_element_by_name('index').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "warning"))))

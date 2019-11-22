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


def test_view_admin_comment_create_valid(driver, live_server, admin_main_page, seed_post):
    driver.get(live_server.url + '/admin/blog/comment/add/')
    driver.find_element_by_name('author').send_keys('Keith')
    driver.find_element_by_name('body').send_keys('Hello World!')

    select = Select(driver.find_element_by_name('post'))
    select.select_by_value(str(seed_post.id))

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_comment_create_too_long(driver, live_server, admin_main_page, seed_post):
    driver.get(live_server.url + '/admin/blog/comment/add/')
    driver.find_element_by_name('author').send_keys('x' * 61)
    driver.find_element_by_name('body').send_keys('Hello World!')

    select = Select(driver.find_element_by_name('post'))
    select.select_by_value(str(seed_post.id))

    assert driver.find_element_by_name(
        'author').get_attribute("value") == 'x' * 60

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_comment_create_empty(driver, live_server, admin_main_page):
    driver.get(live_server.url + '/admin/blog/comment/add/')
    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "errornote"))))


def test_view_admin_comment_edit_valid(driver, live_server, admin_main_page, seed_comment):
    driver.get(live_server.url + '/admin/blog/comment/' +
               str(seed_comment.id) + '/change/')

    driver.find_element_by_name('author').clear()
    driver.find_element_by_name('author').send_keys('x' * 60)

    assert driver.find_element_by_name(
        'author').get_attribute("value") == 'x' * 60

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_comment_edit_too_long(driver, live_server, admin_main_page, seed_comment):
    driver.get(live_server.url + '/admin/blog/comment/' +
               str(seed_comment.id) + '/change/')

    driver.find_element_by_name('author').clear()
    driver.find_element_by_name('author').send_keys('x' * 61)

    assert driver.find_element_by_name(
        'author').get_attribute("value") == 'x' * 60

    driver.find_element_by_name('_save').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_comment_delete(driver, live_server, admin_main_page, seed_comment):
    driver.get(live_server.url + '/admin/blog/comment/')

    select = Select(driver.find_element_by_name('action'))
    select.select_by_value('delete_selected')

    checkbox = driver.find_element_by_xpath(
        "//input[@value='" + str(seed_comment.id) + "']")
    checkbox.click()

    driver.find_element_by_name('index').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))))

    driver.find_element_by_xpath("//input[@type='submit']").click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "success"))))


def test_view_admin_comment_delete_none_selected(driver, live_server, admin_main_page, seed_comment):
    driver.get(live_server.url + '/admin/blog/comment/')

    select = Select(driver.find_element_by_name('action'))
    select.select_by_value('delete_selected')

    driver.find_element_by_name('index').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.CLASS_NAME, "warning"))))

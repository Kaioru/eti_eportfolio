import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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


@pytest.fixture
def admin_change_password_page(driver, live_server, admin_main_page):
    current_url = driver.current_url

    driver.get(live_server.url + '/admin/password_change/')

    WebDriverWait(driver, 3).until(EC.url_changes(current_url))
    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.NAME, "old_password"))))


def test_admin_login_valid(driver, admin_login_page):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('password')
    driver.find_element_by_name('password').send_keys(Keys.RETURN)

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "user-tools"))))

    user_tools_elem = driver.find_element_by_id('user-tools')

    assert user_tools_elem.find_element_by_tag_name('strong').text == 'ADMIN'


def test_admin_change_password_wrong_old_password(driver, admin_change_password_page):
    driver.find_element_by_name('old_password').send_keys('wrongOldPassword')
    driver.find_element_by_name('new_password1').send_keys('matchingPassword')
    driver.find_element_by_name('new_password2').send_keys('matchingPassword')
    driver.find_element_by_name('new_password2').send_keys(Keys.RETURN)

    error = driver.find_element_by_class_name(
        'errorlist').find_elements_by_tag_name("li")[0]

    assert error.text == 'Your old password was entered incorrectly. Please enter it again.'


def test_admin_change_password_mismatch_new_passwords(driver, admin_change_password_page):
    driver.find_element_by_name('old_password').send_keys('password')
    driver.find_element_by_name('new_password1').send_keys('mismatchPassword1')
    driver.find_element_by_name('new_password2').send_keys('mismatchPassword2')
    driver.find_element_by_name('new_password2').send_keys(Keys.RETURN)

    error = driver.find_element_by_class_name(
        'errorlist').find_elements_by_tag_name("li")[0]

    assert error.text == 'The two password fields didn\'t match.'


def test_admin_change_password_password_too_short(driver, admin_change_password_page):
    driver.find_element_by_name('old_password').send_keys('password')
    driver.find_element_by_name('new_password1').send_keys('abdzxc1')
    driver.find_element_by_name('new_password2').send_keys('abdzxc1')
    driver.find_element_by_name('new_password2').send_keys(Keys.RETURN)

    error = driver.find_element_by_class_name(
        'errorlist').find_elements_by_tag_name("li")[0]

    assert error.text == 'This password is too short. It must contain at least 8 characters.'


def test_admin_change_password_valid(driver, admin_change_password_page):
    current_url = driver.current_url

    driver.find_element_by_name('old_password').send_keys('password')
    driver.find_element_by_name('new_password1').send_keys('abdzxc123')
    driver.find_element_by_name('new_password2').send_keys('abdzxc123')
    driver.find_element_by_name('new_password2').send_keys(Keys.RETURN)

    WebDriverWait(driver, 3).until(EC.url_changes(current_url))

    content = driver.find_element_by_id('content')

    assert content.find_element_by_tag_name(
        'h1').text == 'Password change successful'

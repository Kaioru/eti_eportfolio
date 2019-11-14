from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_view_blog_detail(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/' + str(seed_post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert driver.find_element_by_id('post-title').text == 'A cool title'


def test_view_blog_detail_has_comments(driver, live_server, seed_post, seed_comment):
    driver.get(live_server.url + '/blogs/' + str(seed_post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 0


def test_view_blog_detail_no_comments(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/' + str(seed_post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    assert len(driver.find_elements_by_id('error')) == 1


def test_view_blog_detail_not_found(driver, live_server):
    driver.get(live_server.url + '/blogs/' + str(1))

    assert len(driver.find_elements_by_id('post-title')) == 0


def test_view_create_comment_valid(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/' + str(seed_post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    driver.find_element_by_name('author').send_keys('x' * 60)
    driver.find_element_by_name('body').send_keys('Cool blog post!')
    driver.find_element_by_id('submit').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "comment-body"))))

    author = driver.find_element_by_id('comment-author')
    b = author.find_element_by_tag_name('b')

    assert b.text == 'x' * 60


def test_view_create_comment_invalid(driver, live_server, seed_post):
    driver.get(live_server.url + '/blogs/' + str(seed_post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    driver.find_element_by_name('author').send_keys('x' * 61)
    driver.find_element_by_name('body').send_keys('Cool blog post!')

    assert driver.find_element_by_name(
        'author').get_attribute("value") == 'x' * 60

    driver.find_element_by_id('submit').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "comment-body"))))

    author = driver.find_element_by_id('comment-author')
    b = author.find_element_by_tag_name('b')

    assert b.text == 'x' * 60

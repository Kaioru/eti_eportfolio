from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from eti_eportfolio.apps.blog.models import Category, Post


def test_view_blog_detail(driver, live_server):
    post = Post(title='A cool title', body='Lorem ipsum')
    category = Category(name='personal')

    post.save()
    category.save()
    post.categories.add(category)

    driver.get(live_server.url + '/blogs/' + str(post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    elem = driver.find_element_by_tag_name('h1')
    assert elem.text == 'A cool title'


def test_create_comment_valid(driver, live_server):
    post = Post(title='A cool title', body='Lorem ipsum')
    category = Category(name='personal')

    post.save()
    category.save()
    post.categories.add(category)

    driver.get(live_server.url + '/blogs/' + str(post.id))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.TAG_NAME, "h1"))))

    driver.find_element_by_name('author').send_keys('Commenter')
    driver.find_element_by_name('body').send_keys('Cool blog post!')
    driver.find_element_by_tag_name('button').click()

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "comment-body"))))

    comment = driver.find_element_by_id('comment-body')
    assert comment.text == 'Cool blog post!'

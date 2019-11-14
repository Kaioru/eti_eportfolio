import pytest
from eti_eportfolio.apps.blog.models import *
from eti_eportfolio.apps.project.models import *


@pytest.fixture(scope='module')
def driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.headless = True

    chrome = webdriver.Chrome(options=options)

    yield chrome

    chrome.close()


@pytest.fixture
def seed_category():
    category = Category(name='Rants')
    category.save()

    return category


@pytest.fixture
def seed_post(seed_category):
    post = Post(title='A cool title', body='Lorem ipsum')
    post.save()
    post.categories.add(seed_category)

    return post


@pytest.fixture
def seed_comment(seed_post):
    comment = Comment(author="Keith", body="Hello hello!")
    comment.save()
    seed_post.comments.add(comment)

    return comment


@pytest.fixture
def seed_project():
    project = Project(title='ETI ePortfolio',
                      description='a pretty cool example django project to show testcases and stuff.',
                      technology='Python',
                      image='eti_eportfolio.jpg')
    project.save()

    return project

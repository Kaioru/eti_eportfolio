import pytest

# These test cases ensure that the str() method works on the models.
# Which ensures it shows up as legible text in the admin pages.


@pytest.mark.django_db
def test_category_str(seed_category):
    assert seed_category.__str__() == str(seed_category)


@pytest.mark.django_db
def test_post_str(seed_post):
    assert seed_post.__str__() == str(seed_post)


@pytest.mark.django_db
def test_comment_str(seed_comment):
    assert seed_comment.__str__() == str(seed_comment)


@pytest.mark.django_db
def test_project_str(seed_project):
    assert seed_project.__str__() == str(seed_project)

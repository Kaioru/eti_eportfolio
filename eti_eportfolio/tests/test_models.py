import pytest

# These test cases ensure that the str() method works on the models.
# Which ensures it shows up as legible text in the admin pages.


@pytest.mark.django_db
def test_category_str(seed_category):
    assert str(seed_category) == seed_category.name


@pytest.mark.django_db
def test_post_str(seed_post):
    assert str(seed_post) == seed_post.title


@pytest.mark.django_db
def test_comment_str(seed_comment):
    assert str(seed_comment) == seed_comment.body[:20]


@pytest.mark.django_db
def test_project_str(seed_project):
    assert str(seed_project) == seed_project.title

from eti_eportfolio.apps.blog.models import Comment


def test_post_comment_valid(client, live_server, seed_post):
    url = live_server.url + '/blogs/' + str(seed_post.id)
    response = client.post(url,
                           data={'author': "Keith", 'body': "Hello hello!"},
                           follow=True)

    assert response.status_code == 200

    comment = Comment.objects.first()

    assert comment.author == "Keith"
    assert comment.body == "Hello hello!"


def test_post_comment_empty_data(client, live_server, seed_post):
    url = live_server.url + '/blogs/' + str(seed_post.id)
    response = client.post(url, follow=True)

    assert response.status_code == 200

    count = Comment.objects.count()

    assert count == 0


def test_post_comment_long_body(client, live_server, seed_post):
    url = live_server.url + '/blogs/' + str(seed_post.id)
    response = client.post(url,
                           data={'author': "x" * 61, 'body': "Hello hello!"},
                           follow=True)

    assert response.status_code == 200

    count = Comment.objects.count()

    assert count == 0

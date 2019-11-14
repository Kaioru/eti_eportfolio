def test_blog_index_url(client, live_server):
    url = live_server.url + '/blogs'
    response = client.get(url, follow=True)

    assert response.status_code == 200

    url = url.upper()
    response = client.get(url, follow=True)

    assert response.status_code == 200


def test_blog_category_url(client, live_server, seed_category):
    url = live_server.url + '/blogs/' + seed_category.name
    response = client.get(url, follow=True)

    assert response.status_code == 200

    url = url.upper()
    response = client.get(url, follow=True)

    assert response.status_code == 200


def test_blog_detail_url(client, live_server, seed_post):
    url = live_server.url + '/blogs/' + str(seed_post.id)
    response = client.get(url, follow=True)

    assert response.status_code == 200

    url = url.upper()
    response = client.get(url, follow=True)

    assert response.status_code == 200

def test_project_index_url(client, live_server):
    url = live_server.url + '/projects/'
    response = client.get(url, follow=True)

    assert response.status_code == 200

    url = url.upper()
    response = client.get(url, follow=True)

    assert response.status_code == 200


def test_project_detail_url(client, live_server, seed_project):
    url = live_server.url + '/projects/' + str(seed_project.id)
    response = client.get(url, follow=True)

    assert response.status_code == 200

    url = url.upper()
    response = client.get(url, follow=True)

    assert response.status_code == 200

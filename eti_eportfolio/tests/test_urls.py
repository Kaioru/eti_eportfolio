def test_url_redirect_when_not_found(driver, live_server):
    driver.get(live_server.url + '/randomurl123!')

    assert driver.current_url == live_server.url + '/projects/'

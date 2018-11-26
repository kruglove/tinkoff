import requests


def test_script(http_client):
    response = http_client.get_sub(request_id='1', system_code='2', 'e.kruglova')
    assert response.status_code == 200

def test_first(http_client):
    response = http_client.post_sub('1', '2', 'TCS_SPBXM', 'TCS', 'equity', 20, 'e.kruglova')
    assert response.status_code == 201

def test_delete(http_client):
    response = http_client.del_sub( '1', '1', '2', 'e.kruglova')
    assert response.status_code == 200

def test_get(http_client, id):
    response = http_client.get_sub(request_id='1', system_code='2','e.kruglova')
    assert response.body.get('id') == id

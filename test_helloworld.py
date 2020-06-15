# test_helloworld.py
  
from helloworld.helloworld import app
import json

def test_get_noheader():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>\n'

def test_post_noheader():
    response = app.test_client().post('/')
    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>\n'

def test_post_header():
    with app.test_client() as c3:
        header1 = {'Accept': 'application/json'}
        response = c3.post('/',headers=header1).data
        res = json.loads(response)
        assert str(res["message"]) == "Hello, World"

def test_get_header():
    with app.test_client() as c4:
        header2 = {'Accept': 'application/json'}
        response = c4.get('/',headers=header2).data
        res = json.loads(response)
        assert str(res["message"]) == "Hello, World"

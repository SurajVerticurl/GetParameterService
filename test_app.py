# test_app.py
from app import app
import json

def test_hello():
    client = app.test_client()

    response = client.get('/hello')

    assert response.status_code == 200
    assert 'message' in json.loads(response.data)
    assert json.loads(response.data)['message'] == 'Hello, Jenkins!'

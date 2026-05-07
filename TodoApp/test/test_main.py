from fastapi.testclient import TestClient
from ..main import app
from fastapi import status

client = TestClient(app)

def test_return_health_check():
    resonse = client.get('/healthy')
    assert resonse.status_code == status.HTTP_200_OK
    assert resonse.json() == {'status': 'Healthy'}


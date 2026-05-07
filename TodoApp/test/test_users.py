from .utils import *
from ..routers.user import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = overide_get_current_user

def test_return_users(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'luketest'
    assert response.json()['email'] == 'luketest@qq.com'
    assert response.json()['first_name'] == 'luketest'
    assert response.json()['last_name'] == 'skywalkertest'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'


def test_change_password(test_user):
    response = client.put('/user/password', json={
        'password': 'testpassword',
        'new_password': 'newtestpassword'
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={
        'password': 'wrongpassword',
        'new_password': 'newtestpassword'
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()['detail'] == 'Error on password change'


def test_change_phone_number(test_user):
    response = client.put('/user/phonenumber', params={'phone_number': '0987654321'})
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
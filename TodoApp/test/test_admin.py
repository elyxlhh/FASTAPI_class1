from .utils import *
from ..routers.admin import get_db, get_current_user 
from fastapi import status
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = overide_get_current_user


def test_admin_read_all_authenticated(test_todo):
    response = client.get('/admin/todos')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'id': 1,
        'title': 'Learn to code!',
        'description': 'Learn to code with FastAPI',
        'priority': 4,
        'complete': False,
        'owner_id': 1
    }]


def test_admin_delete_todo_authenticated(test_todo):
    response = client.delete('/admin/todo/1')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    todo_model = db.query(Todos).filter(Todos.id == 1).first()
    assert todo_model is None


def test_admin_delete_todo_not_found():
    response = client.delete('/admin/todo/999')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found'}
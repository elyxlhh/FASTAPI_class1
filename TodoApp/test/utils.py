from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
from ..models import Todos, Users
from ..routers.auth import bcrypt_context
import pytest


SQLALCHEMY_DATABASE_URI = 'sqlite:///./testdb.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, 
    connect_args={'check_same_thread': False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def overide_get_current_user():
    return {'username': 'luke', 'id': 1, 'role': 'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title='Learn to code!',
        description='Learn to code with FastAPI',
        priority=4,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos;'))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        username='luketest',
        email='luketest@qq.com',
        first_name='luketest',
        last_name='skywalkertest',
        hashed_password=bcrypt_context.hash("testpassword"),
        role='admin',
        phone_number='1234567890'
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM users;'))
        connection.commit()
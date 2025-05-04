import pytest
from app import create_app
from models import db, Property

@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Добавляем тестовые данные
            test_prop = Property(
                address="Novaia str.",
                area=75.5,
                price=5000000
            )
            db.session.add(test_prop)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()

def test_property_list(test_client):
    """Тест получения списка объектов"""
    response = test_client.get('/properties')
    assert response.status_code == 200
    assert b"Novaia str." in response.data

def test_property_create(test_client):
    """Тест создания объекта"""
    data = {
        "address": "ул. Новая, 2",
        "area": "80.0",
        "price": "6000000",
        "status": "available"
    }
    response = test_client.post('/properties/add', data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"Object created successfully" in response.data

@pytest.fixture
def property_form_data():
    return {
        'address': 'ул. Тестовая, 1',
        'area': '75.5',
        'price': '5000000',
        'status': 'available'
    }

def test_property_create_route(test_client, property_form_data):
    response = test_client.post(
        '/properties/add',
        data=property_form_data,
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Object created" in response.data
import pytest
from models import Property, Client

class TestPropertyModel:
    def test_property_creation(self):
        """Тест создания объекта недвижимости"""
        prop = Property(
            address="ул. Тестовая, 1",
            area=75.5,
            price=5000000,
            status="available"
        )
        assert prop.address == "ул. Тестовая, 1"
        assert prop.area == 75.5
        assert prop.price == 5000000
        assert prop.status == "available"

    def test_invalid_area(self):
        """Тест валидации площади"""
        with pytest.raises(ValueError):
            Property(area=-100, price=1000000)

class TestClientModel:
    def test_client_types(self):
        """Тест типов клиентов"""
        client = Client(
            name="Иванов Иван",
            phone="+79161234567",
            client_type="buyer"
        )
        assert client.client_type == "buyer"
        assert client.is_buyer() is True
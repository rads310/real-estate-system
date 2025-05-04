def test_property_edit_flow(test_client):
    """Тест полного цикла редактирования"""
    # 1. Получение формы редактирования
    response = test_client.get('/properties/1/edit')
    assert response.status_code == 200
    
    # 2. Отправка изменений
    edit_data = {
        "address": "Changed str.",
        "area": "85.0",
        "price": "5500000"
    }
    response = test_client.post('/properties/1/edit', data=edit_data)
    assert response.status_code == 302  # Редирект после успеха
    
    # 3. Проверка изменений
    response = test_client.get('/properties/1')
    assert b"Changed str." in response.data
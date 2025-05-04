def test_property_list_ui(test_client):
    """Тест UI списка объектов"""
    response = test_client.get('/properties')
    assert b'<table class="property-table">' in response.data
    assert b'Add New Property' in response.data
    assert b'Search' in response.data

def test_navigation(test_client):
    """Тест навигации"""
    response = test_client.get('/')
    assert response.status_code == 302  # Проверка редиректа
    assert '/properties' in response.location
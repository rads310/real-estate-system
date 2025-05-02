# Real Estate Management System

![System Screenshot](screenshots/dashboard.png)

Система управления недвижимостью для автоматизации работы риэлторских агентств.

## Основные функции

- 📌 Управление объектами недвижимости (CRUD)
- 👥 Ведение клиентской базы
- 📝 Работа с договорами
- 🔍 Инспектирование объектов
- 📊 Генерация отчетов

## Технологии

- Python 3.9+
- Flask 2.0
- SQLAlchemy 1.4
- Bootstrap 5
- SQLite (для разработки)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/real-estate-system.git
   cd real-estate-system
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите приложение:
   ```bash
   python app.py
   ```

   Приложение будет доступно по адресу: http://localhost:5000

## Структура проекта

```
real_estate_system/
├── instance/         # База данных SQLite
├── migrations/       # Миграции базы данных (если используется Flask-Migrate)
├── routes/           # Маршруты приложения
├── static/           # Статические файлы (CSS, JS)
├── templates/        # HTML шаблоны
├── tests/            # Тесты
├── app.py            # Основное приложение
├── config.py         # Конфигурация
├── models.py         # Модели данных
└── README.md         # Документация
```

## API Документация

Основные API endpoints:

### Объекты недвижимости
- `GET /properties` - Список всех объектов
- `POST /properties` - Создание нового объекта
- `GET /properties/<id>` - Получение объекта
- `PUT /properties/<id>` - Обновление объекта
- `DELETE /properties/<id>` - Удаление объекта

Пример запроса:
```bash
curl -X GET http://localhost:5000/properties
```

Ответ:
```json
{
  "data": [
    {
      "address": "ул. Ленина, 10",
      "area": 75.5,
      "id": 1,
      "price": 5000000,
      "status": "available"
    }
  ],
  "success": true
}
```

## Лицензия

MIT License. См. файл [LICENSE](LICENSE).
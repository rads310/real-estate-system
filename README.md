# Real Estate Management System

Система для автоматизации работы агентства недвижимости

## Функционал
- Управление объектами недвижимости
- Учет клиентов
- Работа с договорами
- Инспектирование объектов

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/real-estate-system.git
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите приложение:
   ```bash
   python app.py
   ```

## Структура проекта
```
real_estate_system/
├── instance/         # База данных
├── routes/           # Маршруты Flask
├── templates/        # HTML шаблоны
├── app.py            # Основное приложение
├── config.py         # Конфигурация
├── models.py         # Модели данных
└── README.md         # Документация
```
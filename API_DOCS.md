# API Documentation

## Base URL
`http://localhost:5000/api/v1`

## Authentication
Для защищенных endpoints требуется JWT токен:
```
Authorization: Bearer <your_token>
```

## Properties

### Get All Properties
```
GET /properties
```

**Response:**
```json
{
  "data": [
    {
      "id": 1,
      "address": "ул. Примерная, 15",
      "area": 65.5,
      "price": 4500000,
      "status": "available"
    }
  ],
  "success": true
}
```

### Create Property
```
POST /properties
```

**Request Body:**
```json
{
  "address": "Новый адрес",
  "area": 80.0,
  "price": 6000000,
  "status": "available"
}
```

**Response:**
```json
{
  "data": {
    "id": 2,
    "address": "Новый адрес",
    "area": 80.0,
    "price": 6000000,
    "status": "available"
  },
  "message": "Property created",
  "success": true
}
```

## Clients

### Get Client by ID
```
GET /clients/<int:client_id>
```

**Response:**
```json
{
  "data": {
    "id": 1,
    "name": "Иванов Иван",
    "phone": "+79161234567",
    "email": "ivanov@example.com",
    "type": "buyer"
  },
  "success": true
}
```

## Error Responses

**400 Bad Request:**
```json
{
  "error": "Invalid input",
  "message": "Missing required field 'address'",
  "success": false
}
```

**404 Not Found:**
```json
{
  "error": "Not found",
  "message": "Property with id 999 not found",
  "success": false
}
```
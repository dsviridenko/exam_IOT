# Заготовка для Экзамена по IOT

## Эндпоинты

1. `GET /` - Корневая страница
   - Ответ: `{"message": "Welcome to FastAPI REST Server"}`
   - Статусы: 200 (OK)

2. `GET /items` - Получить все элементы
   - Ответ: Список элементов в формате JSON
   - Статусы: 200 (OK)

3. `GET /items/{item_id}` - Получить элемент по ID
   - Параметры: `item_id` (int) в URL
   - Ответ: Элемент в формате JSON
   - Статусы:
     - 200 (OK) - элемент найден
     - 404 (Not Found) - элемент не существует

4. `POST /items` - Создать новый элемент
   - Параметры запроса:
     - `name` (str, обязательный) - название элемента
     - `price` (float, опциональный, по умолчанию 0.0) - цена
   - Ответ: Созданный элемент в формате JSON
   - Статусы:
     - 201 (Created) - успешное создание
     - 422 - невалидные данные

5. `DELETE /items/{item_id}` - Удалить элемент
   - Параметры: `item_id` (int) в URL
   - Ответ: Пустое тело
   - Статусы:
     - 204 (No Content) - успешное удаление
     - 404 (Not Found) - элемент не существует

## Документация

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Запуск проекта

1. Склонируйте репозиторий и перейдите в папку проекта.
   ``` bash
   git clone https://github.com/dsviridenko/exam_IOT.git
   ```
 
2. Откройте терминал и запустите виртуальное окружение(если требуется, установите venv перед этим)
   ``` bash
   python -m venv venv
   ```
   Затем активируйте его

   *Если у вас Windows:
   ``` bash
   venv\Scripts\activate
   ```
   *Если Linux или MacOS:
   ``` bash
   source venv/bin/activate
   ```
3. Установите зависимости
   ``` bash
   pip install -r requerements
   ```
4. Запустите приложение
   ``` bash 
   uvicorn main:app --reload
   ```
5. Для запуска тестов откройте второй терминал, запустите виртуальное окружение и введите команду
   ``` bash
   pytest tests.py
   ```

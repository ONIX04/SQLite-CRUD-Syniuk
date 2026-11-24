# SQLite-CRUD-Syniuk

Лабораторна робота №6-7 з дисципліни «Бази даних».
Веб-застосунок «Домашня бібліотека» на Python (Flask) з базою даних SQLite та повним набором CRUD-операцій.

Виконав: Синюк Ярослав, група КІ-42.

## Запуск

```
python -m venv venv
venv\Scripts\activate        # Windows (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
python app.py
```

Після запуску відкрити http://127.0.0.1:5000/

## Структура

- `database_connector.py` - модуль доступу до даних (усі SQL-запити та CRUD-функції)
- `app.py` - маршрути Flask: `/`, `/add`, `/edit/<id>`, `/delete/<id>`
- `templates/` - HTML-шаблони
- `data.db` - файл бази (створюється автоматично, у репозиторій не потрапляє)

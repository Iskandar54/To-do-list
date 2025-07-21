# To-Do List Project

## Ключевые технологии
- Flask
- PostgreSQL, SQLAlchemy
- Flask-Login, хеширование паролей

## Ключевые особенности
- **Безопасность**: Хеширование паролей, защита сессий
- **Масштабируемость**: Чистая архитектура с разделением на модули
- **Гибкая конфигурация**: настройки через `.env`

## Как запустить локально
# 1. Клонировать и перейти в директорию
git clone https://github.com/Iskandar54/To-do-list.git  
cd To-do-list

# 2. Настроить виртуальное окружение
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate    # Windows  

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Создать БД (PostgreSQL)
createdb todolist

# 5. Запустить
flask run

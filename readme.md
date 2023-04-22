**Логины и пароли:**
админ: admin 
пароль: root

**Локальный запуск проекта**
После клонирования проекта выполните команды:

**Создайте виртуальное окружение командой**
python3 -m venv venv

**Активируйте виртуальное окружение командой**
source venv/bin/activate

**Установите зависимости командой**
pip install -r requirements.txt

**Примените миграции командой**
python manage.py migrate

**Загрузите фикстуры командой**
python3 manage.py loaddata source/fixtures/dump.json

**Запустите проект командой**
python manage.py runserver

**Создайте администратора командой**
python manage.py createsuperuser

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin

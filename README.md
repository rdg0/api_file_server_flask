# api_file_server_flask

Заполнить. Не забыть endpoints или добавить свагер

### Базовая реализация файлового сервера на REST API

Помимо базовых функций программа проверят на дубликаты файлы не только по имени, но и посодержимому.   

Написан для ознакомления с фреймворком flask. Использовано минимальное кол-во вспомогательных библиотек.  
В последующем будет переписан c использованием SQLAlchemy и marshmallow.


### Стек 

Python 3.11  
Flask 2  
SQLite


### Запуск  

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Rdg0/api_file_server_flask
```

```
cd api_file_server_flask
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

В файле settings.py при необходимости изменить директорию сохранения файлов и максимальный размер файла.  


Запустить проект:

```
python3 app.py
``` 


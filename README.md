# api_file_server_flask

Заполнить. Не забыть endpoints или добавить свагер

### Базовая реализация файлового сервера на REST API

Python 3.11  
Flask 2

### Запуск  

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Rdg0/...
```

```
cd ...
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

Перейти в каталог my_site:  

```
cd my_site
```

Выполнить миграции:

```
python3 manage.py migrate
```  

Создать суперпользователя


```
python3 manage.py createsuperuser
```  


Запустить проект:

```
python3 manage.py runserver
``` 


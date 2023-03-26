from flask import Flask, json, request, jsonify
import filecmp # это чтобы сравнить файлы
import os





""" 
В ТЗ (п.4) сказано, что необходимо проверять, есть ли файл с таким же СОДЕРЖИМЫМ в системе или нет.
Соотвественно, проверка на дубликат должная быть не по имени. Вероятно, нужно для каждого нового файла расчитывать MD5 хеш
и хранить в БД.
То есть делаем таблицу
id, filename, extension, hash

 """


 
app = Flask(__name__)





@app.route('/files/get/list', methods=['GET'])
def get_list_files():
    pass


@app.route('/files/get/<extantion>', methods=['GET'])
def get_file_extantion():
    pass


@app.route('/files/create/', methods=['POST']) 
def create():
    pass


@app.route('/files/delete/<filename>', methods=['DELETE'])
def delete_file():
    pass


@app.route('/files/get/<extantion>/<filename>', methods=['GET'])
def get_file():
    pass







if __name__ == '__main__':
    app.run(debug=True)
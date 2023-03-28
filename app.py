import os
from flask import Flask,  jsonify, request, send_from_directory
from flask.typing import ResponseReturnValue
from typing import Dict, List
from werkzeug.utils import secure_filename

import db
import services
import settings


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = settings.FILE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = settings.MAX_FILE_SIZE


@app.route('/files/get/list', methods=['GET'])
def get_list_files() -> ResponseReturnValue:
    """Возвращаем список всех файлы."""
    files: List[Dict] = services.preserializing(db.get_file_list().fetchall())
    return jsonify({'files': files}), 200


@app.route('/files/get/<extantion>', methods=['GET'])
def get_file_extantion(extantion: str) -> ResponseReturnValue:
    """Возвращаем список файлов с определенным расширением."""
    files: List[Dict] = services.preserializing(
        db.get_file_list_by_extention(extantion).fetchall()
    )
    return jsonify({'files': files}), 200


@app.route('/files/create/', methods=['POST'])
def create() -> ResponseReturnValue:
    """Загружаем файл на сервер."""
    if 'file' not in request.files:
        return jsonify(
            {'message': 'no file'}
        ), 409
    file = request.files['file']
    if file.filename == '':
        return jsonify('No selected file'), 409
    if db.get_file_by_name(file.filename).fetchone():
        return jsonify(
            {'message': 'file with that name already exists'}
        ), 409
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    hsh: str = services.get_md5(
        os.path.join(app.config['UPLOAD_FOLDER'], filename)
    )
    if db.get_file_by_hash(hsh).fetchone():
        os.remove((os.path.join(app.config['UPLOAD_FOLDER'], filename)))
        return jsonify(
            {'message': 'file with this content already loaded'}
        ), 409
    db.create_file(*services.parse_file_to_save(filename), hsh)
    return jsonify(
        {'message': 'success'}
    ), 201


@app.route('/files/delete/<filename>', methods=['DELETE'])
def delete_file(filename: str) -> ResponseReturnValue:
    """Удаление файла с сервера."""
    if not db.get_file_by_name(filename).fetchone():
        return jsonify(
            {'message': 'file not found'}
        ), 404
    os.remove((os.path.join(app.config['UPLOAD_FOLDER'], filename)))
    db.delete_file(filename)
    return jsonify(
        {'message': 'success'}
    ), 200


@app.route('/files/get/<extention>/<filename>', methods=['GET'])
def get_file(extention: str, filename: str) -> ResponseReturnValue:
    """Отдаем запрашиваемый файл."""
    if not db.get_file_by_name(filename).fetchone():
        return jsonify(
            {'message': 'file not found'}
        ), 404
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], filename, as_attachment=True
    )


if __name__ == '__main__':
    db.start_db()
    app.run(debug=True)

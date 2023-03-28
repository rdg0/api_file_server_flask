import hashlib
import os
from typing import Dict, List, Tuple

import settings


def get_md5(filename: str) -> str:
    """Получаем хеш файла."""
    with open(filename, 'rb') as f:
        hsh = hashlib.md5()
        while True:
            data = f.read(2048)
            if not data:
                break
            hsh.update(data)
        md5_hash: str = hsh.hexdigest()
    return md5_hash


def preserializing(rows: List[Tuple]) -> List[Dict]:
    """Подготовлаваем данные для сериализации."""
    name_column: Tuple = (
        'id', 'filname', 'extention', 'size', 'md5_hash'
    )
    return [dict(zip(name_column, i)) for i in rows]


def parse_file_to_save(filename: str) -> Tuple[str, str, float]:
    """Подготваливаем данные для сохранения в БД."""
    exteneshion: str = filename.split('.')[-1]
    size: float = os.path.getsize((
        os.path.join(settings.FILE_FOLDER, filename)
    ))
    return filename, exteneshion, size

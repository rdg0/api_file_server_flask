import hashlib


def get_md5(filename):
    """Получаем хеш файла."""
    with open(filename, 'rb') as f:
        hsh = hashlib.md5()
        while True:
            data = f.read(2048)
            if not data:
                break
            hsh.update(data)
        md5_hash = hsh.hexdigest()
    return md5_hash



hsh = get_md5('README.md')
print(type(hsh))
print(hsh)
def get_file_info(file_path: str):
    *path, name = file_path.split('/')
    path = '/'.join(path)
    name, ext = name.split('.')
    return path, name, '.' + ext


print(get_file_info('C:/Users/User/Documents/example.txt'))

import os
"""
Функция возвращает два списка. 
Первый со всеми директориями и поддиректориями любой вложенности.
Второй со всеми вложенными файлами
"""

def dir_files(path):
    subdir=[]
    fil=[]
    for root, dirs, files in os.walk(path):
        subdir.extend(dirs)
        fil.extend(files)
    return subdir, fil
path = 'C:\\Users\\User\\Documents\\Python_book\'s\\Course_Python\\ООП'
#c = dir_files()
#print(c)

"""
Функция удаляет директорию и все её файлы, только если нет поддиректории
"""
def del_dir():
    path = 'C:\\Users\\User\\Documents\\Python_book\'s\\Course_Python\\ООП\\tmp'
    for root, dirs, files in os.walk(path):
        if len(dirs) == 0:
            for file in files:
                os.remove(os.path.join(path, file))
            os.rmdir(path)
            return ('Directory deleted!')
        else:
            return ('Directory has other subdirectory!')
#delete = del_dir()
#print(delete)

def del_del_dir():
    path = 'C:\\Users\\User\\Documents\\Python_book\'s\\Course_Python\\ООП\\tmp'
    subdir, files = dir_files(path)
    if len(subdir) == 0:
        for file in files:
            os.remove(os.path.join(path,file))
        os.rmdir(path)
        return ('Directory deleted!')
    else:
        return ('Directory has other subdirectory!')
del_del = del_del_dir()
print(del_del)

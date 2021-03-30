from zipfile import ZipFile
import os

def archive_ext(path, ext):
    for root, dirs, files in os.walk(path):
        for file in files:
            fil, extension = os.path.splitext(file)
            if extension == ext:
                with ZipFile('new_archive.zip', 'a') as new_arch:
                    new_arch.write(file)
            continue
        return 1
    return 0

path = "C:\\Users\\User\\Documents\\Python_book\'s\\Course_Python\\ООП"
ext = ".py"
arc = archive_ext(path, ext)
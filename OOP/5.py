import random
"""
Функция для генерации заданного количества файлов со случайными числами
"""
def creat_files(files):
    for i in range(1, files+1): # создаём переданное функции количество файлов от 1 до cnt_files
        with open(str(i) + ".txt", "wt") as f: # открываем и записываем три случайных числа от 0 до 100 по одному в каждой строке
            f.write(str(random.randint(0, 100)) + "\n")
            f.write(str(random.randint(0, 100)) + "\n")
            f.write(str(random.randint(0, 100)) + "\n")

created_files = creat_files(10)

"""
Функция суммирования чисел внутри переданных файлов
"""
def sum_num_files(list_files):
    summ = 0
    ext = ".txt"
    for i in list_files:
        with open(str(i) + ext, "rt") as f:
            list_num_file = f.readlines() # считываем все строки файла в список списков
            if len(list_num_file) != 3: # проверяем на количество строк в файле, если больше трех то выводим об этом сообщение
                raise Exception("Файл " + str(i) + ext + "содержит неверное количество аргументов")
            else:
                for j in range(len(list_num_file)):
                    try:
                        summ += int(list_num_file[j]) # проверяем являются ли символы в строке цифрами
                    except ValueError:
                        raise ValueError("В строке №" + str(j+1) + " файла " + str(i) + ext + "содержится не числа!")
    return summ
list_files = random.randint(1,10), random.randint(1,10)
sum_numbers = sum_num_files(list_files)
print(sum_numbers)






"""
    with open(str(file2) + ".txt", "rt") as f2:
        list_num_file2 = f2.readlines() # считываем все строки файла в список списков
        if len(list_num_file2) != 3: # проверяем на количество строк в файле, если больше трех то выводим об этом сообщение
            raise Exception("Файл " + str(file2) + ".txt " + "содержит неверное количество аргументов")
        else:
            for i in range(len(list_num_file2)):
                try:
                    sum2 += int(list_num_file2[i]) # проверяем являются ли символы в строке цифрами
                except ValueError:
                    raise ValueError("В строке №" + str(i+1) + " файла " + str(file2) + ".txt " + "содержится не числа!")
"""
#summ = sum1 + sum2


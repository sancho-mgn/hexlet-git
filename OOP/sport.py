import re
class Sport:
    def __init__(self, number=0, name="E", surname="D", country="F", weidth=100, types="G"):
        self.number = number
        self.name = name
        self.surname = surname
        self.country = country
        self.weidth = weidth
        self.types = types

    def set_number(self, new_number):
        self.number = new_number

    def get_number(self):
        return self.number

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_surname(self):
        return self.surname

    def set_country(self, new_country):
        self.country = new_country

    def get_country(self):
        return self.country

    def set_weidth(self, new_weidth):
        self.weidth = new_weidth

    def get_weidth(self):
        return self.weidth

    def set_type(self, new_type):
        self.types = new_type

    def get_type(self):
        return self.types

def autofill(files):
    lst_x = []
    str1 = "В строке № "
    str2 = " не верно введен аргемунт № "
    with open(files, "rt") as sp:
        list_s = [line.split(', ') for line in sp]
        for j in range(len(list_s)):
            for i in range(len(list_s[j])):
                if i == 0:
                    try:
                        int(list_s[j][i])
                    except ValueError:
                        raise ValueError(str1 + str(j) + str2 + str(j) + " номер игрока!")
                elif i == 1:
                    pattern = re.compile("^[a-zA-Z]+$")
                    if pattern.match(list_s[j][i]):
                        continue
                    else:
                        print(str1 + str(i+1) + str2 + str(j) +  " имя игрока!")
                elif i == 2:
                    pattern = re.compile("^[a-zA-Z]+$")
                    if pattern.match(list_s[j][i]):
                        continue
                    else:
                        print(str1 + str(i+1) + str2 + str(j) +  " фамилия игрока!")
                elif i == 3:
                    pattern = re.compile("^[a-zA-Z]+$")
                    if pattern.match(list_s[j][i]):
                        continue
                    else:
                        print(str1 + str(i+1) + str2 + str(j) + " страна игрока!")
                elif i == 4:
                    try:
                        int(list_s[j][i])
                    except ValueError:
                        raise ValueError(str1 + str(i+1) + str2 + str(j) +  " рост игрока!")
                elif i == 5:
                    pattern = re.compile("^[a-zA-Z]+$")
                    if pattern.match(list_s[j][i]):
                        continue
                    else:
                        print(str1 + str(i+1) + str2 + str(j) +  " тип игрока!")
            new_obj = Sport(*list_s[j])
            lst_x.append(new_obj)
        return lst_x
c = autofill("sportsmen.txt")
import random
class Sportsman:
    def __init__(self, player_id = 0, name = "Ivan", surname = "Ivanov",
                 national = "RUS", new_sport = "Sport", action = 0, status = 0):
        self.player_id = player_id  # уникальный идентификатор спортсмена (счётчик)
        self.name = name  # Имя спортсмена
        self.surname = surname  # Фамилия спортсмена
        self.national = national  # Национальность спортсмена
        self.growth = 190  # Рост спорстмена
        self.weight = 100  # Вес спортсмена
        self.age = 30  # Возраст спорстмена
        self._date_of_birth = 1980  # Полная дата рождения спортсмена
        self._marital = ''  # Семейное положение спортсмена
        self.kind_of_sport = new_sport  # Вид спорта
        self.team = ''  # Команда спорстмена
        self.speed = 0  # скорость спорстмена
        self.action = action  # текущие действия спорстмена (нападает, защищает, контратака, забил гол, пропустил гол и тд)
        self.status = status  # текущий статус спорстмена (бой, штраф, отдых и тд)
        self.cnt_goals = 0  # количество забитых мячей (для любого командного игрока)
        self.cnt_games = 0  # количество сыигранных игр (для любого командного игрока)
        self.cnt_seasons = 0  # количество сыигранных сезонов (для любого командного игрока)
        self.types = ''  # Нападающий, защитник, полузащитник, полунападающий, вратарь

    def set_player_id(self, player_id=0):
        self.player_id = player_id

    def get_player_id(self):
        return self.player_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname

    def set_national(self, national):
        self.national = national

    def get_national(self):
        return self.national

    def set_growth(self, growth):
        self.growth = growth

    def get_growth(self):
        return self.growth

    def set_types_sportsman(self, new_sport):
        self.kind_of_sport = new_sport

    def get_types_sportsman(self):
        return self.kind_of_sport

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def set_goals(self):
        self.cnt_goals += 1

    def get_goals(self):
        return self.cnt_goals

    def set_games(self):
        self.cnt_games += 1

    def get_games(self):
        return self.cnt_games

    def set_seasons(self):
        self.cnt_seasons += 1

    def get_seasons(self):
        return self.cnt_seasons

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
        return self.speed

    def stop(self):
        self.speed = 0

    def set_action(self, new_action):
        self.action = new_action

    def get_action(self):
        return self.action

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def set_types(self, new_types):
        self.types = new_types

    def get_types(self):
        return self.types


class Footballer(Sportsman):

    def __init__(self, player_id=0, name="Ivan", surname="Ivanov", national="RUS"
                 , foot_new_sport="Футболист", foot_status=0, foot_action=0):
        super().__init__(player_id, name, surname, national, new_sport=foot_new_sport
                         , action=foot_action, status=foot_status)

    def created(self):
        print("Создан Футболист!")

    def set_status(self, foot_status):  # статус футболиста например выдана красная карточка или желтая тогда футболист обнуляет скорость и меняет статус на скамейка
        self.status = foot_status

    def get_status(self):
        i = 0
        if self.status == 0:
            self.stop()
            print("Красная карточка! Футболистом", self.get_name(), self.get_surname(), "получена красная карточка!")
        elif self.status == 1:
            i += 1
            if i >= 2:
                self.stop()
                print("Футболистом", self.get_name(), self.get_surname(), "получено 2 жёлтых карточки!")
        else:
            self.set_speed(10)
            print("Футболиcт", self.get_name(), self.get_surname(),"в активном состоянии на поле!")


    def set_action(self, foot_action):
        self.action = foot_action

    def get_action(self):
        if self.action == 0:
            self.set_speed(10)
            print("Футболист",  self.get_name(), self.get_surname(), "в нападении!")
        elif self.action == 1:
            self.set_speed(5)
            print("Футболист",  self.get_name(), self.get_surname(), "в защите!")
        elif self.action == 2:
            self.set_speed(15)
            print("Футболист",  self.get_name(), self.get_surname(), "в контраттаке!")
        else:
            self.stop()
            print("Футболист", self.get_name(), self.get_surname(), "стоит!")

class Basketballer(Sportsman):
    def __init__(self, player_id=0, name="Ivan", surname="Ivanov", national="RUS"
                 , foot_new_sport="Баскетболист", basket_status=0, basket_action=0):
        super().__init__(player_id, name, surname, national, new_sport=foot_new_sport, action=basket_action,
                         status=basket_status)


    def created(self):
        print("Создан Баскетболист!" + self.get_name() + self.get_surname())

    def set_status(self, basket_status):  # статус баскетболиста
        self.status = basket_status

    def get_status(self):
        if self.status == 0:
            self.stop()
            print("Получено 2 фола за неспортивное поведение! Баскетболист", self.get_name(), self.get_surname(),
                  "на скамейки запасных в течении всей игры!")
        elif self.status == 1:
            self.stop()
            print("Получено 6 технических фолов! Баскетболист", self.get_name(), self.get_surname(),
                  "на скамейки запасных в течении всей игры!")
        else:
            self.set_speed(10)
            print("Баскетболист", self.get_name(), self.get_surname(),
                  "в активном состоянии на игровом поле!")

    def set_action(self, basket_action):
        self.action = basket_action

    def get_action(self):
        if self.action == 0:
            self.set_speed(10)
            print("Баскетболист",  self.get_name(), self.get_surname(), "в нападении!")
        elif self.action == 1:
            self.set_speed(5)
            print("Баскетболист",  self.get_name(), self.get_surname(), "в защите!")
        elif self.action == 2:
            self.set_speed(15)
            print("Баскетболист",  self.get_name(), self.get_surname(), "в контраттаке!")
        else:
            self.stop()
            print("Баскетболист", self.get_name(), self.get_surname(), "стоит!")

"""
John_Hunter = Basketballer(0,"John", "Hunter", "USA", 220, 120, 23, 12122000, "Married", "Баскетболист", "Динамо", "Нападающий", 0, 1)
Mike_Jordan = Basketballer(1,"Mike", "Jordan", "USA", 223, 123, 54, 30101966, "Unmarried", "Баскетболист", "СКА", "Нападающий", 1, 0)
Steve_Kock = Basketballer(2, "Steve", "Kock", "Canada", 200, 100, 27, 12121993, "Married", "Баскетболист", "Ласточка", "Нападающий", 0, 2)
Nick_Tole = Basketballer(3, "Nick", "Tole", "India", 203, 103, 29, 12121991, "Unmarried", "Баскетболист", "Местные фонари", "Нападающий", 1, 1)
Erny_Thule = Basketballer(4, "Thule", "Erny", "Russia", 233, 133, 24, 12121996, "Married", "Баскетболист", "Трактор", "Нападающий", 0, 0)

Ronaldo = Footballer(5, "Ronaldo", "Ricaro", "Brasil", 180, 80, 23, 12122000, "Married", "Футболист", "Динамо", "Нападающий", 1, 1)
Pele = Footballer(6, "Pele", "Richard", "Brasil", 160, 90, 63, 11051957, "Unmarried", "Футболист", "Металлург", "Полузащитник", 0, 0)
Loloo = Footballer(7, "Loloo", "Nick", "Germany", 199, 60, 23, 11051997, "Married", "Футболист", "ЦСКА", "Защитник", 2, 0)
Martin = Footballer(8, "Martin", "Zick", "Finland", 168, 75, 31, 11061989, "Unmarried", "Футболист", "Зенит", "Нападающий", 0, 1)
Steford = Footballer(9, "Steford", "Nikolay", "Russia", 174, 62, 21, 11061999, "Married", "Футболист", "Зенит", "Нападающий", 1, 0)

with open("sportsmen.txt", "rt") as s:
    list_sports = s.readlines()
    x = 1
    for i in range(len(list_sports)):

            x = Footballer(list_sports[i].split(','))
            print(list_sports[i].split(', '))
            print(x.get_name(),x.get_surname())
            x.created()
"""
def create_sportsman():   
    with open("sportsmen.txt", "rt") as sp:
        list_sport = [line.split() for line in sp]
        sport_list2 = []
        for i in range(len(list_sport)):
            if random.randint(0, 100) < 50:
                new_obj = Footballer()
                for j in range(len(list_sport[i])):
                    if j==0:
                        new_obj.set_player_id(list_sport[i][j])
                    elif j==1:
                        new_obj.set_name(list_sport[i][j])
                    elif j==2:
                        new_obj.set_surname(list_sport[i][j])
                    elif j==3:
                        new_obj.set_growth(list_sport[i][j])
                    elif j==4:
                        new_obj.set_types_sportsman(list_sport[i][j])
                    elif j==5:
                        new_obj.set_team(list_sport[i][j])
                    elif j==6:
                        new_obj.set_types(list_sport[i][j])
                    elif j==7:
                        new_obj.set_status(list_sport[i][j])
                    else:
                        new_obj.set_action(list_sport[i][j])
                sport_list2.append(new_obj)
            else:
                new_obj = Basketballer()
                for h in range(len(list_tmp)):
                    if h == 0:
                        new_obj.set_player_id(list_tmp[h])
                    elif h == 1:
                        new_obj.set_name(list_tmp[h])
                    elif h == 2:
                        new_obj.set_surname(list_tmp[h])
                    elif h == 3:
                        new_obj.set_growth(list_tmp[h])
                    elif h == 4:
                        new_obj.set_types_sportsman(list_tmp[h])
                    elif h == 5:
                        new_obj.set_team(list_tmp[h])
                    elif h == 6:
                        new_obj.set_types(list_tmp[h])
                    elif h == 7:
                        new_obj.set_status(list_tmp[h])
                    else:
                        new_obj.set_action(list_tmp[h])
                    print(list_tmp[h])
                    print(new_obj.get_player_id(), new_obj.get_name(), new_obj.get_surname(),
                          new_obj.get_types_sportsman())
            sport_list2.append(new_obj)
        return sport_list2
cr_sp = create_sportsman()
print(cr_sp)
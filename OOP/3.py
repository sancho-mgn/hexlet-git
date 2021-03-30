class Sportsman:

    def __init__(self, name, surname, national, growth, weight, age, date_of_birth, marital, kind_of_sport, team,
                 action, status):
        self.player_id += 1  # уникальный идентификатор спортсмена (счётчик)
        self.first_name = name  # Имя спортсмена
        self.second_name = surname  # Фамилия спортсмена
        self.national = national  # Национальность спортсмена
        self.growth = growth  # Рост спорстмена
        self.weight = weight  # Вес спортсмена
        self.age = age  # Возраст спорстмена
        self._date_of_birth = date_of_birth  # Полная дата рождения спортсмена
        self._marital = marital  # Семейное положение спортсмена
        self.kind_of_sport = kind_of_sport  # Вид спорта
        self.team = team  # Команда спорстмена
        self.speed = 0  # скорость спорстмена
        self.action = action  # текущие действия спорстмена (нападает, защищает, контратака, забил гол, пропустил гол и тд)
        self.status = status  # текущий статус спорстмена (бой, штраф, отдых и тд)

    def get_speed(self):
        return self._speed

    def set_speed(self, new_speed):
        self._speed = new_speed

    def stop(self):
        self._speed = 0

    def status(self, new_status):
        self.status = new_status


class Footballer(Sportsman):

    def __init__(self, player_id, name, surname, national, growth, weight, age, date_of_birth, marital, kind_of_sport,
                 team, types, status, action):
        super().__init__(player_id, name, surname, national, growth, weight, age, date_of_birth, marital, kind_of_sport,
                         team, status, action)
        self.__types = types  # Нападающий, защитник, полузащитник, полунападающий, вратарь
        self.__cnt_games = 0  # Количество сыигранных игр
        self.__cnt_seasons = 0  # Количество сыигранных сезонов
        self.__cnt_goals = 0  # Количество забитых мячей
        self.__cnt_pass_boals = 0  # Количество пропущенных мечей (для вратарей)

    def set_types(self, new_types):
        self.__types = new_types

    def get_types(self):
        return self.__types

    def set_status(self,
                   new_status):  # статус футболиста например выдана красная карточка или желтая тогда футболист обнуляет скорость и меняет статус на скамейка
        i = 0
        self.status = new_status
        if new_status == "Red":
            self.stop()
        elif new_status == "Yellow":
            i += 1
            if i >= 2:
                self.stop()
        else:
            self.set_speed(10)

    def set_goals(self, goals):
        self.__cnt_goals += goals

    def scored(self):
        self.__cnt_goals += 1

    def get_goals(self):
        return self.__cnt_goals

    def set_games(self, new_game):
        self.__cnt_games += new_game

    def get_games(self):
        return self.__cnt_games

    def set_seasons(self, new_season):
        self.__cnt_seasons += new_season

    def get_seasons(self):
        return self.__cnt_seasons

    def set_passed_boal(self, new_pas_boal):
        self.__cnt_pass_boals += new_pas_boal

    def get_passed_boal(self):
        return self.__cnt_pass_boals

    def action(self, new_action):
        self._action = new_action
        if new_action == "Attack" or new_action == "Protect" or new_action == "Counter attack" or new_action == "Corner kick":
            self.run(10)
        elif new_action == "scored":
            self.stop()
            self.scored()


ronaldo = Footballer("Ronaldo", "Ricaro", "Brasil", 180, 80, 23, 12122000, "Married", "Football", "Динамо",
                     "Нападающий", "Green", "Attack")
ronaldo.set_status("Red")
print(ronaldo.set_status())
ronaldo.set_status("Green")
ronaldo.set_goals(200)
print(ronaldo.get_goals())
ronaldo.set_games(10)
print(ronaldo.get_games())
ronaldo.set_seasons(5)
print(ronaldo.get_seasons())
ronaldo.name = "Ron"
ronaldo.marital = "Unworied"
ronaldo.set_action("scored")
print(ronaldo.get_goals(), ronaldo.get_speed())
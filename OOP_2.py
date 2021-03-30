import random

class Gamer:
    
    def __init__(self, id, name, surname, national, team, types, status, age, speed, cnt_games, cnt_seasons, cnt_goals, cnt_pass_boals):
        self.player_id = id # уникальный идентификатор игрока (счётчик)
        self.first_name = name # Имя игрока
        self.second_name = surname # Фамилия игрока
        self.national = national # Национальность игрока
        self.team = team # Команда игрока
        self.types = types # Нападающий, защитник, полузащитник, полунападающий, вратарь
        self.status = status # текущий статус футболиста
        self.age = age # Возраст
        self.speed = speed # скорость футболиста
        self.cnt_games = cnt_games # Количество сыигранных игр
        self.cnt_seasons = cnt_seasons # Количество сыигранных сезонов
        self.cnt_goals = cnt_goals # Количество забитых мячей
        self.cnt_pass_boals = cnt_pass_boals # Количество пропущенных мечей (для вратарей)
    
    def Run(self, new_speed):
        self.speed = new_speed
    
    def Stop(self):
        self.speed = 0
    
    def Status(self, new_status): # статус футболиста например выдана красная карточка или желтая тогда футболист обнуляет скорость и меняет статус на скамейка
        self.status = new_status
        if new_status == "Red":
            self.Stop()
        elif new_status == "Yellow":
            i += 1
            if i >= 2:
                self.Stop()
        else:
            self.Run(10)
    
    def Goals(self, new_goal):
        self.cnt_goals += new_goal
        
    def Games(self, new_game):
        self.cnt_games += new_game
    
    def Seasons(self, new_season):
        self.cnt_seasons += new_season
    
    def Passed_boal(self, new_pas_boal):
        self.cnt_pass_boals += new_pas_boal

ronaldo = Gamer(1, "Ronaldo", "Ricaro", "Brasil", "Динамо", "Нападающий", "Green", 23, 10, 10, 10, 100, 0)
ronaldo.Status("Red")
ronaldo.Status("Green")
ronaldo.Goals(200)
ronaldo.Games(10)
ronaldo.Seasons(5)




class Teams:

    def __init__(self, id, name, city, status, season, cnt_seasons, games, cnt_win, cnt_win_seasons, cnt_boals):
        self.id_team = id
        self.name = name # наименование команды
        self.city = city # город команды
        self.status = status # статус команды не Pass значит команда в сезоне, если pass сезон анлируется и команда дисквалифицирована
        self.season = season # Текущий сезон
        self.cnt_seasons = cnt_seasons # Количество сыигрианных сезонов
        self.games = games # Количество игр
        self.cnt_win = cnt_win # Количество выигранных игр
        self.cnt_win_seasons = cnt_win_seasons # Количество выигранных сезонов
        self.cnt_boals = cnt_boals # Общее количество забитых мечей командой
    
    def sum_season(self, season):
        self.cnt_seasons += season
    
    def sum_games(self, game):
        self.games += game
    
    def sum_win(self, win):
        self.cnt_win += win
    
    def sum_win_seasons(self, win_season):
        self.cnt_win_seasons += win_season
    
    def status_team(self, status):
        self.status = status
        if status == "Pass":
            self.cnt_seasons -= 1
        else:
            self.cnt_seasons += 1

dinamo = Teams(1, "Динамо", "Москва", "Active", 2020, 130, 872, 766, 98, 3333)
dinamo.status_team("Pass")
dinamo.status_team("Active")
dinamo.sum_season(10)
dinamo.sum_games(100)
dinamo.sum_win(90)
dinamo.sum_win_seasons(8)
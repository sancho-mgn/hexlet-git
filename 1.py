Задание 1. 
Программа Notepad++
Я бы создал класс:
1. Класс ввода_информации
В нём бы создал дочернии классы:
1.1. Синтаксис:
в нем следующие методы:
1.1.1 xml
1.1.2 json
1.1.3 text
1.1.4 html
1.1.5 python 
и другие. При применении этих методов к вводимому тексту - применяются правила реализованные в методах класса "Синтаксис"
1.2 Кодировка:
в нём следующие методы:
1.2.1 unicode
1.2.2 ansi
1.2.3 utf-8 
и другие. Эти методы применяются автоматически анализатором функии, также добавил бы методы преобразования текущей кодировки в другие
1.3 класс Вид:
в нем следующие методы:
1.3.1 масштаб текста
1.3.2 окно документа
1.3.3 перенос строк 
и другие. При примении этих методов к окну, применяются правила (увеличить масштаб окна, уменьшить шрифт и тд)
Программа Telegram
Создал бы классы:
1. Пользователь
От него дочении классы
1.1 Группы
1.2 Каналы
1.3 Контакты
1.4 Вызовы

Задание 2.
Игра футбол
import random

class Gamer:
    player_id = 0 # уникальный идентификатор игрока (счётчик)
    first_name = "Ivan" # Имя игрока
    second_name = "Ivanov" # Фамилия игрока
    national = "Rus" # Национальность игрока
    team = "Динамо" # Команда игрока
    status = "Защитник" # Нападающий, защитник, полузащитник, полунападающий, вратарь
    age = 18 # Возраст
    height = 180 # Рост игрока
    weight = 100 # Вес игрока
    cnt_play = 0 # Количество сыигранных игр
    cnt_seasons = 0 # Количество сыигранных сезонов
    cnt_goals = 0 # Количество забитых мячей
    cnt_bad_goals = 0 # Количество пропущенных мечей (для вратарей)
    
gamers = []
for i in range(22):
    gamer = Gamer()
    gamers.append(gamer)
    gamers[i].player_id = i    # задаём счётчик идентификатора каждого игрока
    gamers[i].age += i
    gamers[i].height -= i
    gamers[i].cnt_play = random.randint(1, 800)
    gamers[i].cnt_seasons = random.randint(1, 30)
    gamers[i].cnt_goals = random.randint(0, 1000)
    print(gamers[i].player_id, gamers[i].first_name, gamers[i].second_name, gamers[i].national, gamers[i].team, gamers[i].age, gamers[i].height, gamers[i].cnt_play, gamers[i].cnt_seasons, gamers[i].cnt_goals)

class Teams:
    id_team = 0
    name = "Динамо" # наименование команды
    city = "Москва" # город команды
    country = "Россия" # страна команды
    city_play = "" # город проведения игры
    season = 1900 # Текущий сезон
    cnt_seasons = 0 # Количество сыигрианных сезонов
    games = 0 # Количество игр
    cnt_win = 0 # Количество выигранных игр
    cnt_win_seasons = 0 # Количество выигранных сезонов
    cnt_goals = 0 # Общее количество забитых мечей командой
    cnt_goals_win = 0 # Общее количество забитых мечей во время игры
    player_id = 0 # Уникальный идентификатор игрока

teams = []
for i in range(30):
    team = Teams()
    teams.append(team)
    teams[i].id_team = i
    teams[i].cnt_win = random.randint(0, 1000) # количество выйгранных игр
    #print(teams[i].cnt_win)
    teams[i].cnt_seasons = random.randint(1,100) # количество сыигранных сезонов
    #print(teams[i].cnt_seasons)
    teams[i].games = random.randint(30,1000) # количество игр
    print(teams[i].id_team,teams[i].name, teams[i].cnt_win, teams[i].cnt_seasons, teams[i].games)


Задание 3.
gamers2 = gamers
print(gamers2 == gamers)

gamers = 0
print(gamers2 == gamers) # при изменении одной ссылки, вторая не меняется

gamers = gamers2
print(gamers2 == gamers)
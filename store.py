import re
from draft import Team

file = open('htm.txt', encoding='utf-8')
for line in file:
    game = re.split("[(\t\-)\n\xa0]+", line)
    game[1] = game[1].strip()
    game[2] = game[2].strip()
    game.remove('')
#    print(game)
#    break
    Team.meetings.append(game)
Team.meetings.reverse()

Wolfsburg = Team('Вольфсбург')
Cologne = Team('Кельн')
Leverkusen = Team('Байер Л')
Hannover = Team('Ганновер 96')
Hoffenheim = Team('Хоффенхайм')
Dortmund = Team('Боруссия Д')
Bayern_Munich = Team('Бавария')
Stuttgart = Team('Штуттгарт')
Schalke_04 = Team('Шальке 04')
Eintracht_Frankfurt = Team('Айнтрахт Фр')
Freiburg = Team('Фрайбург')
Augsburg = Team('Аугсбург')
Hertha = Team('Герта')
Leipzig = Team('Лейпциг')
Hamburg = Team('Гамбург')
M_gladbach = Team('Боруссия М')
Mainz_05 = Team('Майнц 05')
Werder_Bremen = Team('Вердер')

Team.teams.extend([Werder_Bremen, Wolfsburg, Cologne, Leverkusen, Hannover, Hoffenheim, Dortmund, Bayern_Munich, Mainz_05,
                   Stuttgart, Schalke_04, Eintracht_Frankfurt, Freiburg, Augsburg, Hertha, Leipzig, Hamburg, M_gladbach])

for each in Team.teams:
    for game in Team.meetings:
        if each.name == game[1] or each.name == game[2]:
            each.meetings.append(game)
print(M_gladbach.meetings)

print(Cologne.game_score())
print(Cologne.series_above(0.5, ">"))


"""
import shelve

db = shelve.open('storeDB')
for object in Team.teams:
    db[object.name] = object
db.close()
"""
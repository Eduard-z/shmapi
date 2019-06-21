import re
from draft import Team

list_of_champs = ['belarus', 'brazilA', 'brazilB', 'china', 'estonia', 'finland', 'finland2', 'iceland1',
                  'icelandP', 'indonesia', 'ireland1', 'irelandP', 'japan', 'japan2', 'kazahstan', 'koreaK', 'koreaKC',
                  'latvia', 'lithuania', 'malaysia', 'MLS', 'moldova', 'norway2', 'norwayP', 'singapur', 'sweden2',
                  'swedenP', 'thailand', 'vietnam']

for championship in list_of_champs:
    print('\n', file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))
    print(championship, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))
    path_to_results = r'C:\Users\Admin\Desktop\soccer\{champ}.txt'.format(champ=championship)
    file = open(path_to_results, encoding='utf-8')
    list_of_teams = set()
    for line in file:
        game = re.split("\t|\s\-\s|\W\(|\)|\n", line)
        game[1] = game[1].strip()
        game[2] = game[2].strip()
        game.remove('')
        # print(game)
        # break
        Team.meetings.append(game)
        list_of_teams.add(game[1])  # list of team names
    Team.meetings.reverse()

    print(list_of_teams)  # test
    list_of_objects = []  # list of object names
    for i in list_of_teams:
        temp = Team(i)
        list_of_objects.append(temp)
    Team.teams = list_of_objects

    for each in Team.teams:
        for game in Team.meetings:
            if each.name == game[1] or each.name == game[2]:
                each.meetings.append(game)
    print(Team.meetings)  # test

    # print(Dortmund.game_score())  # test
    for each in Team.teams:
        print(each.game_score())
        for indicator in ["self.scored", "self.scored1", "self.scored2", "self.conceded", "self.conceded1", "self.conceded2",
                          "total_first_half", "both_scored", "both_scored_second_half"]:
            # "both_scored_first_half", "total_second_half"
            for param in [0.5]:
                for above in [">", "<"]:
                    for place in ["all", "home", "away"]:
                        if len(each.series_above(indicator, param, above, place)) > 2:
                            print(each.series_above(indicator, param, above, place), each.name, indicator, above, param,
                                  place, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))

        for indicator in ["self.scored", "self.conceded", "total_first_half", "total_second_half"]:
            for param in [1.5]:
                for above in [">", "<"]:
                    for place in ["all", "home", "away"]:
                        if len(each.series_above(indicator, param, above, place)) > 2:
                            print(each.series_above(indicator, param, above, place), each.name, indicator, above, param,
                                  place, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))

        for indicator in ["total"]:
            for param in [1.5, 2.5, 3.5]:
                for above in [">", "<"]:
                    for place in ["all", "home", "away"]:
                        if len(each.series_above(indicator, param, above, place)) > 2:
                            print(each.series_above(indicator, param, above, place), each.name, indicator, above, param,
                                  place, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))

        for indicator in ["self.result"]:
            for param in [0.5, 1.5, -0.5, -1.5]:
                for above in [">", "<"]:
                    for place in ["all", "home", "away"]:
                        if len(each.series_above(indicator, param, above, place)) > 2:
                            print(each.series_above(indicator, param, above, place), each.name, indicator, above, param,
                                  place, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))

        for indicator in ["self.result_first_half", "self.result_second_half"]:
            for param in [0.5, -0.5]:
                for above in [">", "<"]:
                    for place in ["all", "home", "away"]:
                        if len(each.series_above(indicator, param, above, place)) > 2:
                            print(each.series_above(indicator, param, above, place), each.name, indicator, above, param,
                                  place, file=open(r'C:\Users\Admin\Desktop\test_belarus.txt', 'a', encoding='utf-8'))


"""
import shelve

db = shelve.open('storeDB')
for object in Team.teams:
    db[object.name] = object
db.close()
"""
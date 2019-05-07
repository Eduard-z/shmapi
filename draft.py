import time, datetime


class Result:
    def __init__(self, date, home, away, score):
        self.date = date
        self.home = home
        self.away = away
        self.score = score
        half1 = self.score.split()[1].strip('()')
        game = self.score.split()[0]
        half2 = str(int(game[0]) - int(half1[0])) + ':' + str(int(game[2]) - int(half1[2]))

        home.scored = game[0]
        home.scored1 = half1[0]
        home.scored2 = half2[0]
        away.scored = game[2]
        away.scored1 = half1[2]
        away.scored2 = half2[2]

        home.conceded = away.scored
        home.conceded1 = away.scored1
        home.conceded2 = away.scored2
        away.conceded = home.scored
        away.conceded1 = home.scored1
        away.conceded2 = home.scored2

        total = int(home.scored) + int(away.scored)
        total1 = int(home.scored1) + int(away.scored1)
        total2 = int(home.scored2) + int(away.scored2)

        result = int(home.scored) - int(away.scored)
        result1 = int(home.scored1) - int(away.scored1)
        result2 = int(home.scored2) - int(away.scored2)


class Team:
    champ = 'Bundesliga'
    country = 'Germany'
    year = '17/18'
    sport = 'soccer'
    meetings = []
    teams = []

    def __init__(self, name):
        self.name = name
        self.meetings = []
        self.score = ''
        self.result = []

    def game_score(self):
        for game in self.meetings:
            structed_time = time.strptime(game[0], "%d.%m.%y")
            matchday = datetime.date(structed_time.tm_year, structed_time.tm_mon, structed_time.tm_mday)
            home = game[1]
            away = game[2]
            total_score = game[3]
            first_half_score = game[4]
            second_half_score = str(int(total_score[0]) - int(first_half_score[0])) + \
                                ':' + str(int(total_score[2]) - int(first_half_score[2]))

            if self.name == home:
                self.place = "home"
                self.scored = total_score[0]
                self.scored1 = first_half_score[0]
                self.scored2 = second_half_score[0]

                self.conceded = total_score[2]
                self.conceded1 = first_half_score[2]
                self.conceded2 = second_half_score[2]

            if self.name == away:
                self.place = "away"
                self.scored = total_score[2]
                self.scored1 = first_half_score[2]
                self.scored2 = second_half_score[2]

                self.conceded = total_score[0]
                self.conceded1 = first_half_score[0]
                self.conceded2 = second_half_score[0]

            d1 = dict({"date": matchday, "home": home, "away": away, "total_score": total_score,
                       "first_half_score": first_half_score, "second_half_score": second_half_score,
                       "self.scored": self.scored, "self.scored1": self.scored1, "self.scored2": self.scored2,
                       "self.conceded": self.conceded, "self.conceded1": self.conceded1,
                       "self.conceded2": self.conceded2, "self.place": self.place
                       })
            self.result.append(d1)
        return self.result

    def series_above(self, param, above):
        count = 0
        self.series_list = []
        for game in self.result:
            if above == ">":
                if float(game["self.scored"]) > param:
                    count += 1
                    self.series_list.append('+')
                else:
                    # count = 0
                    self.series_list.append('-')
            elif above == "<":
                if float(game["self.scored"]) < param:
                    count += 1
                    self.series_list.append('+')
                else:
                    # count = 0
                    self.series_list.append('-')

        if len(self.series_list) - count < 2:
            return self.series_list, len(self.series_list), count
        else:
            return "cunt", count


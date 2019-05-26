import time, datetime


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
        self.game_result = []

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
            total = str(int(total_score[0]) + int(total_score[2]))
            total_first_half = str(int(first_half_score[0]) + int(first_half_score[2]))
            total_second_half = str(int(second_half_score[0]) + int(second_half_score[2]))
            both_scored = str(int(total_score[0]) * int(total_score[2]))
            both_scored_first_half = str(int(first_half_score[0]) * int(first_half_score[2]))
            both_scored_second_half = str(int(second_half_score[0]) * int(second_half_score[2]))

            if self.name == home:
                self.place = "home"
                self.result = str(int(total_score[0]) - int(total_score[2]))
                self.result_first_half = str(int(first_half_score[0]) - int(first_half_score[2]))
                self.result_second_half = str(int(second_half_score[0]) - int(second_half_score[2]))

            if self.name == away:
                self.place = "away"
                self.result = str(int(total_score[2]) - int(total_score[0]))
                self.result_first_half = str(int(first_half_score[2]) - int(first_half_score[0]))
                self.result_second_half = str(int(second_half_score[2]) - int(second_half_score[0]))

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
                       "self.conceded2": self.conceded2, "self.place": self.place, "total": total,
                       "total_first_half": total_first_half, "total_second_half": total_second_half,
                       "self.result": self.result, "self.result_first_half": self.result_first_half,
                       "self.result_second_half": self.result_second_half, "both_scored": both_scored,
                       "both_scored_first_half": both_scored_first_half,
                       "both_scored_second_half": both_scored_second_half
                       })
            self.game_result.append(d1)
        return self.game_result

    def series_above(self, indicator, param, above, place="all"):
        count = 0
        self.series_list = []
        for game in self.game_result:
            if place == "all":
                if above == ">":
                    if float(game[indicator]) > param:
                        count += 1
                        self.series_list.append('+')
                    else:
                        # count = 0
                        self.series_list.append('-')
                elif above == "<":
                    if float(game[indicator]) < param:
                        count += 1
                        self.series_list.append('+')
                    else:
                        # count = 0
                        self.series_list.append('-')
            elif place == "home":
                if above == ">":
                    if float(game[indicator]) > param and game["home"] == self.name:
                        count += 1
                        self.series_list.append('+')
                    elif float(game[indicator]) > param and game["home"] != self.name:
                        pass
                    elif float(game[indicator]) < param and game["home"] == self.name:
                        # count = 0
                        self.series_list.append('-')
                elif above == "<":
                    if float(game[indicator]) < param and game["home"] == self.name:
                        count += 1
                        self.series_list.append('+')
                    elif float(game[indicator]) < param and game["home"] != self.name:
                        pass
                    elif float(game[indicator]) > param and game["home"] == self.name:
                        # count = 0
                        self.series_list.append('-')
            elif place == "away":
                if above == ">":
                    if float(game[indicator]) > param and game["away"] == self.name:
                        count += 1
                        self.series_list.append('+')
                    elif float(game[indicator]) > param and game["away"] != self.name:
                        pass
                    elif float(game[indicator]) < param and game["away"] == self.name:
                        # count = 0
                        self.series_list.append('-')
                elif above == "<":
                    if float(game[indicator]) < param and game["away"] == self.name:
                        count += 1
                        self.series_list.append('+')
                    elif float(game[indicator]) < param and game["away"] != self.name:
                        pass
                    elif float(game[indicator]) > param and game["away"] == self.name:
                        # count = 0
                        self.series_list.append('-')

        if len(self.series_list) - count == 0:
            return "SERIES", self.series_list, len(self.series_list), count
        elif len(self.series_list) - count <= 2: #and self.series_list[-1] == "-":
            return "CUT_SERIES", self.series_list, len(self.series_list), count
        else:
            return "cunt", count


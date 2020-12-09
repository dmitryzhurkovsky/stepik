# Реализация сделана 2 способами: Первый с помощью словарей и функций, а второй с помощью классов.
# Реализация 1, вложенные словари и функции
# from collections import defaultdict
#
#
# def game(team1, team1_points, team2, team2_points):
#     def add_command_in_table(team1, team2, table):
#         if team1 not in table:
#             table[team1]['all_games'] = 0
#             table[team1]['victory'] = 0
#             table[team1]['draw'] = 0
#             table[team1]['loss'] = 0
#             table[team1]['points'] = 0
#
#         if team2 not in table:
#             table[team2]['all_games'] = 0
#             table[team2]['victory'] = 0
#             table[team2]['draw'] = 0
#             table[team2]['loss'] = 0
#             table[team2]['points'] = 0
#
#     def victory_team(team1, team1_points, team2, team2_points, table):
#         if int(team1_points) > int(team2_points):
#             table[team1]['victory'] += 1
#             table[team1]['points'] += 3
#             table[team2]['loss'] += 1
#         else:
#             table[team2]['victory'] += 1
#             table[team2]['points'] += 3
#             table[team1]['loss'] += 1
#
#     def draw(team1, team2, table):
#         table[team1]['draw'] += 1
#         table[team2]['draw'] += 1
#         table[team1]['points'] += 1
#         table[team2]['points'] += 1
#
#     add_command_in_table(team1, team2, table)
#     table[team1]['all_games'] += 1
#     table[team2]['all_games'] += 1
#     if team1_points == team2_points:
#         draw(team1, team2, table)
#     else:
#         victory_team(team1, team1_points, team2, team2_points, table)
#
#
# n = int(input())
# games = [input().split(';') for i in range(n)]
# table = defaultdict(dict)    # lambda: defaultdict(int)) - можно передать, и будет вложенный словарь, в словаре
#
#
# for team_pairs in games:
#     game(*team_pairs)
#
# for team_name in table:
#     print(team_name + ':', end ='')
#     for value in table[team_name].values():
#         print(value, end=' ')
#     print()


# Реализация 2, классы и методы
class Team:
    def __init__(self, name):
        self.team_name = name
        self.all_games = 0
        self.wins = 0
        self.draw = 0
        self.losess = 0
        self.points = 0

    def __str__(self):
        return f'{self.team_name}: {self.all_games} {self.wins} {self.draw} {self.losess} {self.points}'

    def __repr__(self):
        return f'Team(\'{self.team_name}\')'

    def add_wins(self):
        self.wins += 1
        self.points += 3
        self.all_games += 1

    def add_draw(self):
        self.draw += 1
        self.points += 1
        self.all_games += 1

    def add_lose(self):
        self.losess += 1
        self.all_games += 1


table = {}
for team_pairs in range(int(input())):
    team1, team1_points, team2, team2_points = input().split(';')
    for command in (team1, team2):
        if command not in table:
            table.update({command: Team(command)})
    if int(team1_points) > int(team2_points):
        table[team1].add_wins()
        table[team2].add_lose()
    elif int(team1_points) == int(team2_points):
        table[team1].add_draw()
        table[team2].add_draw()
    else:
        table[team2].add_wins()
        table[team1].add_lose()

for team in table.values():
    print(team)





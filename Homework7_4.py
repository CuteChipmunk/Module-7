team1 = 'Masters of code'
team2 = 'Vizards of information'
score1 = 0
score2 = 0

def num(team1_num = 0, team2_num = 0):
    print('В команде %s участников: %s !' % (team1, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

def time(team1_time = 0, team2_time = 0, tasks=0):
    time1 = team1_time
    time2 = team2_time
    print('Команда {} решила задач: {}!'.format(team2, score2))
    print('{} решили задачи за {} cек. !'.format(team2, time2))
    print(f'Команды решили {score1} и {score2} задач')

def test(tasks = 0, all_time = 0):
    if score1 > score2:
        print(f'Результат битвы: победа команды {team1} !')
    else:
        print(f'Результат битвы: победа команды {team2} !')
    print(f'Сегодня было решено {tasks} задач, в среднем по {all_time} секунды на задачу')

# team1_num = 5
# team2_num = 6
# score_1 = 40
# score_2 = 42
# team1_time = 1552.512
# team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

num(5,6)
score1 = 40
score2 = 42
time(1552.512, 2153.31451)
test(82,45.2)
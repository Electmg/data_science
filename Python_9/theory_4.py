# Задание 4.3
from collections import deque

def brackets(line):
    lines = deque()
    for i in line:
        if i == "(" :
            lines.append(i)
        elif i == ")" :
            if len(lines) == 0:
                return False
            lines.pop()
    return True if len(lines) == 0 else False
#print(brackets("(()())"))
#print(brackets(""))
#print(brackets("(()()))"))

# Задание 4.4

north_new = list()
for row in north:
    for elem in row:
        north_new.append(elem)
print("north:", len(north_new))

center_new = list()
for row in center:
    for elem in row:
        center_new.append(elem)
print("center:", len(center_new))

south_new = list()
for row in south:
    for elem in row:
        south_new.append(elem)
print("south:", len(south_new))
# ИЛИ
north_list = [elem for bill in north for elem in bill]
south_list = [elem for bill in south for elem in bill]
center_list = [elem for bill in center for elem in bill]
print(len(north_list))
print(len(south_list))
print(len(center_list))

# Задание 4.5
from collections import Counter

north_new = Counter(north_new)
center_new = Counter(center_new)
south_new = Counter(south_new)
print(north_new.most_common()[-1])# Находим наименьшее значение в Counter

# Задание 4.6
print(center_new - north_new)

# Задание 4.7
print(south_new - (center_new + north_new))
print(north_new - (center_new + south_new))
print(center_new - (south_new + north_new))

# Задание 4.8
print((center_new + north_new + south_new).most_common(2))

# Задание 4.9
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

ratings.sort(key= lambda x: (-x[1], x[0]))
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict

cafes = OrderedDict(ratings)

# Задание 4.10 
#Напишите функцию task_manager, которая принимает список задач для нескольких серверов. Каждый элемент списка состоит из кортежа (<номер задачи>, \
    # <название сервера>, <высокий приоритет задачи>).
#Функция должна создавать словарь и заполнять его задачами по следующему принципу: название сервера — ключ, по которому хранится очередь задач для \
    # конкретного сервера. Если поступает задача без высокого приоритета (последний элемент кортежа — False), добавить номер задачи в конец очереди. Если приоритет высокий, добавить номер в начало.
#Для словаря используйте defaultdict, для очереди — deque.

from collections import defaultdict 
from collections import deque

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1] is True:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))
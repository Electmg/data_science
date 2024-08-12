#ORDEREDDICT
from collections import OrderedDict
#data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
#ordered_client_ages = OrderedDict(data)
#print(ordered_client_ages)

#Можно, например, отсортировать с помощью функции sorted список кортежей при создании из него OrderedDict, и объекты будут добавлены в порядке сортировки:

# Сортируем по второму значению из кортежа, то есть по возрасту
#ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
#print(ordered_client_ages)

#Если удалить элемент, а затем добавить его снова, он также окажется в конце:

del ordered_client_ages['Andrey']
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])
#ordered_client_ages['Andrey'] = 23

#DEQUE
from collections import deque
clients = deque()
#Добавим несколько человек в очередь с помощью append:
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
#Объект deque поддерживает индексацию по элементам:
#print(clients[2])

# Освободилось два оператора — заберём двоих человек из начала очереди с помощью popleft:
first_client = clients.popleft()
second_client = clients.popleft()

#добавить элемент в начало очереди с помощью appendleft:
clients.appendleft('Vip-client')

#Добавить сразу несколько элементов из итерируемого объекта в дек. Для этого используют функции extend 
# shop = deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
# Добавить их в начало той же очереди с помощью extendleft:
shop.extendleft([11, 12, 13, 14, 15, 16, 17])

#ОЧЕРЕДЬ С ОГРАНИЧЕННОЙ МАКСИМАЛЬНОЙ ДЛИНОЙ
# в очереди с ограниченной длиной сохраняются только последние элементы, а первые исчезают из памяти:
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)

#Посчитаем динамику средней температуры с усреднением за каждые последние 7 дней
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
        
#reverse позволяет поменять порядок элементов в очереди на обратный:
dq = deque([1,2,3,4,5])
dq.reverse()
print(dq)

#rotate переносит  заданных элементов из конца очереди в начало:
dq = deque([1,2,3,4,5])
dq.rotate(2)
print(dq)
#ИЛИ
dq.rotate(-2)
print(dq)

#Функция index позволяет найти первый индекс искомого элемента, а count позволяет подсчитать, сколько раз элемент встретился в очереди (функции аналогичны одноимённым функциям для списков):
dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(4))
# 2
print(dq.count(4))
# 6


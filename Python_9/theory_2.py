from collections import Counter
#c = Counter()
#c ["Red"] += 1


#cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
#c = Counter()
#for car in cars:
    #c[car] += 1
 # ИЛИ
#c = Counter(cars)

#print(c['black'])
#print(sum(c.values()))

#ОПЕРАЦИИ С COUNTER
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

# Сложение словарей
#print(counter_moscow + counter_spb)

# Вычитание словарей(При использовании "-" отрицательные значения не возможны)
#counter_moscow.subtract(counter_spb)
#print(counter_moscow)

#1. Чтобы получить список всех элементов, которые содержатся в Counter, используется функция elements(). \
    # Она возвращает итератор, поэтому, чтобы напечатать все элементы, распакуем их с помощью *:
#print(*counter_moscow.elements())

#2. Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():
#print(list(counter_moscow))

# 3. С помощью функции dict() можно превратить Counter в обычный словарь:
#print(dict(counter_moscow))

# 4. Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
#print(counter_moscow.most_common())
# ИЛИ можно передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2:
#print(counter_moscow.most_common(2))

# 5. Наконец, функция clear() позволяет полностью обнулить счётчик:
#counter_moscow.clear()

# Задание 2.3
#print(c.most_common(1))

# Задание 2.4
#print(c[953421102])

# Задание 2.5
#from hidden import clients
#from collections import Counter
#c = Counter(clients)
#print(len(list(c)))

# DEFAULTDICT
# Обычный способ
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
#groups = dict()
 
#for student, group in students:
    # Проверяем, есть ли уже эта группа в словаре
    #if group not in groups:
        # Если группы ещё нет в словаре, создаём для неё пустой список
        #groups[group] = list()
    #groups[group].append(student)
 
#ИЛИ Через DEFAULTDICT:
#from collections import defaultdict

#groups = defaultdict(list)
#for student, group in students:
    #groups[group].append(student)
#print(groups)
#print(type(groups))
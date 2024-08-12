import numpy as np

#Итак, обобщим. Чтобы узнать максимальное целое положительное число, которое можно уместить в  бит, необходимо воспользоваться следующей формулой:
2**n - 1

n_max = (2**n)/2 - 1
n_max = -(2**n)/2
#ЦЕЛОЧИСЛЕННЫЕ ТИПЫ ДАННЫХ В NUMPY
#a = np.int8(25)

#Чтобы узнать границы int, можно воспользоваться функцией np.iinfo (int info):
#print(np.iinfo(np.int8))
#ИЛИ
#np.iinfo(a)

#В NumPy доступны и беззнаковые целочисленные типы данных. Они имеют корень uint (unsigned int — беззнаковое целое).
#b = np.uint8(124)
#print(b)
#np.iinfo(b)

#Если операция проводится с двумя NumPy-типами с фиксированным объёмом памяти, в результате сохраняется наиболее «старший» тип:
#a = np.int32(1000)
#b = np.int8(25)
#c = a + b
#print(c)

#ТИПЫ ДАННЫХ С ПЛАВАЮЩЕЙ ТОЧКОЙ В NUMPY
#np.finfo(np.float16)

#ДОПОЛНИТЕЛЬНЫЕ ТИПЫ ДАННЫХ В NUMPY
#Полный список (а точнее, словарь) типов данных в NumPy можно получить с помощью атрибута sctypeDict
#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

#Следует обратить внимание на типы данных bool_ и str_
#a = np.bool(a)
#print(type(a))
# <class 'bool'>
#a = np.bool_(a)
#print(type(a))
# <class 'numpy.bool_'>
 
# Значения равны
#print(np.bool(True) == np.bool_(True))
# True
# А типы — нет:
#print(type(np.bool(True)) == type(np.bool_(True)))
# False

#Пример со str:
#a = "Hello world!"
#a = np.str_(a)
#print(type(a))
# <class 'numpy.str_'>

#Задание
a = np.uint8(-456)
print(a)
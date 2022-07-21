#СОЗДАНИЕ МАССИВА ИЗ СПИСКА
import numpy as np

#arr = np.array([1,5,2,9,10])
#print(type(arr))
# <class 'numpy.ndarray'>
#Название ndarray — это сокращение от n-dimensional array, -мерный массив.

#Задать тип данных сразу при создании массива можно с помощью параметра dtype:
#arr = np.array([1,5,2,9,10], dtype=np.int8)
#arr[2] = 2000
#print(arr)

#np.finfo(np.float16)
#print(np.finfo(np.float32))

#Задание 6.3
#a = np.float32(-1000)
#print(a)

#СВОЙСТВА NUMPY-МАССИВОВ
#arr = np.array([1,5,2,9,10], dtype=np.int8)
#nd_arr = np.array([
               #[12, 45, 78],
               #[34, 56, 13],
               #[12, 98, 76]
               #], dtype=np.int16)

# 1. Узнать размерность массива можно с помощью .ndim:
#arr.ndim
# 1
#nd_arr.ndim
# 2

# 2. Узнать общее число элементов в массиве можно с помощью .size:
#arr.size
# 5
#nd_arr.size
# 9

# 3. Форма или структура массива хранится в атрибуте .shape:
#arr.shape
# (5,)
#nd_arr.shape
# (3, 3)

# 4. Наконец, узнать, сколько «весит» каждый элемент массива в байтах позволяет .itemsize:
#arr.itemsize
# 1
#nd_arr.itemsize
# 2

#ЗАПОЛНЕНИЕ НОВЫХ МАССИВОВ
#zeros_1d = np.zeros(5)
#print(zeros_1d)
#Создадим трёхмерный массив с формой 5x4x3 и типом float32:
#zeros_3d = np.zeros((5,4,3), dtype=np.float32)
#print(zeros_3d.shape)

#Ещё одной удобной функцией для создания одномерных массивов является arange. Она аналогична встроенной функции range, но обладает рядом особенностей.\
    # Вот её сигнатура: arange([start,] stop, [step,], dtype=None).
#np.arange(2.5, 5, 0.5, dtype=np.float16)

#для работы с дробными параметрами start, stop и step лучше использовать функцию linspace 
#arr = np.linspace(1, 2, 10)
#arr = np.linspace(1, 5, 10, endpoint=False)

#Задание 6.6-7 С каким шагом сгенерируется массив из 60 чисел от -6 до 21 включительно и невключительно?
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)

# Задание 6.8
#print(mystery.ndim)

# Задание 6.9 Какова максимальная протяжённость по одной из осей массива?
#print(mystery.shape)

# Задание 6.10 Узнайте число элементов массива.
#print(mystery.size)

# Задание 6.11 Какой тип данных у элементов массива?
#print(mystery.dtype)

# Задание 6.12 Узнайте вес всех элементов в массиве в байтах.
#print(mystery.itemsize * mystery.size)
import numpy as np
# Задание 7.2
try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery
# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]
# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]
# В переменную line_4 сохраните строку 4
line_4 = mystery[3, :]
# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:,-2]
# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно) Результат сохраните в переменную part
part = mystery[1:4,2:5]
#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[:, -1]
rev = rev[::-1]
# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()

# Задание 7.5
try:
    from Root.src.hidden import mystery
except ImportError:
    from hidden import mystery
import numpy as np
# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)

# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)

# Заполните пропущенные значения в массиве mystery нулями
mystery[np.isnan(mystery)] = 0

# Поменяйте тип данных в массиве mystery на int32
mystery = np.int32(mystery)

# Отсортируйте значения в массиве по возрастанию и сохраните. результат в переменную array
array = np.sort(mystery)

# Сохраните в массив table двухмерный массив, полученный из массива array. В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3), order = "F")

#  Сохраните в переменную col средний столбец из table
col = table[:, 1]
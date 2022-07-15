"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int=1) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    n_min = 1
    n_max = 101
    pred_number = 0
    count = 0
    
    while True:
        count += 1
        if pred_number < number:
            n_min = pred_number
            pred_number = round((n_min+n_max) / 2)
        elif pred_number > number:
            n_max = pred_number
            pred_number = round((n_min+n_max) / 2)
        else:
            break
        
    return count    
   
   
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'ваш алгоритм угадывает в среднем за: {score} попыток')
    return(score)  

print(f'количество попыток: {random_predict(10)}')

score_game(random_predict)
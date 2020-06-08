#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом делим интервал пополам в зависимости от того, 
        больше оно или меньше нужного. 
        Функция принимает загаданное число и возвращает число попыток'''    
    count = 0        
    start = 1
    finish = 100    
    predict = np.random.randint(1,101) #          
    while number != predict:         
        count +=1        
        if number > predict:             
            start = predict + 1 # так как граница уже проверена увеличиваем ее          
        elif number < predict:                         
            finish = predict - 1 # так как граница проверена уменьшаем ее
        predict = (start+finish)//2 #Для ускорения делим интервал пополам
        
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    #Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(100))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)

score_game(game_core_v2)


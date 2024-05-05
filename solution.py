import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1

    table = [[x_success, (x_cnt - x_success)],
             [y_success, (y_cnt - y_success)]]
    
    res = sps.fisher_exact(table, alternative='less')

    do_reject = (res[1] < alpha)
    return do_reject # Ваш ответ, True или False

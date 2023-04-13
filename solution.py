import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu


chat_id = 5437824033   # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.02
    stat, p = mannwhitneyu(x, y, alternative='greater')
    
    if p < alpha:
        return True
    else:
        return False

import random
from functools import reduce
import numpy as np

prices = list(range(1, 100))
random.shuffle(prices)

# min_right_to_left = np.zeros(len(prices), dtype=int)

# prices_np = np.array(prices)
# min_so_far = np.full(len(prices), float('inf')) 

# # for i in range(len(prices) - 1, -1, -1):
# #     min_so_far = min(prices[i], min_so_far)
# #     min_right_to_left[i] = min_so_far

# min_right_to_left = np.full(len(prices), np.min(prices_np, min_so_far)) 


#print(min_right_to_left)


def find_max_down_fall(prices):
    min_right_to_left = [0 for i in range((len(prices)))]

    min_so_far = float('inf')
    for i in range(len(prices) - 1, -1, -1):
        min_so_far = min(prices[i], min_so_far)
        min_right_to_left[i] = min_so_far

    res = 0
    for i, buy in enumerate(prices):
        worst_sell = min_right_to_left[i]
        down_fall = (buy - worst_sell) / buy
        res = max(res, down_fall)

    return res


def find_max_down_fall_np(prices_np):
    min_right_to_left = np.zeros(len(prices_np), dtype=int)
    
    min_so_far = float('inf')
    
    min_right_to_left = 
    
    res = 0

    res = np.max(1 - prices_np / min_right_to_left)

    return res


prices_np = np.array(prices)
print(find_max_down_fall(prices))
print(find_max_down_fall_np(prices_np))
print(find_max_down_fall(prices) == find_max_down_fall_np(prices_np))

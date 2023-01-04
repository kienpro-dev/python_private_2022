import math

def sumDiv(n):
    return sum([i for i in range(math.sqrt(n)) if n % i == 0])


list_n = list(map(int, input().split()))
    
list_res = []
list_res.append(i for i in list_n if sumDiv(i) == 3)

print(len(list_res))
    
    
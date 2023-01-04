def sumDiv(n):
    return sum([i for i in range(2,n) if n % i == 0])

list_n = list(map(int, input().split()))

list_res = []
for i in list_n:
    if sumDiv(i) > i :
        list_res.append(i)

print(len(list_res))
list_res.sort(reverse=True)
print(list_res)

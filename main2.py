# # slicing trong String:
# #     <tenbien> [start:end:step]
# s= "hello"
# print(s[0:4:2])

# #split(): chia chuoi
# s=list(map(int, input().split())) # -> nhap 1 list so nguyen
# print(s)

# #join() noi chuoi 
# a = "-".join(['1','2','3','4'])
# print(a)

# # list
# fruits = ["apple", "banana", "guava"]
# fruits.pop(2)
# del fruits[0]
# fruits.remove("banana")
# print(fruits)

# a = ['1',2,3,[2,4],5.5]
# a[:0] = [10] #chen dau
# a[2:2] = [1,1] #chen vi chi co chi so 2
# a[len(a):] = [100] #chen cuoi
# a[1:3] = [] # xoa list chi so 1 den nho hon 3

# print(a)

# a = 9999999999999999999999999999999999999999999999999999999999999999999999
# print(a)

a = {2,5,6,4,5}
a.pop()
print(a)
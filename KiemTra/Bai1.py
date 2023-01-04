a = input()
b = input()

cnt = 0

for i in range(len(b)):
    if b[i:len(a) + i] == a:
        cnt += 1
        
print(cnt)
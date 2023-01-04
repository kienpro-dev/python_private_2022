def dem(s):
    res = ""
    cnt = 1
    for i in range(1,len(s)):
        if s[i] != s[i - 1] or i != len(s):
            res+=s[i] + str(cnt)
            cnt=1
        else:
            cnt+=1
        res+=s[i] + str(cnt)
    return cnt
            

s = input()
n = int(input())

for i in range(n):
    strr = dem(s)
    print(strr)
    
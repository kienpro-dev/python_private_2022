for _ in range(int(input())):
    s = input()
    print(s + s[::-1])

for _ in range((int)(input())):
    k = (int)(input())
    if k % 2:
        print(*([1] * k))
    else:
        print(*([2] * (k - 2) + [1, 3]))
    print()

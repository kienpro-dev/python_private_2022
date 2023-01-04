def sum1(a, b, c):
    return a + b + c


def sum2(*num):  # nhận 1 tuple truyền bao nhiêu đối số cũng đc
    return sum(num)

# def sum3(**name): nhận 1 dictionary


def tinhNo(notien, lai, **s):
    no = notien+lai
    if ('tra' in s.keys()):
        no -= s['tra']
    return no


def tinhToan(a, b, *s):

    return a + b, a - b, a / b, a * b  # khi trả về nhiều giá trị thì ném vào tuple


print(sum1(a=1, c=2, b=3))
print(sum2(1, 2, 3, 4, 5))

kien = tinhNo(500, 100)
kien = tinhNo(500, 100, tra=200)

print(kien)

print(tinhToan(4, 5))

a = tinhToan

# biến cục bộ, toàn cục
# khi dùng biến toàn cục cần khai báo global và nonglobal

class Car:
    def __init__(self, name):
        self.name = name
        
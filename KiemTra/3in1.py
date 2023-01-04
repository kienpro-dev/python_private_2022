from multimethod import *


class Matrix:
    @multimethod
    def __init__(self, row: int, col: int, val=0):
        self._row = row
        self._col = col
        self._matrix = [[val for j in range(self._col)]
                        for i in range(self._row)]

    @__init__.register
    def __init__(self, matr: list):
        self._matrix = matr.copy()
        self._row = len(self._matrix)
        self._col = len(self._matrix[0])

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self._matrix)

    def __add__(self, other):
        if self.shape() != other.shape():
            raise Exception("Cannot add to matrix with different shape")
        add = Matrix(self._row, self._col)
        for i in range(self._row):
            for j in range(self._col):
                add._matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return add

    def __sub__(self, other):
        if self.shape() != other.shape():
            raise Exception("Cannot sub to matrix with different shape")
        sub = Matrix(self._row, self._col)
        for i in range(self._row):
            for j in range(self._col):
                sub._matrix[i][j] = self._matrix[i][j] - other._matrix[i][j]
        return sub

    def __pow__(self, other: int):
        if other < 0:
            raise Exception("Don't accept negative numbers")
        poww = Matrix(self._row, self._col)
        for i in range(self._row):
            for j in range(self._col):
                poww._matrix[i][j] = self._matrix[i][j] ** other
        return poww

    def __mul__(self, other):
        this_row, this_col = self.shape()
        other_row, other_col = other.shape()
        if this_col != other_row:
            raise Exception("Cannot multiply matrix with this shape")
        mul = Matrix(this_row, other_col)
        for i in range(this_row):
            for j in range(other_col):
                for k in range(this_row):
                    mul._matrix[i][j] += self._matrix[i][k] * \
                        other._matrix[k][j]
        return mul

    def shape(self):
        return (self._row, self._col)

    def input(self):
        self._matrix = [[int(input()) for j in range(self._col)]
                        for i in range(self._row)]


def convert(s):
    l = []
    for c in s:
        if c >= '0' and c <= '9':
            l.append(int(c))
    return l


n = int(input())
m = int(input())

list_n = []
for i in range(n):
    l = convert(input())
    list_n.append(l)

list_m = []
for j in range(m):
    l = convert(input())
    list_m.append(l)


matr_n = Matrix(list_n)
matr_m = Matrix(list_m)

print(matr_n + matr_m)
print(matr_n - matr_m)
print(matr_n ** 2)
print(matr_n * matr_m)

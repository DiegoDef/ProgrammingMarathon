"""
1 |__|__|__|__|__|__|__|__|
2 |__|__|__|__|__|__|__|__|
3 |__|__|__|__|__|__|__|__|
4 |__|__|__|X |__|__|__|__|
5 |__|__|__|__|__|__|__|__|
6 |__|__|__|__|__|__|__|__|
7 |__|__|__|__|__|__|__|__|
8 |__|__|__|__|__|__|__|__|
   1, 2, 3, 4, 5, 6, 7, 8
"""
def diagonal(inicio):
    x1, y1, x2, y2 = inicio
    while x1 < 9 and y1 < 9:
        x1 += 1
        y1 += 1
        if x1 == x2 and y1 == y2:
            return True
    x1, y1, x2, y2 = inicio
    while x1 > 0 and y1 < 9:
        x1 -= 1
        y1 += 1
        if x1 == x2 and y1 == y2:
            return True
    x1, y1, x2, y2 = inicio
    while x1 < 9 and y1 > 0:
        x1 += 1
        y1 -= 1
        if x1 == x2 and y1 == y2:
            return True
    x1, y1, x2, y2 = inicio
    while x1 < 9 and y1 > 0:
        x1 -= 1
        y1 -= 1
        if x1 == x2 and y1 == y2:
            return True


while sum((inicio := list(map(int, input().split())))) != 0:
    x1, y1, x2, y2 = inicio
    a = x1 == x2
    b = y1 == y2
    if a and b:
        print("0")
    elif a or b or diagonal(inicio):
        print("1")
    else:
        print("2")

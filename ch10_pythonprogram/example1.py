# -*- coding: utf-8 -*-
def gugudan(n):
    result = []
    for k in range(1, 9):
        result.append(k*n)

    print(result)

# 이 위치에 코드를 작성한다.


print(gugudan(2))
print(gugudan(3))
print(gugudan(4))
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[3, 6, 9, 12, 15, 18, 21, 24, 27]
[4, 8, 12, 16, 20, 24, 28, 32, 36]
'''

# -*- coding: utf-8 -*-
# 게시판 페이징하기
import math


def getTotalPage(m, n):
    return math.ceil(m/n)

    # 이 위치에 코드를 작성한다.
print(getTotalPage(5, 10))  # 1
print(getTotalPage(15, 10))  # 2
print(getTotalPage(30, 10))  # 3

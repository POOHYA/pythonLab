#   변수의 범위 : 함수 안에서 정의한 변수는 함수 안에서만 사용할 수 있다.
a = 5


def func1():
    a = 1
    print("[func1] 지역변수 a=", a)


func1()

print(a)

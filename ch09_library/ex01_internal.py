#   내장함수
#   abs(x)는 절대값
#   all()
#   any()
#   chr(i)
print(chr(65))  # A
print(chr(44032))

#   dir은 객체가 자체적으로 가지고 있는 변수와 함수를 보여준다.
print(dir([1, 2, 3]))  # 리스트 객체

print(dir({'1': 'a'}))  # 딕셔러리 객체

# divmod은 몫과 나머지를 튜플 형태로 리턴하는 함수이다.
print(divmod(7, 3))
# (2, 1)
print(7/3)
print(int(7/3))  # 몫
print(7 % 3)  # 나머지

# enumerate 함수는 순서가 있는 자료형(리스트,튜플,문자열)을 입력을 받아
# 인덱스 값을 포함하는 enumerate 객체로 리턴한다.
i = 0
for name in ['body', 'foo', 'bar']:
    i += 1  # i = i + 1
    print(i-1, name)
'''
0 body
1 foo
2 bar
'''
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''

# eval(expression)은 실행 가능한 문자열을 입력으로 받아
# 문자열을 실행한 결과값으로 리턴하는 함수이다.
print("1+2")  # '1+2'
print(eval("1+2"))  # '3'

print("'hi'+'a'")  # 'hi'+'a'
print(eval("'hi'+'a'"))  # 'hia'

print('divmod(4,3)')  # divmod(4,3)
print(eval('divmod(4,3)'))  # (1, 1)


# filter 함수는 첫번째 인수로 함수이름을, 두번째 인수로 그 함수에 차례로
# 들어갈 반복 가능한 자료형을 받는다.

def positive(l):  # l = [1,-2,-3,4,-5]
    result = []  # 리스트 result = [1,4]

    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive([1, -2, -3, 4, -5]))
# [1, 4]


def positive1(x):
    return x > 0  # True or False


print(list(filter(positive1, [1, -2, -3, 4, -5])))
# [1, 4]

# lambda는 익명함수를 만드는 식.
print(list(filter(lambda x: x > 0, [1, -2, -3, 4, -5])))
# [1, 4]


# [과제] Q4 filter와 lambda를 사용하여 아래 리스트에서 홀수를 모두 제거해 보자.
# [1,-2,3,-5,8,-3] -> [-2,8]
print(list(filter(lambda x: x % 2 == 0, [1, -2, 3, -5, 8, -3])))
# [-2, 8]
# hex(x)는 정수값을 입력받아 16진수(hexadecimal)로 변환하여 리턴하는 함수
print(hex(234))
# 0xea
print(hex(16))
# 0x10
print(hex(3))

#   유용한 내장 함수
#   형 변환 함수
#   정수형으로 변환
print([int(0.123), int(3.5123345), int(-1.312346)])
#   [0,3,-1]

#   실수형으로 변환
print([float(123), str(45678), str(-87)])
#   [123.0, '45678', '-87']

#   리스트, 튜플, 세트형으로변환
list_data = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data = {'abc', 1, 2, 'def'}

print([type(list_data), type(tuple_data), type(set_data)])

print("리스트로 변환: ", list(tuple_data), list(set_data))
print("튜플로 변환: ", tuple(list_data), tuple(set_data))
print("세트로 변환: ", set(list_data), set(tuple_data))

#   bool 함수
#   숫자를 인자로 bool 함수 호출
print(bool(0))
print(bool(1))
print(bool(-10))

#   문자열을 인자로 bool 함수 호출
print(bool('a'))
print(bool(' '))
print(bool(' '))
print(bool(None))

#   리스트, 튜플, 세트를 인자로 bool 함수 호출
myFriends = []
print(bool(myFriends))  # False

myFriends = ['James', 'Robert']
print(bool(myFriends))  # True

myNum = ()
print(bool(myNum))  # False

mySetA = {}
print(bool(mySetA))  # False

#   bool 함수의 활용


def print_name(name):
    if bool(name):
        print("입력된 이름:", name)
    else:
        print("입력된 이름이 없습니다,")


print_name("James")
print_name("")


#   최솟값과 최댓값을 구하는 함수
myNum = [10, 5, 12, 0, 3.5, 99.5, 42]
print([min(myNum), max(myNum)])

myStr = 'zxyabc'
print([min(myStr), max(myStr)])

#   절대값과 전체 합을 구하는 함수
print([abs(10), abs(-10)])  # 절대값
sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(sumList))

#   항목의 갯수를 구하는 함수
print(len("ab cd"))
print(len(([1, 2, 3, 4, 5, 6, 7, 8])))
print(len({1: "Thomas", 2: "Edward", 3: "Henry"}))

#   내장 함수의 활용
scores = [90, 80, 95, 85]

score_sum = 0
subject_num = 0
for score in scores:
    score_sum += score
    subject_num += 1

average = score_sum / subject_num
print("총점:{0}, 평균: {1}".format(score_sum, average))

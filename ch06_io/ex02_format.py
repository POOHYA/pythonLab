#   형식 지정 출력
#   나머지 연산자(%)를 이용한 형식 및 위치 지정
#   형식: print("%type" %data)
#          print("%type %type" %data %data)

name = "광제"
print("%s는 나의 친구입니다" %name)

r = 3
PI = 3.141592
print("반지름: %d, 원주율: %f" %(r,PI))

#   형식 지정 문자열에서 출력 위치 지정
#   형식: print("{0}")
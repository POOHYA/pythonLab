#   Q1 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 3과 6을 입력했을 때 9가 아닌 36이라는 결과값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))
total = input1 + input2
print("두 수의 합은 %d 입니다." %total)
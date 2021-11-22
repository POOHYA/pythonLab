#   Q1 다음과 같이 동작하는 클래스 Calculator를 작성해 보자.
class Calculator():
    #   초기화 메소드(인스턴스 메소드)
    def __init__(self, numList):
        self.numList = numList

    def sum(self):
        sumresult = 0
        for num in self.numList:
            sumresult += num
        return sumresult

    def avg(self):
        avgresult = sum(self.numList)/len(self.numList)
        return avgresult


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
# 15
print(cal1.avg())
# 3.0
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
# 40
print(cal2.avg())
# 8.0

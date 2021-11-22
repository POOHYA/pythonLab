#   클래스 상속
#   형식: class 자식클래스명(부모클래스명):
#        <코드 블록>

class Bicycle():
    #   초기화 함수(인스턴스 메소드)
    def __init__(self, wheel_size, color):
        #   인스턴스 변수
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거: 시속 {0}회전".format(direction))

    def stop(self):
        print("자전거 ({0},{1}): 정지".format(self.wheel_size, self.color))


class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state):
        super().__init__(wheel_size, color)
        self.state = staticmethod

    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state = {0}".format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state = {0}".format(self.state))


#   객체 생성
folding_bicycle = FoldingBicycle(27, 'white', 'unfolding')
folding_bicycle.move(2)
folding_bicycle.fold()
folding_bicycle.unfold()

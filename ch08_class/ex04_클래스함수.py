#   인스턴스 메소드:
# - 각 객체에서 개별적으로 동작하는 함수
# - 첫 인자로 self가 필요함

class Car():
    #   클래스 변수
    instance_count = 0

    #   초기화 함수(인스턴스 메소드)
    def __init__(self, size, color):
        #   인스턴스 변수
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1
        print("자동차 객체의 수: {0}".format(Car.instance_count))

    #   1.인스턴스 메소드
    # - 각 객체에서 개별적으로 동작하는 함수
    # - 첫 인자로 self가 필요함
    def move(self, speed):
        self.speed = speed
        print("자동차({0} {1})가".format(self.size, self.color), end='')
        print("시속 {0}킬로미터로 전진".format(self.speed))

    #   2.정적 메소드
    # - 클래스나 클래스의 인스턴스(객체)와는 무관하게 독립적으로 동작하는 함수
    # - 인자로 self를 사용하지 않으며 인스턴스 메서드나 인스턴스 변수에 접근할 수 없다.
    # - @staticmethod 데코레이터로 선언
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동하는 전기차입니다.")
        elif(10 <= model_code < 20):
            print("이 자동차는 가솔린차입니다")
        else:
            print("이 자동차는 디젤차입니다")

    #   3. 클래스 메소드
    # - 클래스 변수를 사용하기 위한 함수
    # - 인자로 cls가 필요하다.
    # - @classmothod 데코레이터로 선언
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {0}".format(cls.instance_count))


car1 = Car("small", "red")
car2 = Car("big", "green")

car1.move(80)
car2.move(100)


#   정적 메소드
# - 클래스나 클래스의 인스턴스와는 무관하게 독립적으로 동작하는 함수
# - self를 사용하지 않으면 정적 메소드 안에서는 인스턴스 메소드나 인스턴스 변수를 접근할 수 없다.
Car.check_type(25)
Car.check_type(5)


Car.count_instance()    # 객체 생성 전에 클래스 메소드 호출

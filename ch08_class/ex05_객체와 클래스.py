robort_name = 'R1'
robort_pos = 0

#   함수


def robort_move():
    global robort_pos
    robort_pos += 1
    print("{0} postion: {1}".format(robort_name, robort_pos))


robort_move()
#   R1 postion: 1

robort1_name = 'R1'
robort1_pos = 0


def robort1_move():
    global robort1_pos
    robort1_pos += 1
    print("{0} postion: {1}".format(robort1_name, robort1_pos))


robort1_move()


robort2_name = 'R2'
robort2_pos = 10


def robort2_move():
    global robort2_pos
    robort2_pos += 1
    print("{0} postion: {1}".format(robort2_name, robort2_pos))


robort2_move()


class Robort():
    #   초기화 함수
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def move(self):
        self.pos += 1
        print("{0} postion: {1}".format(self.name, self.pos))


robot1 = Robort("R1", 1)
robot2 = Robort("R2", 10)

robot1.move()
robot2.move()

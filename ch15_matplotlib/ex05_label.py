#   라벨,제목,격자,범례,문자열 표시
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

x = np.arange(-4.5, 5, 0.5)
y = 2*x**3

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph title')
plt.show()

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph title')
plt.grid(True)  # 'plt.grid()'도 가능
plt.show()

#   범례지정
x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['data1', 'data2', 'data3', 'data4'])
plt.show()

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['data1', 'data2', 'data3', 'data4'], loc='lower right')
plt.show()

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'], loc='best')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.title('그래프 제목')
plt.grid(True)
plt.show()

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.text(0, 6, "문자열출력1")
plt.text(0, 5, "문자열출력2")
plt.text(0, 5, "문자열출력3")
plt.text(0, 5, "문자열출력4")

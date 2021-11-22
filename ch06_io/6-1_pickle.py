# pickle 모듈을 이용하여 리스트와 클래스 저장하기
colors = ['red','green','black']
print(colors)

import pickle
f = open('colors','wb')
pickle.dump(colors,f)
f.close()

class test:
    var = None

a = test()
a.var = 'Test'

f = open('test','wb')
pickle.dump(a,f)
f.close()

f = open('test','rb')
b = pickle.load(f)
f.close()

print(b)
print(b.var)
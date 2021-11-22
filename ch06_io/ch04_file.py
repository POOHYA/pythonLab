#   파일 읽기
#   형식: f = open('file_name', 'mode')

#   파일 쓰기
#   형식: f = open('file_name', 'w')
#   f.write(str)
#   f.close()

f = open('./ch06_io/myfile.txt', 'w')
f.write('This id mt first file')
f.close()

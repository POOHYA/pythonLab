#   with 문을 활용해 파일 읽고 쓰기
#   with 문의 구조
f = open('./ch06_io/myfile.txt', 'w')
f.write('File write/read.test')
f.close()

#   with 문의 활용
with open('./ch06_io/myfile2.txt') as f:
    f.write('File write/read.test2: line1\n')
    f.write('File write/read.test2: line2\n')
    f.write('File write/read.test2: line3\n')

with open('./ch06_io/myfile2.txt') as f:
    file_string = f.read()
    print(file_string)


with open('./ch06_io/myfile3.txt', 'w') as f:
    for num in range(1,6):
        format_string = "3x{0}={1}\n".format(num, 3*num)
        f.write(format_string)

with open('./ch06_io/myfile3.txt', 'r') as f:
    for line in f:
        

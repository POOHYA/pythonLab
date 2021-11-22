#   필요없는 문자열 삭제하기
#   str.strip([chars])

print("aaaaaPythonaaa".strip('a'))

test_str = "aaaaaPyathonbbbaaa"
temp1 = test_str.strip('a')
print(temp1)

print(temp1.strip('b'))

print(test_str.strip('ab'))
print(test_str.strip('ba'))

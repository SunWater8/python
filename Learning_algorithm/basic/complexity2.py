from random import randint
import time

### 선택정렬 성능 측정
array = []  # 배열 틀 구성
for _ in range(10000):  # range(A)함수 : 0부터 A-1까지의 정수 범위를 반환한다.
    # _(언더바) : 숫자 리터럴 값의 자릿수 구분을 위한 구분자로 쓰임.
    array.append(randint(1, 100))  # 1부터 100 사이의 랜덤한 정수
    # randint(a, b) 함수: a,b 사이의 랜덤한 정수를 반환.
"""

print(array)
print('array[0]', array[0])
print('array 길이: ', len(array))
sort_incre = array.sort()
print('array 오름차순:',array)

a = range(10)
b = range(0,10)
print('a: ', a)
print('b: ', b)

"""

start_time = time.time()

for i in range(len(array)):
    min_index = i  # array에서 가장 작은 정수
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swaping

"""
# 배엷 바꾸기
list_a = [3,5]
list_a[0], list_a[1] = list_a[1], list_a[0]
print('list_a: ',list_a)
"""

end_time = time.time()
print("선택 정렬 성능 측정: ", end_time - start_time)

"""/////////////////////////////////////////////////////"""
### 기본 정렬 라이브러리 성능 측정
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()
print('기본 정렬 라이브러리 성능 측정: ', end_time - start_time)

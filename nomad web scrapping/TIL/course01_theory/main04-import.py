print("==============================")
print("1.12 Modules")
# 모듈에 대해서
# 파이썬을 설치하면 모듈은 기본으로 제공된다.


# math 모듈을 통해 math 관련 함수 사용하기
import math

print(math.ceil(2.3)) # 3
print(math.fabs(-1.2)) # 1.2 fabs(): return absolute num

# python standard library 9.2. , 14.1. , 19.1 에서 math 모듈과 더불어 여러 다른 모듈에 대해서 확인할 수 있음


# 특정함수만 가져오기
# 모듈을 참조하려고 할 때 math 모듈 전체를 불러오는 게 아니라 ceil과 fsum만 불러오게 할 수 있다.
from math import ceil, fsum

print(ceil(1.2)) # 2
print(fsum([1, 2, 3, 4, 5, 6, 7])) # 28.0

# 함수 이름 바꿔보기
from math import fsum as interesting_sum

print(interesting_sum([1, 2, 3, 4])) # 10.0


# 다른파일에서 내가 만든 함수 참조하기
from TIL.course01_theory.calculator import plus, minus
print(plus(1,2)) 
print(minus(2,1))


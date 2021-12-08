print("==============================")
print("1.9 <Conditionals>")
# 조건문 if

# 조건문 중 if else에 대해서 알아보자!
# if user gave me a string, return None. else return something. 문자열이라면 반환하지 않고, 문자열이 아니라면 더하기 연산을 수행하라
def plus(a, b):
    if type(b) is str: #조건 입력
        return None # 조건에 대한 행위 입력
    else:
        return a + b

print(plus(12, "10"))

# python standard library에서 truth value testing 카테고리 안에 보면 비교문 연산자들을 볼 수 있다.

# or 이용해서 if else 문 만들어보기
def plus2(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None 

print(plus2(12, "10"))




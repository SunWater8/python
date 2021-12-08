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







print("==============================")
print("1.10 <if else and or>")
# if else 문에서 and와 or 이용하기. & elif 이용 (elif는 else if와 같은 기능임)

# 조건식 만들어 보기!!
"""
나이를 기준으로 음주 가능한지 출력하기.

18세 이하 - you can't drink
18세, 19세 - you are new to this!
20세 이상 25세 이하 - you are still kind of young
이외의 나이 - enjoy your drink
"""

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink.")
    elif age == 18 or age == 19:
        print("you are new to this!")
    elif age >= 20 and age <= 25: 
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(18)
print("==============================")
print("1.4 <Creating a Your First Python Function>")
# 함수 정의하기
# 파이썬에서는 function을 만든다고 하지 않고 function을 define(정의)한다고 한다.
# function 정의하는 방식 : def라고 쓴 후 function 이름을 쓴다. 함수 내용은 :을 입력한 다음 줄에 들여쓰기 되어야 한다.

def say_hello():
    print("hello")
    print("bye")

# 함수 실행하기
say_hello()





print("==============================")
print("1.5 <Function Arguments>")
# 함수 안에 인자 넣기 
def say_hello(who):
    print("hello", who)

say_hello("sun") # hello sun
say_hello(True) # True

# 계산기 함수 만들어보기
def plus(a,b):
    print(a+b)

plus(3,4) # 7

def minus(a,b):
    print(a-b)

minus(5,2) # 3
# minus(5) --> 인자를 하나만 넣으면 에러가 난다. 

# 인자를 하나만 넣어도 에러가 안나게 하는 방법 : 인자에 기본값을 설정해둔다.
def divide(a,b=2):
    print(a/b)

divide(6) #3

# 마찬가지로 앞서 만들었던 say_hello 함수에도 인자에 기본값을 설정해주면 함수 호출할 때 인자를 입력하지 않아도 에러가 나지 않고 기본값으로 출력이 된다.
def say_hello2(name="anonymous"):
    print("hello", name)

say_hello2() # hello anonymous






print("==============================")
print("1.6 <Return>")
# 함수에서 print()함수와 return 사용하여 결과 값 확인해보기
def p_plus(a,b):
    print(a+b)

def r_plus(a, b):
    return a + b

p_result = p_plus(2, 3) # 5
r_result = r_plus(2, 3)

print(p_result, r_result) # None 5
#  함수 안에서 return 사용한 것은 결과 값을 간직하고 있기 때문에 none이 아닌 결과 값 그대로라고 보여준다.
# return는 결과 값을 반환할 뿐만 아니라 function을 종료하는 기능도 갖고 있다.

def r_plus2(a,b):
    return a + b
    print("dkfjsfldkfj", True) 

r_result2 = r_plus2(2,4)
print(r_result2) # 6 (return 아래에 적은 print는 실행되지 않는다. return는 function을 종료하는 기능을 가지고 있기 때문)








print("==============================")
print("1.7 <Keyworded Arguments>")
# 키워드 인자
# 위에서 적용된 인자는 position argument이다. 위치가 정해져 있는 인자라는 뜻이다.
# def plus(a, b): 로 시작하는 함수에서 a, b가 이에 해당한다. plus(2,4)라고 함수를 호출할 때 함수 만들 때의 a와 숫자2는 한 쌍을 이루며 같은 자리에 위치해야 한다.
# 반면 keyworded arguments라는 것도 존재한다. 위치가 정해져 있지 않은 대신에 이름으로 쌍이 이뤄져 있다.

# position arguments 함수
def plus2(a,b):
    return a + b

result2 = plus2(2,3)
print(result2) # 5

# keyworded arguments 함수
def plus3(a,b):
    return a + b

result3 = plus3(b=30, a=1)
print(result3) # 31

# keyworded arguments 함수 응용 - arguments 가 많을 경우 keyworded arguments가 유용
def say_hello3(name, age, country, fav_food):
    return f"I am {name} and {age} years old. I am from {country}. I like {fav_food}"
# String으로 return 할 경우 앞에 f를 써주어야 들어오는 data가 적용이 됨.

hello = say_hello3(age="20", name="sun", fav_food="pizza", country="korea")

print(hello)


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

plus(3,4)

def minus(a,b):
    print(a-b)

minus(5,2)
# minus(5) --> 인자를 하나만 넣으면 에러가 난다. 

# 인자를 하나만 넣어도 에러가 안나게 하는 방법 : 인자에 기본값을 설정해둔다.
def divide(a,b=2):
    print(a/b)

divide(6)

# 마찬가지로 앞서 만들었던 say_hello 함수에도 인자에 기본값을 설정해주면 함수 호출할 때 인자를 입력하지 않아도 에러가 나지 않고 기본값으로 출력이 된다.
def say_hello2(name="anonymous"):
    print("hello", name)

say_hello2()

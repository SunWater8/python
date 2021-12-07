print("1.0 <Data Types of Python>")
# 변수 variable
# 변수는 수학과 비슷하다. a=2, b=3 처럼
a=2
b=3
print(a+b)

# data type 종류 - string, boolean, integer, float, none
# (변수이름이 길어지면 snake case를 사용한다.)
# 문자는 quote 로 감싸져 있어야 한다.
a_string = "like this"  

# boolean은 앞글자가 항상 대문자다.
a_boolean = False

# 숫자
a_number = 3

# 실수
a_float = 3.12

# none. 존재하지 않는다는 의미. 파이썬에만 있는 개념.
a_none = None



# data type 알아내는 메소드 
print(type(a_number))
print(type(a_boolean))
print(type(a_string))
print(type(a_none))  #NoneType





print("==============================")
print("1.1 <Lists in Python>")

# sequence type (열거형 타입)

# list는 sequence type 중 하나이다. 파이썬에는 열거형 타입이 두 가지 있다. 하나는 list, 다른 하나는 tuples (튜플) 이다.
# list 는 mutable sequence type 이다.mutable은 내용이 바뀔 수 있다는 의미. s.append(x)처럼 배열에 값을 추가할 수 있다.
# list와 다르게 tuples는 immutable 이다. 내가 값을 바꾸고 싶지 않을 때 immutable sequence에 넣어야 한다.

# 요일 list 만드는 방식 : [ ] 괄호 사용.
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

# python standard library 에서 built in types 안에 list에 대해 적힌 기능처럼, x in s 를 적용해서 출력해보기
print("Mon" in days)  #True

# 이 list에서 3번째 요일 찾기
get_third_day = days[2] #index는 0부터 시작하므로 3이 아닌 2를 넣어야 함.
print(get_third_day)

# days 배열의 길이 구하기
print(len(days))  # 5

# days 배열에 sat 이라는 값 추가하기
days.append("sat")
print(days)

# 배열 거꾸로 하기.
days.reverse()
print(days)





print("==============================")
print("1.2 <Tuples and Dicts>")
# tuples는 mutable sequence type이다. mutable은 내용이 바뀌지 않는다는 의미. list에서 했던 것들의 50%를 할 수 있다. 

# 요일을 tuples 로 만드는 방식 : ( ) 괄호 사용.
days2 =  ("Mon", "Tue", "Wed", "Thur", "Fri")
print(days2)

# days2의 타입을 확인해보기
print(type(days2)) #tuples




# Object와 비슷한 개념인 dictionary 만들어보기.
name = "Sun"
age = 33
korean = True
fav_food = ["Kimbap", "milk"]

# 위의 변수들은 모여있지 않은 붕붕떠다니는 변수에 불과하다. 하지만 { } 괄호를 활용하면 하나로 묶을 수가 있다.
sun = {
    "name" : "sun",
    "age" : 33,
    "korean" : True,
    "fav_food" : ["Kimbap", "milk"] #dictionary 안에 list 형태로 된 내용을 저장할 수도 있다.
}

print(sun)
# sun 안의 내용 불러오기
print(sun["name"])
print(sun["age"])
# sun 안에 내용 추가하기
sun["smart"] = True
print(sun)



# dictionary 안에는 list와 tuples를 저장할 수 있다.
# dictionary와 마찬가지로 list에도 다양한 data type을 저장할 수 있다.
something = ["string", True, 11, None, False, "lslslsls"]
print(something)
# 3일차

다중 선택: 싸피

# 함수

## 함수란?

> 특정 작업을 수행하기 위해 재사용 가능한 코드묶음
> 

```python
return_value = print(1) #1
print(return_value) #None
# 할당문은 오른쪽부터 -> print(1) 실행, 1 콘솔에 보여주지만 반환값 없음
# return_value에 할당된게 없음
```

### 함수와 메모리

> 함수 안에 있는 변수들은 함수가 호출 될 때 메모리에 올라간다
> 

## 매개변수와 인자

매개변수(Parameter) : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수

인자(Argument) : 함수를 호출할 때, 실제로 전달되는 값

인자를 인식하는 방법들

- 위치 인자 : 함수 호출 될 때 파라미터 위치에 맞게 인자를 매칭
- 기본 인자 : 인자가 비었을 때를 위해 기본 값을 미리 파라미터에 할당
- 키워드 인자 : 매개변수 시에 지정해둔 이름으로 인자를 매핑
- 임의의 인자 목록 : 정해지지 않은 개수의 인자를 처리
- 임의의 키워드 인자 목록 : 정해지지 않은 개수의 키워드 인자를 처리

```python
# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
greet('Alice')  # TypeError: greet() missing 1 required positional argument: 'age'

######################################################################## 

# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.

######################################################################## 

# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments
greet('Dave', age=35)  # Positional argument cannot appear after keyword arguments

######################################################################## 

# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>

calculate_sum(1, 100, 5000, 30) 
 # (1, 100, 5000, 30)
 # <class 'tuple'>

######################################################################## 

# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30 }
print_info('Eve', age=30)  # TypeError: print_info() takes 0 positional arguments but 1 was given

```

### 함수 파라미터 작성 권장 순서

- 위치 → 기본 → 가변 → 가변키워드
- 강제적인 규칙 X

```python
# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""

```

## 재귀함수

```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(1000))  # 120

def factorial(n):
	# 무한 재귀
	return n * factorial(n - 1)

'''
 return n * factorial(n - 1)
               ~~~~~~~~~^^^^^^^
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
'''

```

그럼 996번 이상의 재귀는?

### Increase Recursion Limit (Not Recommended Unless You Know What You're Doing)

```python
python
복사편집
import sys
sys.setrecursionlimit(2000)
```

Use this only if your recursion is **deep but correct**, e.g., in certain tree or graph traversals. Otherwise, it's better to **rewrite the function iteratively** or **fix the logic**.

## 내장 함수

파이썬이 기본적으로 제공하는 함수

ex) print, sum 등등 너무 많음

## 함수와 Scope

### python의 범위(scope)

함수는 코드 내부에 local scope, 그 외 공간인 global scope로 구분

### 범위와 변수 관계

- Scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
- variable
    - global variable : global scope에 정의 된 변수
    - local vairable : local scope(함수 내부)에 정의 된 변수

```python
# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20

func()

print('global', num)  # NameError: name 'num' is not defined

```

### 변수의 수명

- Built-in scope : 영원
- global scope : 모듈이(파일) 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지
- local scope : 함수가 호출 될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)

- 파이썬 사용되는 이름(식별자)들은 namespace에 저장되어있음
- 그 스페이스를 단계별로 탐색하는 규칙이 있음
    1. Local scope : 현재 함수
    2. Enclosed scope  : 바깥쪽 함수
    3. Global scope  : 모듈 전체
    4. Built-in scope : 기본 내장 

```python
# LEGB Rule 퀴즈
x = 'G'
y = 'G'

def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # EPL

    inner_func('P')
    print(x, y)  # EE

outer_func()
print(x, y)  # GG

```

### global  키워드

- 변수의 스코프를 전역범위로 지정
- 함수 내에서 전역변수 수정하려고 사용

```python
num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1

# ‘global’ 키워드 주의사항 - 1
# global 키워드 선언전에참조불가
num = 0

def increment():
    # SyntaxError: name 'num' is used # prior to global declaration
    print(num)
    global num
    num += 1

# ‘global’ 키워드 주의사항 - 2
# 매개변수에는 global 키워드 사용불가
num = 0

def increment(num):
    # "num" is assigned before global # declaration
    global num
    num += 1
```

## 함수의 규칙

### 작명 규칙

- 소문자와 언더스코어(_)
- 동사로 시작하여 함수 동작 설명
- 약어 사용 지양

### 단일 책임 원칙 (Single Responsibility Principle)

→ 모든 객체는 하나의 명확한 목적과 책임 만을 가져야 함

### 함수 설계 원칙

1. 명확한 목적
    - 함수는 한가지 작업만 수행
    - 함수 이름으로 목적을 명확히 표현

1. 책임 분리
    - 데이터 검증, 처리, 저장 등을 별도 함수로 분리
    - 각 함수는 독립적으로 동작 가능하도록 설계

1. 유지 보수성
    - 작은 단위의 함수로 나누어 관리
    - 코드 수정 시 영향 범위를 최소화

```python
# 올바른 설계 예시 (책임을 분리한함수들)
def validate_password(password):
    """비밀번호 유효성 검사"""
    if len(password) < 8:
        raise ValueError('비밀번호는 8자 이상이어야 합니다')

def save_user(user_data):
    """비밀번호 암호화 및 저장"""
    user_data['password'] = hash_password(user_data['password'])
    db.users.insert(user_data)

def send_welcome_email(email):
    """환영 이메일 발송"""
    send_email(email, '가입을 환영합니다!')

# 메인 함수에서 순차적으로 실행
def process_user_data(user_data):
    validate_password(user_data['password'])
    save_user(user_data)
    send_welcome_email(user_data['email'])
```

### 함수 반환 규칙

1. 오직 하나의 객체만 return 할 수 있음
2. return a, b, c 처럼 콤마를 사용하면 파이썬은 이를 객체로 자동 패킹함

## Packing & Unpacking

### 패킹 (Packing)

패킹 : 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)
```

임의의 인자 : ‘*’을 활용한 패킹  

- 남는 위치 인자들을 튜플로 묶기
- * 을 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듬

```python
# ‘*’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>

```

임의의 키워드 인자 : ‘**’ 을 활용한 패킹

- 남는 키워드 인자들을 딕셔너리로 묶기
- ** 을 붙인 매개변수가 남는 키워드 인자들을 모두 모아 하나의 딕셔너리로 만듦

```python

# ‘**’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func2(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs))  # <class 'dict’>
```

### 언패킹(Unpacking)

- 언패킹 : 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐놓는 과정
- 시퀀스 언패킹 또는 다중할당이라 부름

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) #(1, 2, 3, 4, 5)
# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5

```

```python
# ‘*’ 을 활용한 언패킹 (함수 인자 전달)
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter

# ‘**’을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```

### 언패킹에 대한 고찰

```python
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}

############################################

# **로 언패킹하여 함수에 전달
my_function(**my_dict)  # 1 2 3

############################################

# 변수에 언패킹 하여 출력 
x, y, z = my_dict
print(x, y, z) #x, y, z

# 그럼 바로 언패킹 하면?
print(**my_dict) # TypeError: print() got an unexpected keyword argument 'x'

"""
셋 다 언패킹인데 my_function 함수는 되고, 변수 언패킹도 되는데 바로 언패킹은 왜 안될까?
이유는 ** 언패킹이 두가지로 나뉘기 때문에
1. iterable 언패킹
2. 키워드 인자 언패킹
"""
# 1 function은 왜 될까? -> 키워드 인자여서
def my_function(a, b, c):
    print(a, b, c)
my_dict = {'x': 1, 'y': 2, 'z': 3}

my_function(**my_dict) # TypeError: my_function() got an unexpected keyword argument 'x'

"""
my_function 파라미터 이름이 x,y,z가 아니어서 오류가 남
my_function(x=1, y=2, z=3)이어서 오류가 남
my_dict = {'a': 1, 'b': 2, 'c': 3} 라면 오류 안남
"""
#결국 print(**my_dict)는 아래와 같은 이유로 에러가 남
print(x=1) #TypeError: print() got an unexpected keyword argument 'x'

#2 print(x, y, z) #x, y, z 는 왜 될까?

x, y, z = my_dict  # iterable unpacking → keys만 unpack
# dict는 기본적으로 반복(iteration)하면 key만 나옵니다

```

### 전역 변수와 전역 리스트의 차이

```python
# 1
a = 1
def change():
    a = 3
    print(a)

change() #3
print(a) #1

###########################

# 2
a = 1
def change():
    a = a + 1
    print(a)

change() # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

############################

# 3
li = [0,1,99]
def change():
    li[0] = li[1]
    print(li)

change() # [99, 1, 99]
print(li) # [99, 1, 99]

# 4 
lst = [1, 2, 3]

def rebind():
    lst = [999, 2, 3]  # 새로운 리스트 할당 (재바인딩)
    print(lst)

rebind() # [999, 2, 3
print(lst)  # [1, 2, 3]
"""
파이썬은 함수 내부의 변수 = ? 을 무조건 지역변수로 생각함
그래서 global로 전역변수를 지역변수 처럼 포장해야 쓸 수 있음

그렇다면 3번은 왜?
리스트 자체에 할당하는 것이 아니라 리스트 내부에 값을 수정하는 것이기 때문에 가능했음

4번은 지역 리스트가 됨

"""
```

## Lambda Expression

> 익명 함수 표현식
> 

### 람다의 구조

```python
# 변경 전
def addition(x, y):
    return x + y

# 변경 후
lambda x, y: x + y

# 변경 전 활용
result = addition(3, 5)
print(result)  # 8

# 변경 후 활용
addition = lambda x, y: x + y
result = addition(3, 5)
print(result)  # 8

# 람다 표현식 활용 - 1 (with map 함수)
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]

```
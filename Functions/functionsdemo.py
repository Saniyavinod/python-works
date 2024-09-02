# def function_name(p1,p2,...........):

#     function defenition

#     return value


def add(n1,n2):
    result=n1+n2
    return result
print(add(30,70))


def is_odd(num1):
    result=True if num1%2!=0 else False
    return result
print(is_odd(67)) 

def max_two(n1,n2):
    result=n1 if n1>n2 else n2
    return result
print(max_two(8,7))


def cube(num):
    result=num**3
    return result
print(cube(3))
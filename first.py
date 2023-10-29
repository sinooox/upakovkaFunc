def fun(*args):
    print(args[0])

    print(args)

fun("Python", "C++", "Java", "C#")

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1, 2, 3))
print(sum(1, 2, 3, 4))
print(sum(1, 2, 3, 4, 5))

def fun(**kwargs):
    print(kwargs)

fun(name="Александр", age="17", company="НГТУ")
fun(language="Python", version="3.8")

def fun(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

fun(name="Анна", age="16", company="НГТУ")

def sum(*args):
  result = 0
  for arg in args:
    result += arg
  return result

numbers = (1, 2, 3, 4, 5)
print(sum(*numbers))

def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")

person =("Алена", 18, "НГТУ")
print_person(*person)

def print_person(name, age, company):
  print(f"Name:{name}, Age: {age}, Company: {company}")

alena ={"name":"Алена", "age":18, "company":"НГТУ"}
print_person(**alena)

def sum(num1, num2, *nums):
    result=num1+num2
    for n in nums:
        result += n
    return result

print(sum(1,2,3))
print(sum(1,2,3,4))
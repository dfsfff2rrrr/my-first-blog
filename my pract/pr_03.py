#def say_hello(name):
 #   print(f"Hello, {name}")


#say_hello("Tom")
#say_hello("Bob")
#say_hello("Alice")

#def print_person(name, age):
 #  print(f"Age: {age}")

#print_person("Tom", 37)

#def say_hello(name="Tom"):
 #  print(f"Hello, {name}")

#say_hello()
#say_hello("Bob")

#def print_person(name, age = 18):
 #   print(f"name: {name} Age: {age}")

#print_person("Bob")
#print_person("Tom", 37)

#ef print_person(name, /, age = 18, *, company):
 #   print(f"Name: {name} Age: {age} Company: {company}")
'''
#rint_person("Sam", company ="Google" )
#rint_person("Tom", 37, company="JetBrains")
#rint_person("Bob", company = "Micrasoft", age = 42
def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1, 2, 3, 4, 5)  # sum = 15
sum(3, 4, 5, 6)  # sum = 18



def get_message():
    return "Hello METANIT.COM"


message = get_message()
print(message)


print(get_message())



def sum(a, b):
    return a + b


result = sum(4, 6)
print(f"sum(4, 6) = {result}")
print(f"sum(3, 5) = {sum(3, 5)}")



def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)

def do_operation(a, b, operation):
     result = operation(a,b)
     print(f"result = {result}")

def sum(a, b): return a + b
def multiply(a, b): return a * b

do_operation(5, 4, sum)
do_operation(5, 4, multiply)



def sum(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply


operation = select_operation(1)
print(operation(10, 6))

operation = select_operation(2)
print(operation(10, 6))

operation = select_operation(3)
print(operation(10, 6))

sum = lambda a, b,: a + b

print(sum(4, 5))
print(sum(5, 6))

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b

    operation = select_operation(1)
    print(operation(10, 6))

    operation = select_operation(2)
    print(operation(10, 6))

    operation = select_operation(3)
    print(operation(10,6))

a = int(15)
b = int (3.7)
c = int ("4")
e = int (False)
f = int (True)

a = "2.7"
b = 3
c = float(a) + b
print(c)

a = float (15)
b = float (3.6)
c = float ("4.7")
d = float ("5")
e = float (False)
message = "Age: " + str(age)
print(message)

name = "Tom"


def say_hi():
    print("Hello",name)

def say_bye():
   print("Good bye", name)

say_hi()
say_bye()

def say_hi():
   name = "Sam"
   surname = "johnson"
   print("Hello", name, surname)


def say_bye():
   name = "Tom"
   print("Good bye", name)

say_hi()
say_bye()

name = "Tom"

def say_hi():
   name = "Bob"
   print("Hello",name)

def say_bye():
   print("Good bye", name)

say_hi()
say_bye()



def outer():
    n = 5

    def inner():
        nonlocal n
        n = 25
        print(n)

    inner()
    print(n)


outer()

name = "Tom"

def say_hi():
     print("Hello",name)

def say_bye():
   print("Good bye", name)

say_hi()
say_bye()

def outer():
  n = 5
  def inner():
    nonlocal n
    n +=1
    print(n)
   return inner
fn = outer()

fn()
fn()
fn()
'''

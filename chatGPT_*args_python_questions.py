#Q1. Predict the output.
def test(*a):
    print(a)

test(10, 20, 30)
#(10, 20, 30)
#Explanation: *a collects all positional arguments into a tuple.
#Q2. Predict the output.
def test(*numbers):
    print(type(numbers))
    print(len(numbers))

test(5, 10, 15, 20, 25)
#<class 'tuple'>
#5
#Explanation: *numbers stores the arguments in a tuple. len() returns the number of elements.
'''Q3. Write a program using *args to accept any number of numbers and print each number using a for loop.'''
def num(*a):
    for i in a:
        print(i)

num(10, 20, 3, 4, 5, 6)
'''Q4. Write a function using *args to calculate the sum of all given numbers.'''
def add(*num):
    total = 0

    for i in num:
        total += i

    print(total)

add(10, 23, 53, 63)
#Level 2 – Unpacking
'''Q5. Predict the output.'''
a = [10, 20, 30, 40]
print(*a)
#Explanation: *a unpacks the list into individual values.
'''Q6. Predict the output.'''
a = (1, 2, 3)
b = [*a, 4, 5]
print(b)
#Explanation: The tuple elements are unpacked into a new list.
'''Q7. Write a program to unpack a list into a function.'''
def student(a, b, c):
    print(a)
    print(b)
    print(c)
numbers = [10, 20, 30]
student(*numbers)
'''Q8. Explain the difference between these two statements.'''
a = [10, 20, 30]
print(a)
print(*a)
'''Your Answer:
- print(a) – Prints the values in the list as a list.
- print(*a) – Unpacks the values in the list and prints them individually.'''
#Level 3 – Intermediate challenges
'''Q9. Find the maximum number using *args without using the built-in max() function.'''
def maximum(*a):
    temp = a[0]
    for i in a:
        if i > temp:
            temp = i
    print(temp)
maximum(10, 50, 30, 90, 20)
#Explanation: We initially store the first number in temp and compare it with every other number.
'''Q10. Create a function that accepts any number of arguments and separates even and odd numbers.'''
def check(*a):
    ev = []
    od = []
    for i in a:
        if i % 2 == 0:
            ev.append(i)
        else:
            od.append(i)
    print("Even:", ev)
    print("Odd:", od)
check(2, 3, 4, 5, 6, 7, 8, 9)
'''Q11. Combine two lists using unpacking instead of +.'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c)
'''Q12. Create a function that accepts any number of names and prints the longest name.'''
def long(*a):
    length = 0
    name = ""
    for i in a:
        if len(i) >= length:
            length = len(i)
            name = i
    print(name)
long("Ram", "Venkat", "Alexander", "John")
#Explanation: The function compares the length of each name and stores the longest name
'''
Important concepts – Quick revision
Syntax	             Purpose
def test(*a)	       Packing
test(*a)	           Unpacking
*args	               Collects arguments into a tuple
[*a]	               Unpacks elements into a new list
**kwargs	           Collects keyword arguments into a dictionary'''








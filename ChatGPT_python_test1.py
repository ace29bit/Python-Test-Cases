'''Create a list containing [10, 20, 30, 40, 50]. Append 60, insert 15 at index 1, remove 30, and print the
final list.'''
'''l=[10,20,30,40,50]
l.append(60)
l.insert(1,15)
l.remove(60)
print(l)'''
'''Given nums = [8, 3, 12, 5, 2, 10],
print the largest number, smallest number, and sum of all numbers.'''
'''nums = [8, 3, 12, 5, 2, 10]
print(min(nums))
print(max(nums))
print(sum(nums))'''
'''Given names = ['Ravi', 'Anu', 'Kiran', 'Meena'],
replace 'Kiran' with 'Arjun' and print the updated
list.
names = ['Ravi', 'Anu', 'Kiran', 'Meena']
names.pop(2)
names.insert(2,"Arjun")
print(names)'''
'''4. Given items = ['pen', 'book', 'pen', 'bag', 'pen'],
count how many times 'pen' appears.
items = ['pen', 'book', 'pen', 'bag', 'pen']
print(items.count("pen"))'''

'''5. Given a = [1, 2, 3] and b = [4, 5, 6],
create and print one combined list without changing the original
lists.'''
'''a = [1, 2, 3]
b = [4, 5, 6]
c=a.copy()+b.copy()
print(c)'''

'''6. Given values = [10, 20, 30, 40, 50, 60],
print the first three elements, last two elements, and the list
in reverse order.
values = [10, 20, 30, 40, 50, 60]
print([values[0],values[1],values[2]])
print([values[4],values[5]])
values.reverse()
print(values)'''

'''7. Given marks = [45, 80, 67, 90, 32],
sort the list in ascending order and then in descending order.
marks = [45, 80, 67, 90, 32]
marks.sort()
print(marks)
marks.reverse()
print(marks)'''

'''8. Given data = [1, 2, 2, 3, 3, 3, 4],
create a new list containing each value only once. Preserve the
original order.
data = [1, 2, 2, 3, 3, 3, 4]
samp=data.copy()
print(list(set(samp)))
print("Original set ",data)'''
#sets

'''1. Create a set from [1, 2, 2, 3, 4, 4, 5].
Print the set and explain why duplicate values disappear.
data=[1, 2, 2, 3, 4, 4, 5]
print(set(data))
print("Set doesn't take duplicate values. If, duplicate value occur it will only print the single value")
'''
'''
2. Given A = {1, 2, 3, 4} and B = {3, 4, 5, 6},
print their union, intersection, and difference (A − B).
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)
print(a&b)
print(a.difference(b))'''

'''3. Given students_python = {'Asha', 'Ravi', 'John'} and students_java = {'Ravi',
'Meena', 'John'}, find students learning both languages.
students_python = {'Asha', 'Ravi', 'John'}
students_java = {'Ravi','Meena', 'John'}
print("Students who are learning both  language: ",students_python&students_java)'''

'''4. Create an empty set,
add the values 10, 20, and 30, remove 20, and print the result.
empty=set()
empty.update({10,20,30})
print(empty)
empty.remove(20)
print(empty)'''

'''5. Given x = {2, 4, 6} and y = {2, 4, 6, 8, 10},
check whether x is a subset of y.
6. Given two lists of phone numbers,
find the numbers that are present in both lists using sets.
#5
x = {2, 4, 6}
y = {2, 4, 6, 8, 10}
print(x.issubset(y))'''

#dict
'''1. Create a dictionary for a student with keys name, age, and course.
Print each value using its key.
2. Given student = {'name': 'Arun', 'marks': 75},
update marks to 88 and add a new key city with
value 'Vijayawada'.
3. Given prices = {'pen': 10, 'book': 50, 'bag': 400},
print the names of all products and calculate
the total price.
#1
details={"name":"venkat","age":24,"course":"python"}
print(details.get("name"))
print(details.get("age"))
print(details.get("course"))
print(details.get("name","age"))
#2
student = {'name': 'Arun', 'marks': 75}
student.update({'marks':88})
student.setdefault("city","vijayawada")
print(student)
#3
prices = {'pen': 10, 'book': 50, 'bag': 400}
print(prices.keys())
print(sum(list(prices.values())))'''

'''4. Given inventory = {'apple': 10, 'banana': 5},
check whether 'orange' exists. If it does not, add it
with quantity 8.
5. Create a dictionary from two lists: keys = ['name', 'age', 'city']
and values = ['Sam', 22,'Guntur'].
The result should pair each key with its matching value.
6. Given marks = {'Asha': 85, 'Ravi': 72, 'John': 91, 'Meena': 66},
find the student with the highest marks.
7. Given sentence = 'python is easy and python is useful',
create a dictionary that counts how many times each word appears.'''
#4
'''inventory = {'apple': 10, 'banana': 5}
#print(bool(inventory.get("orange")))
print(inventory.get("oranges"))'''
#5
'''keys = ['name', 'age', 'city']
values = ['Sam', 22,'Guntur']
dic={keys[0]:values[0],keys[1]:values[1],keys[2]:values[2]}
print(dic)'''
#6
'''marks = {'Asha': 85, 'Ravi': 72, 'John': 91, 'Meena': 66}
high=max(marks.values())
for name, mark in marks.items():
    if mark==high:
        print("Name: ",name)'''
#7
'''di={}
sentence = 'python is easy and python is useful'
#di.update({"Python":sentence.count("python"),"is":sentence.count("is"),"easy":sentence.count("easy"),"and":sentence.count("and"),"useful":sentence.count("useful")})
#print(di)
words=sentence.split()
for word in words:
    di[word]=di.get(word,0)+1
print(di)'''
#conditions
'''3. Ask for three numbers and print the largest number.
Also handle the case where two or more numbers are
equal.
4. Ask the user for a mark from 0 to 100.
Print a grade: A (90–100), B (75–89), C (60–74), D (40–59), or Fail
(below 40). Reject values outside 0–100.'''
#3
'''a=int(input("Enter number "))
b=int(input("Enter number "))
c=int(input("Enter number "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
elif a==b==c:
    print("All are equal")'''
#4
'''marks=int(input("Enter your marks: "))
if marks<40:
    print("Fail")
elif marks<=59:
    print("grade D")
elif marks<=74:
    print("grade C")
elif marks<=89:
    print("grade B")
elif marks<=100:
    print("grade A")
elif '''
'''5. Ask for a year and check whether it is a leap year.
6. Ask for a username and password.
Print 'Login successful' only when both match values you define in your
program; otherwise print 'Invalid login'.'''
'''user="venkat@gamil.com"
pas="Techminds@123"
user1=input("Enter the userName: ")
pas1=input("Enter the valid: ")
if user==user1 and pas==pas1:
    print("Log-in Successfull")
else:
    print("Invalid Login")'''
#Loop
'''Use a for loop to print the numbers from 1 to 20.
2. Use a while loop to print the numbers from 10 down to 1.
3. Ask the user for a number n. Use a loop to calculate the sum from 1 to n.
4. Ask the user for a number. Print its multiplication table from 1 to 10.
5. Given nums = [12, 5, 18, 7, 20, 3], use a loop to print only the even numbers.'''
#1
'''for i in range(1,21):
    print(i,end=" ")'''
#2
'''i=1
while i<=10:
    print(i,end=" ")
    i+=1'''
#3
'''n=int(input("Enter a number: "))
total=0
for i in range(1,n+1):
    total+=i
print(total)'''
#4
'''num=int(input("Enter a value: "))
mul=0
for i in range(1,11):
    mul=num*i
    print(mul)'''
#5
'''nums = [12, 5, 18, 7, 20, 3]
for num in nums:
    if num%2==0:
        print(num)'''
#mixed challanges
'''1. Given students = {'Asha': 85, 'Ravi': 38, 'John': 72, 'Meena': 29},
use a loop and
condition to create separate lists for passed students (40 or more)
and failed students.
'''
'''students = {'Asha': 85, 'Ravi': 38, 'John': 72, 'Meena': 29}
pas=[]
fail=[]
for names,marks in students.items():
    if marks>=40:
        pas+=names,marks
    else:
        fail+=names,marks      
print("Pass Students: ",pas)
print("Failed: ",fail)'''
#2
'''2. Given numbers = [1, 2, 2, 3, 4, 4, 5, 6], use a set to remove duplicates,
then use a loop to create
a list containing only even values.'''
'''
numbers = [1, 2, 2, 3, 4, 4, 5, 6]
uni_num=set(numbers)
eve=[]
for num in uni_num:
    if num%2==0:
        eve.append(num)
print("Even Numbers list: ",eve)'''
#3
'''3. Build a simple shopping cart using a dictionary.
Let the user enter a product and quantity, update the cart, and
print the final cart and total quantity of items.'''
'''cart={}
total_quan=0
while True:
    products=input("Enter your products: ")
    quant=int(input("Enter the quantity: "))
    cart.update({products:quant})
    total_quan+=quant
    print(cart)
    choice=input("Do you want continue:(yes/no): ")
    if choice.lower()=="no":
        break
print("Final Cart ",cart,"\ntotal Quantity: :",total_quan)'''
#4
'''4. Create a menu-driven calculator.
Repeatedly show options for addition, subtraction, multiplication, division, and
exit. Use conditions to select the operation and a loop to keep the menu running.
'''
'''print("welcome to calculator")
while True:
    #print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice=int(input("enter the operation:\n1.add\n2.sub\n3.mul\n4.div\n5.exit\n"))
    if choice==1:
        print("Addition")
    elif choice==2:
        print("Subtraction")
    elif choice==3:
        print("Multiplication")
    elif choice==4:
        print("Division")
    elif choice==5:
        print("Thank you")
        break'''
        
#5
'''5. Given a sentence, use a dictionary to count each word.
Then print only the words that occur more than once.'''
'''sent="python is very useful and python is good to learn"
di={}
nsen=sent.split()
for i in nsen:
    di[i]=di.get(i,0)+1
for k,v in di.items():
    if v==2:
        print(k,v)'''

sent = "apple banana apple mango banana apple orange"
nsent=sent.split()
di={}
for i in nsent:
    di[i]=di.get(i,0)+1
for k,v in di.items():
    if v==1:
        print(k,v,end=" ")













    



















    
    


    



























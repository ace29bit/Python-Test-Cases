#1)Write a program to find whether a given year is a leap year or not satisfying all the possible conditions for a leap year?
#solution
year=int(input("enter the year: "))
if year%4==0:
    print(year," is Leap year")
else:
    print(year," is not a Leap year")
#2
'''
2) Write a program to convert the temperature entered in Fahrenheit to Celsius ?'''
#solution
f=float(input("Enter the temperature: "))
faren=(f-32)/1.8
print("Temperature in CELCIUS: ",faren,"C")
#3
'''4)Write a program to calculate the sum and average of First n natural numbers by taking n as input
from the user?'''
#solution
n=int(input("Enter the n natural number: "))
sum_of_n=n*(n+1)/2
avg_of_n=sum_of_n/n
print("Sum of N natural numbers are: ",sum_of_n)
print("Average of N natural numbers are: ",avg_of_n)
#5
'''5)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of
5,'''
#solution
count=0
for i in range(1,201):
    if i%7==0 and i%5!=0:
        count+=1
        print(i,end=",")
print("Total count is: ",count)
#6
'''6)Write a program to find the sum of squares of the first 20 odd numbers?'''
#solution
squ_sum=0
for i in range(41):
    if i%2!=0:
        squ_sum+=i**2
print("Sum of squares of the first 20 Odd numbers: ",squ_sum)'
#7
'''7)Write a program that accepts a sentence
and calculates the number of letters and digits.'''
#solution
st=input("enter the sentence that contains both numbers and alphabets: ")
char=0
num=0
for i in st:
    if i.isdigit():
        num+=1
    elif i.isalpha():
        char+=1
print(f"No. of letters {char} and numbers {num}")
#or
st=input("enter the sentence that contains both numbers and alphabets: ").lower()
char=0
num=0
for i in st:
    if 'a'<=i<='z':
        char+=1
    else:
        num+=1
print(f"No. of letters {char} and numbers {num}")
#8
'''8)write a program to
print the multiplication table of n,by taking n as input from user'''
#solution
num=int(input("Type number to get the table: "))
num2=0
for i in range(1,11):
    num2=i
    i*=num
    print(f"{num}X{num2}={i}")
#9
'''9)Write a program to
calculate the area of the triangle by accepting base and height as integer/float
input from the user?'''
#solution
b=float(input("enter base: "))
h=float(input("enter height: "))
_area_t=1*(b*h)/2
print("Area of Triangle: ",_area_t)
#10
'''10)Write a program to
find the greatest number from three numbers by accepting three integer
inputs from the user?'''
#solution
a=[]
for i in range(3):
    i=int(input("Enter the number: "))
    a.append(i)
if a[0]>a[1] and a[0]>a[2]:
    print(a[0]," is Big")
elif a[1]>a[0] and a[1]>a[2]:
    print(a[1]," is Big")
else:
    print(a[2]," is Big")
#11
'''11)Write a program that prompts the
user to enter a number between 1-7 and then displays the
corresponding day of the week.'''
#solution
while True:
    num = int(input("Enter a number between 1 and 7: "))

    if num in [1, 2, 3, 4, 5, 6, 7]:
        if num == 1:
            print("Monday")
        elif num == 2:
            print("Tuesday")
        elif num == 3:
            print("Wednesday")
        elif num == 4:
            print("Thursday")
        elif num == 5:
            print("Friday")
        elif num == 6:
            print("Saturday")
        else:
            print("Sunday")
        break
    else:
        print("Select only from 1 to 7")
#12
'''12)Write a Python program to convert
Imperial Units of Inches with the Metric Units of Centimetres
by if-elif-else by accepting float value of units and ask whether inches or cms from the user and then
convert that means two inputs from the user?'''
#solution
value=float(input("enter the value: "))
unit=input("entered value is inches/cm(centimeter): ")
if unit in ['inches','inche','in']:
    cm=value*2.54
    print("{} centimeters".format(cm))
elif unit in ['centimeters','cm']:
    inche=value/2.54
    print(f"{inche} inches")
else:
    print("You haven't entered any value")
#13
'''13)write a program to determine
whether the character entered is a vowel or not by using logical
operator?'''
#solution
st=input("enter alphabet to know vowel or consonents: ")
if st=='a' or st=='i' or st=='e' or st=='o' or st=='u':
    print("it is vowel")
else:
    print("it is consonents")
#14
'''14)Write a program that accepts a sentence and calculate the number of upper case letters and
lower case letters.'''
#solution
st=input("enter the sentence: ")
upper=0
lower=0
for i in st:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("UPPER CASE ",upper,"\nLOWER CASE ",lower)
#15
'''15)Write a program to evaluate
whether the given number is even or odd by accepting input from
the user?'''
#solution
'''num=int(input('enter a number: '))
print("Even" if num%2==0 else "odd")'''
#16
'''16))Write a program that accepts a sentence
and calculates the number of letters and digits.'''
#solution
st=input("enter a  sentence contains alphanumerical: ")
char=0
num=0
for i in st:
    if i.isalpha():
        char+=1
    elif i.isdigit():
        num+=1
print("No. of characters {} and numbers {}".format(char,num))



















count = 5 
count = count + 1  
print(count)

name = "Akbert"
age = 21
height = 1.55

print(name)
print(age)
print(height)

pi = 3.1459688
print(f"pi is rounded to 3 decimals: {pi:.3f}")


a =int(input("enter the first number: "))
b =int(input("enter the second number: "))

print(a+b)

num =int(input("Enter a number: "))

for i in range(1, 11):

     print(f"{num} x  {i} = {num * i}")

string_ = "adam is a boy and adam loves to play cricket."
words = string_.split()
count = words.count("adam")
print(f"adam occurs {count} times")

num = int(input())
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


num1 =int(input("number1 = "))
num2 =int(input("number2 = ")) 
product = num1 * num2
result = num1 + num2
if product >500:
    result = num1 + num2
else:
    result = product
    print("the result is" , result)

a,b,c = 10,30,20
greatest = max(a,b,c)
print(f"{greatest} is greatest")

lst =input("Enter list items separated by space:").split()
if not lst:
    print("false")
else:
    print(lst[0] == lst[-1])

f =float(input("enter temprature in fahrenheit: "))
c = (f-32)*5/9
print(f"{f} fahrenheit is equal to {c} celcius")

n =int(input())
fact = 1
for i in range(1,n+1):
    fact*=i
    print(fact)

word =input()
reversed_word = word[::-1]
print(reversed_word)

num  =input()
reversed_num = num[::-1]
print(reversed_num)

n =int(input())
print("result:" , end=" ")
while n > 0:
    print(n, end=" ")
    n -=1

count = 0 
for i in range(0, 50):
   if i % 7 == 0:
      print(i,end=" ")
      count += 1
   if count == 8:
       break

x = [2,3,4,5,6,7,8]
squares = [num**2 for num in x]
print(f"Result: {squares}")

x =[10,23,24,35,65,78,90]
even_numbers = [num for num in x if num % 2 == 0]
odd_numbers = [num for num in x if num % 2 !=0]
print(f"{even_numbers}")
print(f"{odd_numbers}")
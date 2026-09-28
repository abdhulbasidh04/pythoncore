# def add():
#     "addition of two numbers"
#     n1=int(input("Enter the first number: "))
#     n2=int(input("Enter the second number: "))
#     s=n1+n2
#     print("sum",s)
#     return
# add()

# define a function to display "hello your name"
# def display():
#     "To display name"
#     s="hello your name"
#     print(s)
#     return
# display()
# define a function to find the factorial of a number
# def fact():
#     "To find the factorial of a number"
#     n=int(input("Enter the number: "))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#     return
# fact()
# # define a function to find the count of a specific character of a given string
# def count_ch():
#     'fing a specific character of a string'
#     s=input("Enter the string: ")
#     c=input("Enter the character: ")
#     count=0
#     for i in s:
#         if i==c:
#             count=count+1
#     print(count)
#     return
# count_ch()
# define a function to check whether a number is prime or not
# def prime():
#     "to find prime or not"
#     n = int(input("Enter the number: "))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("Not Prime")
#                 break
#         else:
#             print("Prime")
#     else:
#         print("neither prime nor composite")
#     return
# prime()
#define a function to find the factors of a number
# def fact():
#     "factors of a number"
#     n=int(input("Enter the number: "))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#             1
#     return
# fact()

#parametr & arguments
# def add(n1,n2):
#     "sum of two numbers"
#     sum=n1+n2
#     print(sum)
#
# add(23,34)
#define a function that takes amount,year and rate as arguments
# def si(p,n,r):
#     si=(p*n*r)/100
#     print(si)
#     return
#
# p=int(input("Enter the amount: "))
# n=int(input("Enter the year: "))
# r=int(input("Ente the rate: "))
# si(p,n,r)

# return statement
# define a function that takes two numbers as arguments and return sum as result
#call the function and print the result
# def sum(n1,n2):
#     s=n1+n2
#     return s
#
# a=sum(10,20)
# print(a)

#  define a function that takes as a string as argument and return as a new dictionary where keys are words and values are length of each word call the function and print the dictionery
# def func(s):
#     new={i:len(i) for i in s.split()}
#     return new
# print(func(s="python coding is easy and fun"))

# define a function that takes a number as arguments and check whether that number is spy number or not.
# sum of digits =product of digits
# def func(n):
#     sum=0
#     p=1
#     s=str(n)
#     for i in s:
#         sum=sum+int(i)
#         p=p*int(i)
#         if sum==p:
#             return "spy number"
# print(func(21))

# keyword argument
# def sum(n1,n2):
#     s=n1+n2
#     return s
# a=sum(n2=20,n1=10)
# print(a)
# def fun(n,a):
#     print("name",n)
#     print("age",a)
# fun(a=23,n='arun')

#arbitary positional arguments
# def fun(**args):
#     print(args)
# fun(1,2,3,4,5)
#arbitary keyword type
# def fun(**kwargs):
#     print(kwargs)
# fun(a=1,b=2,c=3)

# define a function to find the sum of number using arbitrary argument type
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# add(1,2)
# add(10,20,30,40)



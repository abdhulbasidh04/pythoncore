# #write a program to check whether the user entered number is 2digit,3digit,4digit or not
# # a=int(input("Enter the number: "))
# # if a>=10 and a<=99:
# #     print("The entered number is two digit")
# # elif a>=100 and a<=999:
# #     print("The entered number is three digit")
# # elif a>=1000 and a<=9999:
# #     print("The entered number is four digit")
# # else:
# #     print("invalid")
#
# #write a basic calculator program to perform arithmatic operation
# #(+,-,*,/,%,//)
# n1=int(input("Enter the first number: "))
# n2=int(input ("Enter the second number: "))
# op=input("Enter the operation: ")
# if op=='+':
#     print(f"sum is :{n1+n2}")
# elif op=='-':
#     print(n1-n2)
# elif op=='*'
#     print(n1*n2)
# elif op=='/':
#     print(n1/n2)
# elif op=='%'
#     print(n1%n2)
# elif op=='//'
#     print(n1//n2)
# else:
#     print("invalid")

#write a program to print the number of days in a month
# l1=['jan','mar','may','jul','aug','oct','dec']
# l2=['apr','jun','sep','nov']
# l3=['feb']
# month=input("Enter the month: ")
# if month in l1:
#     print("31 days in",month)
# elif month in l2:
#     print("30 days in",month)
# elif month in l3:
#     print("28 or 29 days in",month)
# else:
#     print("wrong")
#write a program to print the grades based on the following criteria:
#91-100   grade A
#81-90    grade B
#71-80    grade C
#61-70     grade D
# a=int(input("Enter the number: "))
# if a>=91 and a<=100:
#     print("Grade A")
# elif a>=81 and a<=90:
#     print("Grade B")
# elif a>=71 and a<=80:
#     print("Grade C")
# elif a>=61 and a<=70:
#     print("Grade D")
# else:
#     print
#Write a program to check the following
#a number is divisible by 2&3
#a number is divisible by two and not divisible by 3
#a number is divisible by 3 and not divisible by 2
#a number is not divisible by two and three
# a=int(input("Enter the number: "))
# if a%2==0:
#     print(a," is divisible by 2 ")
#     if a%3==0:
#         print(a,"is divisible by 3")
#     else:
#         print(a,"is 6not divisible by 3")
# else:
#     print(a,'not divisible by 2')
#     if a%3==0:
#         print(a,"is divisible by 3")
#     else:
#         print(a,"is not divisible by 3")
#check whether the entered number is
#positive even or positive odd
# negative even or negative odd
n=int(input("Enter the number: "))
if n>0:
    print(n,"is positive")
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
else:
    print(n,"is negative")
    if n%2!=0:
        print(n,"odd")
    else:
        print(n,"even")

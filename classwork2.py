
# #Write a program to check whether two entered numbers are equal or not
a=int(input("Enter the first number: "))
b=int(input("Enter the second number"))
if a=b:
    print("both the number are equal")
else:
    print("not equal")

#Write a program to check whether two entered words are equal or not
a=input("Enter the first word: ")
b=input("Enter the second word: ")
if a=b:
    print("Both words are equal")
else:
    print("Not equal")

#Write a program to find the maximum of two numbers
n1=int(input("Enter the number: "))
n2=int(input("Enter the second number"))
if n1>n2:
    print("n1 is greater")
else:
    print("n2 is greater")

#write a program to check whether the entered character is vowel or not
ch=input("Enter the word: ")
vowel="aeiou"
if ch in vowel:
    print("entered character is vowel")
else:
    print("not vowels")

#Write a program to check whether the entered country name contains word 'land'
country=input("Enter the country name: ")
if land in country:
    print(country)
else:
    print("no")

#write a program to check whether the entered number is 3 digit or not
a=int(input("Enter the number: "))
if a>=100 and a<=999:
    print("Given number is three digit")
else:
    print("Not three digit")

#write a program to check whether the entered string is  palindromde or not
a=input("Enter the string: ")
if a==a[::-1]:
    print("palindrome")
else:
    print("Not palindrome")

#Write a program to check whether a number is present in given list
l=[23,67,12,90]
a=int(input("Enter the number: "))
if a in l:
    print("yes")
else:
    print("no")

#Write a program to check whether a key is present in a dictionary or not
d={101:'Arun',102:'Amal',103:'Anu'}
key=int(input("Enter the key: "))
if key in d.keys():
    print("present")
else:
    print("not present")

# #Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
passwrd=input("Enter the password: ")
if len(passwrd)>=8:
    print("strong")
else:
    print("weak")

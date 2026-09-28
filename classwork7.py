# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
# names = ['alin', 'arun', 'anu']
# print(list(map(lambda x:x.capitalize(),names)))

# 2.Append "@gmail.com" to a list of usernames
# users = ['user1', 'user2']
# print(list(map(lambda x:x+"@gmail.com",users)))
# 3.Filter out all empty strings from a list
# words = ['hello', ' ', 'world', ' ', 'python']
# print(list(filter(lambda x:x!=' ',words)))
# 4.Filter names that start with the letter 'A'
# names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# print(list(filter(lambda x:x.startswith('A'),names)))
# 5.Concatenate all strings in a list
# import functools
# words = ['Python', 'is', 'fun']
# print(functools.reduce(lambda x,y:x+y,words))

# 6.Multiply all numbers in a list
# import functools
# nums = [2, 3, 4]
# print(functools.reduce(lambda x,y:x+y,nums,0))

# 7.Extract First Character of Each Word
# words = ["apple", "banana", "cherry"]
# print(list(map(lambda x:x[0],words)))

# 8.Add 10 to Each Number
# nums = [5, 10, 15]
# print(list(map(lambda x:x+10,nums)))
# 9.Given a list
# l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers

import functools
# e=list(filter(lambda x:x%2==0 and x>0,l))
# print(e)
# print(functools.reduce(lambda x,y:x+y,e))
    # #Sum of Positive Odd numbers
# o=list(filter(lambda x:x%2!=0 and x>0,l))
# print(o)
# print(functools.reduce(lambda x,y:x+y,o))
    # #Sum of Negative  odd numbers
# no=list(filter(lambda x:x%2!=0 and x<0,l))
# print(no)
# print(functools.reduce(lambda x,y:x+y,no))
    # #Sum of Negative Even numbers
# eo=list(filter(lambda x:x%2==0 and x<0,l))
# print(eo)
# print(functools.reduce(lambda x,y:x+y,eo))
    # #Count of Positive numbers
# a=list(filter(lambda x:x>0,l))
# print(len(a))
    # #Count of negative numbers
# a=list(filter(lambda x:x<0,l))
# print(len(a))
# 10.Given a list
# nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
# print(list(map(lambda x:int(x),nums)))

# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
# print(list(map(lambda x:x['name'].upper(),p)))
#print products with price greater than 10000
# print(list(filter(lambda x:x['price']>10000,p)))
#Find the total price of all products
# c=list(map(lambda x:x['price'],p))
# import functools
# print(functools.reduce(lambda x,y:x+y,c))
#or
# print(functools.reduce(lambda x,y:x+y['price'],p,0))
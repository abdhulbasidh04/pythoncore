#map()
# n=[1,2,3,4]
# find the square of a list using map()
# list
# print(list(map(lambda x:x*x,n)))
# tuple
# print(tuple(map(lambda x:x*x,n)))
# set
# print(set(map(lambda x:x*x,n)))

#create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda n:n**3,l)))

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda n:n**0.5,l)))

#create a new list of lengths
# colors=['red','green','blue','yellow','black']
#create a new list of first characters
# print(list(map(lambda n:n[0],colors)))

#create a new list of last characters
# print(list(map(lambda n:n[-1],colors)))

#create a new list of reverse of each element
# print(list(map(lambda n:n[::-1],colors)))

# Given a list
# l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda n:n+10,l)))

##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails
# print(list(map(lambda n:n['email'],l)))

# filter()
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda n:n%2==0,l)))

# givan a list
# l=[23,45,67,12,89,70]
# filter even values greater than 50
# print(list(filter(lambda n:n%2==0 and n>50,l)))

# given a list
# colors=['red','green','blue','yellow','orange']
# filter the colors whose length is greater than 5
# print(list(filter(lambda n:len(n)>5,colors)))
# filter color containing letter n
# print(list(filter(lambda x:'n' in x,colors)))
import functools
# l=[1,2,3,4]
# print(functools.reduce(lambda x,y:x+y,l,0))


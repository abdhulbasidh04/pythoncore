#list built-in
# given a list
l=[1,2,2,3,4,4,5,6]
#1  create a new list where key are numbers and values are number occurrence of each number
# new={}
# for i in l:
#     if i in new:
#         new[i]=new[i]+1
#     else:
#         new[i]=1
#     print(new)

#     #or
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)

#2 givem a list
# l=[11,34,78,23,90,25]
# find the largest num
# find the second largest
# find the smallest
# find the secomd smallest

# l.sort()
# print(sorted(l))
# print("Largest:", max(l))
# print("Second Largest:", l[-2])
# print("Smallest:", min(l))
# print("Second Smallest:", l[1])

# #3). Given a list
# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# # find the maximum salary
# # find the minimum age
# print("Maximum salary is",max(i[2] for i in l))
# print("Minimum age is",min(i[1] for i in l))

#4
# l=[23,45,67,12,90,78]
# # find the largest num,mallest num without using buit in method
# max=l[0]
# min=l[0]
# for i in l:
#     if i>max:
#         max=i
#     if  i<min:
#         min=i
# print('max number',max)
# print('min number',min)


#1given
# l=[1,1,2,3,3,4]
#remove the duplicates
# l = list(set(l))
# print(l)

#2 given a list
# l=[1,1,2,3,3,4]
# new = []
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
# remove duplicates without using set() order should be preserved
#3given 2 list
# l1={13,27,30,42,57}
# l2={13,57,89,33,80}
#find the common elements
# l1 = [13, 27, 30, 42, 57]
# l2 = [13, 57, 89, 33, 80]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))

# dictionary
# d={'name':'arun','age':23}
# print(d.get('name'))
# d.update({'place':'ekm','gender':'male'})
# print(d)
# d.popitem()
# print(d)
# d.pop('place')
# print(d)
# d.copy()
# print(d)
# d.clear()
# print(d)

# user defined
# define a function that takes a number as an argument and return its square
# def fun(n):
#     s=n*n
#     return s
# a=fun(5)
# print(a)

# using lambda
# a=lambda n:n*n
# print(a(5))

#sum of two numbers
# lambda n1,n2:n1+n2
# product of three numbers
# lambda n1,n2,n3:n1*n2*n3
# cube of a number
# lambda n:n**3
# first letter of a string
# a=lambda s:s[0]
# print(a('hello'))
# length of a string
# a=lambda s:len(s)
# print(a('hello'))
# reverse of a strings='hello'
# a=lambda s:s[::-1]
# print(a('hello'))
# name value from a dictionary
# a=lambda d:d['name']
# print(a({'name':'arun'}))
# second element from a list
# a=lambda l:l[1]
# print(a([1,2,3,4]))
# add 10 to a number
# a=lambda n:n+10
# print(a(5))


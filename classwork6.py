# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(n1,n2):
#     p=n1*n2
#     return p
# a=product(10,20)
# print(a)
# # Q2.Define a function that takes a string and returns number of vowels
# def string(s):
#     vowels="AEIOUaeiou"
#     count=0
#     for i in s:
#         if i in vowels:
#             count=count+1
#     return count
# a=string("python coding is easy")
# print(a)


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     a=l*b
#     return a
# ar=area(10,20)
# print(ar)
#
# # Q4.Define a function that takes a list of numbers and creates a new list#
# with even numbers and returns the new list
# def even(l):
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     return new

# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# e=even(l)
# print(e)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def sum(l):
#     new=[]
#     for i in l:
#         s=str(i)
#         sum=0
#         for j in s:
#             sum=sum+int(j)
#         new.append(sum)
#     return new
# a=sum(l)
# print(a)


#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list

# def new_list(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# l=[12,34,78,12,67,34,90,23]
# a=new_list(l)
# print(a)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements

# def new_list(l1,l2):
#     new=[]
#     for i in l1:
#         if i in l2:
#             new.append(i)
#     return new
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# a=new_list(list1,list2)
# print(a)



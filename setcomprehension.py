# given a string
# s='python coding is easy and fun'
# create a new list with only vowels
# new={i for i in s if i in 'AEIOUaeiou'}
# print(new)

# Dictionary comprehension
# given a list
# l=[1,2,3,4]
# create a new dictionary where keys are numbers and values are squares of each numbers
# new={i:i**2 for i in l}
# print(new)
# create a new dictionary where keys are numbers and values are cubes of each numbers
# new={i:i**3 for i in l}
# print(new)

# given aa list
# l=[10,20,30,40]
# create a new dictionary where keys are indexes and values are numbers
# new={i:l[i] for i in range(0,len(l)}
# print(new)

# split()
# s='hello world'
# for i in s.split():
#     print(i)

# s='python is a programming language'
# for i in s.split():
#     print(i)

#given a string
s='python coding is easy and fun'
# create a new dictionary where keys are words and values are length of each world
new={i:len(i) for i in s.split()}
print(new)

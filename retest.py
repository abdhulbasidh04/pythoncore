def fun(l):
    count={}
    for i in l:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print()
print(fun(l = [1, 2, 2, 3, 4, 2, 5, 3, 4, 6]))

#interpolstion search for non uniform array

def interpolation(list,n,item):
    low=0
    high=n-1
    count=0

    while low<high:
        pos = int(low + ((item - list[low]) / (list[high] - list[low])) * (high - low))
        count=count+1

        if list[pos]==item:
            return int(pos)

        elif item<list[pos]:
            high=int(pos)-1

        elif item>list[pos]:
            low=int(pos)+1
    print(count)
list=[1,3,5,14,21,25,26,27]
result=interpolation(list,len(list),27)
print('element present at position',result)




import math
def jumpsearch(list,n,item):

    step=int(math.sqrt(n))

    low=0
    high=low+step

    while list[high]<item:

        low=high
        high=high+step
        if(high>n-1):
            high=n-1

    for i in range(low, high+1):
        if(list[i]==item):
            return i
    return -1
list=[1,3,4,5,6,7,8,9,10,11,12,13]
result=jumpsearch(list,len(list),10)
if result==-1:
    print('not found')
else:
    print('found at',result)


import math
def search(list,n,item):
    step=int(math.sqrt(n))

    low=0
    high=low+step

    while  list[high]<item:

        low=high

        high=high+step
        if(high>n-1):
            high=n-1

    for i in range(low,high+1):
        if list[i]==item:
            return i
list=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
result=search(list,len(list),80)
print(result)


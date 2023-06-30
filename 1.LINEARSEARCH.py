def search(list,n,target):
    index=0
    for i in range(n):
        if list[i]==target:
            index=i
            return index
    return -1
list=[2,5,4,9,5,1,9,3]
result=search(list,len(list),1)
if result==-1:
    print('element not found')
else:
    print('element present at ',result)
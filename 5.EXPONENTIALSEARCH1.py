def binarysearch(list,l,r,item):
    while l<r:
        mid=int((l+r)/2)

        if list[mid]==item :
            return mid

        elif item<list[mid]:
            r=mid-1
        elif item>list[mid]:
            l=mid+1


def exponentialsearch(list,n,item):
    if list[0]==item:
        return 0
    i=1
    while i<n and list[i]<item:
        i=i*2

        result=binarysearch(list,int(i/2),min(i,n-1),item)
        return result


list=[1,2,3,4,5,6,7,8,9,10,11,12]
result=exponentialsearch(list,len(list),11)
print('element present at',result)
def binarysearch(list,l,r,item):


    while l<=r:

        mid=int((l+r)/2)

        if(list[mid]==item):
            return mid

        elif(item<list[mid]):
            r=mid-1

        elif(item>list[mid]):
            l=mid+1
list=[10,20,30,40,50,60,70]
result=binarysearch(list,0,len(list),60)
print(result)
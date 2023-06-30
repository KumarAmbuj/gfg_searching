def binarysearch(list,l,r,item):
    if(l<r):
        mid = int((l + r) / 2)

        if list[mid] == item:
            return mid

        elif item < list[mid]:
            return binarysearch(list, l, mid - 1, item)

        elif item > list[mid]:
            return binarysearch(list, mid + 1, r, item)
    else:
        return -1



list=[10,20,30,40,50,60,70,80]
result=binarysearch(list,0,len(list),70)
print(result)
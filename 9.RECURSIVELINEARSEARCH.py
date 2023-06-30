def reclinsearch(arr,l,r,x):
    if r<l:
        return -1
    if arr[l]==x:
        return l
    if arr[r]==x:
        return r
    return reclinsearch(arr,l+1,r-1,x)

list=[12,34,54,2,3]
index=reclinsearch(list,0,len(list)-1,7)

if index!=-1:
    print('element found at index {}'.format(index))
else:
    print('element not found')
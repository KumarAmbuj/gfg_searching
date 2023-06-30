#fibonacci search
def fibonaccisearch(arr,x,n):
    fibMm1=0
    fibMm2=1
    fibM=fibMm1+fibMm2
    while(fibM<n):
        fibMm2=fibMm1
        fibMm1=fibM
        fibM=fibMm1+fibMm2

    offset=-1

    while(fibM>0):

        i=min((fibMm2+offset),n-1)

        if arr[i]==x:
            return i
        elif(arr[i]<x):
            fibM=fibMm1
            fibMm1=fibMm2
            fibMm2=fibM-fibMm1
            offset=i
        elif(arr[i]>x):
            fibM=fibMm2
            fibMm1=fibMm1-fibMm2
            fibMm2=fibM-fibMm1

list=[10,22,35,40,45,50,80,82,85,90,100]
result=fibonaccisearch(list,85,len(list))
print(result)


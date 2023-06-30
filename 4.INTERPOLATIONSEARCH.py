#interpolation search for unifrom array

def interpolationsearch(list,n,item):
    low=0
    high=n-1

    pos=low+ ((item-list[low])/(list[high]-list[low]))*(high-low)

    print('element present at position ',int(pos))

list=[1,3,5,7,9,11,13,15]
interpolationsearch(list,len(list),7)


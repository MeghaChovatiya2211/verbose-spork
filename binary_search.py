#python program for binary search
#for binary searc the list should be sorted

def binarysearch(seq,x,start,end):

    if (start-end==0):
        return False

    mid=int((end+start)/2)
    
    #print(type(x))
    #print(type(seq[mid]))
    
    if seq[mid]==x:
        return True
    elif x < seq[mid]:
        binarysearch(seq,x,start,mid)
    else:
        binarysearch(seq,x,mid+1,end)

#main program

size=int(input("enter list size"))
print("enter list elements in ascending order")
seq=[]
for i in range(0,size):
    temp=int(input())
    seq.append(temp)

x=int(input("enter element to be searched"))
ans=binarysearch(seq,x,0,size)

if ans is True:
    print(str(x)+" is present in the list")
else:
    print(str(x)+" is absent in the list")
    
    
    
    

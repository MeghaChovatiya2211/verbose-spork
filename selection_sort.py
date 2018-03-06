#python program for selection sort

def selection_sort(l):
    for i in range(0,len(l)-1):
        small=l[i]
        for j in range(i,len(l)):
            if l[j]<small:
                small=l[j]
        index=l.index(small)
        temp=l[i]
        l[i]=small
        l[index]=temp
    
    return(l)

#main program
size=int(input("enter list size"))
l=[]
print("enter list elements")
for i in range(0,size):
    temp=int(input())
    l.append(temp)
ans=selection_sort(l)
print(ans)

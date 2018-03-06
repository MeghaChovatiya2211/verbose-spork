
#python program for selection sort

def selection_sort(l):
    for i in range(0,len(l)-1):
        small=l[i]
        
        for j in range(i,len(l)):#find the minimum value n list
            if l[j]<small:
                small=l[j]
        index=l.index(small)
        (l[i],l[index])=(l[index],l[i])  #swap elements
    
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

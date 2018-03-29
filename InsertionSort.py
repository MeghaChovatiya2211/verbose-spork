#insertion sort complexity O(n^2)
#good only for very few elements in the list


def insertion_sort(a):
    for i in range(0,len(a)):
        for j in range(i,-1,-1):
           if a[j]<a[j-1]:
               a[j],a[j-1]=a[j-1],a[j]
               if j==1:
                 break
           else:
               break
    print(a)

#main program
size=int(input("enter list size : "))
a=[]
print("enter list elements :")
for i in range(0,size):
    a.append(int(input()))
   
insertion_sort(a)

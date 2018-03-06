#python program to find the smallest number in list
def smallest(l):
    small=l[0]
    for i in range(0,len(l)):
        if l[i]<small:
            small=l[i]
    return small

#python program to find the greatest number in list
def greatest(l):
    greatest=l[0]
    for i in range(0,len(l)):
        if l[i]>greatest:
            greatest=l[i]
    return greatest

#main program
size=int(input("enter list size"))
l=[]
print("enter list elements")
for i in range(0,size):
    temp=int(input())
    l.append(temp)

choice=int(input("enter your choice (1)find the smallest no (2)find greatest number"))
if choice==1:
      ans=smallest(l)
      print(ans)
else:
    ans=greatest(l)
    print(ans)


#python program to check if the list elements are alternating

def alternating(a):
    temp=0

    if len(a)==1: # returns ture if there is only one element in the list
        return True
    
    if a[0]<a[1]:
        flag=1
    else:
        flag=0 #a[0]>a[1]

    for i in range(1,len(a)-1):
        if flag==1:
            if a[i]<=a[i+1]:
                temp=-1
                break
            else:
                flag=0
        elif flag==0:
             if a[i]>=a[i+1]:
                 temp=-1
                 break
             else:
                 flag=1
    if temp==-1:
        return False
    else:
        return True
    
#main program
size=int(input("enter size of a list :"))

print("enter list elements : ")
l=[]
for i in range(0,size):

    temp1=input()
    l.append(temp1)

print("entered list is :" +str(l))
list1=alternating(l)
print(list1)

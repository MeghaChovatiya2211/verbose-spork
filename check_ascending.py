def ascending(l):
    flag=0
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            flag=flag-1
        else:
            flag=flag+1
    if flag==len(l)-1:
        return True
    else:
        return False
    
        
    

    

size=int(input("enter size of a list :"))

print("enter list elements : ")

l=[]



for i in range(0,size):

    temp1=input()

    l.append(temp1)



print("entered list is :" +str(l))
list1=ascending(l)
print(list1)

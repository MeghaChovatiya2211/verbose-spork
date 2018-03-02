#python program to rotate a list left based on a number entered by a user
##write a python program to rotate list

def rotatelist(l,k):

    for i in range(0,k):
        temp=l[-1]
        for j in range(len(l)-1,0,-1):
            l[j]=l[j-1]
        l[0]=temp
        
    return(l)
#main program
k=int(input("enter a number to rotate list :"))
size=int(input("enter size of a list :"))
print("enter list elements : ")
l=[]

#input list elements frm user
for i in range(0,size):
    temp1=input()
    l.append(temp1)

#call function 
print("entered list is :" +str(l))
list1=rotatelist(l,k)
print("list after rotation of "+str(k)+" number of times is "+str(list1))




              

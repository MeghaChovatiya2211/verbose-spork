#check if the entered list is ascending 

def ascending(l):
   
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            return False
        return True 
        
    

#main program     
size=int(input("enter size of a list :"))
print("enter list elements : ")
l=[]

for i in range(0,size):
    temp1=input()
    l.append(temp1)

print("entered list is :" +str(l))
list1=ascending(l)

if list1 is True:
	print("list is ascending")
else:
	print("list is not ascending")


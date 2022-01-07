list1=[]
positive1=[]
num=int(input('enter the total number of list elements:'))
for i in range(1,num+1):
    value=int(input("element {} is:".format(i)))
    list1.append(value)
    #print(list1)
for j in list1:
       if(j>0):
            positive1.append(j)
print("positive list is:",positive1)
            
              
            
    
    

    
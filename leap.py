start=int(input("enter the starting year"))
end=int(input("enter the last year"))
for i in range(start,end):
    if(i%4==0):
        if(i%100==0):
            if(i%400==0):
                print("{} is aleap year".format(i))
            
        else:
         print("{} is a leap year".format(i))
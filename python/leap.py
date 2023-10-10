# year=int(input("enter a year "))
# if(year %100==0) and (year %400==0):
#     print("it is leap year",year)
# elif(year %100!=0) and (year %4==0):  
#     print("it is leap year",year)  
# else:    
    # print("it is not leap year")    

    #case 1
    #if its century year  that must be divisible by 400

    #case 2
    #if year is not century that must be divisible by 4




year=int(input("enter a year"))
if(year %100==0) and (year%400==0):
    print("It is a leap year")
elif(year %100!=0)and(year%4==0):
    print("It is a leap year")
else:
    print("It is not a leap year")
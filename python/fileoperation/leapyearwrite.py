fw=open("C:\\Users\\Hamad\\Desktop\\python\\fileoperation\\years.txt","r")
lw=open("C:\\Users\\Hamad\\Desktop\\python\\fileoperation/leapyears.txt","w")
for year in fw:
    year=int(year)
    if (year%100==0) and (year%400==0):
      lw.write(str(year)+"\n")
    elif(year%100!=0)and(year%4==0):
       lw.write(str(year)+"\n")
                              
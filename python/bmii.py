height=float(input("enter your height"))
weight=float(input("enter your weight"))
height_mtr=height/100
bmi=weight//height_mtr**2
print(bmi)
if(bmi<20):
    print("underweight")
elif(bmi<25):
    print("normal weight")
elif(bmi<30):
    print("pre obesity")
else:
    print("obesity")      

    #print 3  numbers and check greatest among them    
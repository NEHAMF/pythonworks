# try:
#     x=int(input("enter a number"))
#     y=int(input("enter other number"))
#     z=x/y
#     print(z)
# except:
#     print("enter a valid number")    


while True:
 try:
    x=int(input("enter a number"))
    if x%2==0:
       print("x is an even number")
       break
    else:
       print("x is not an even number")
 except ZeroDivisionError:
    print("zero cannot be divided")
 except TypeError:
    print("rnter a crct va")
 except ValueError:
    print("Enter a valid num")    
 finally:
    print("thank u")    


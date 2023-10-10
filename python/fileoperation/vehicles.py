f=open("C:\\Users\\Hamad\\Desktop\\python\\fileoperation\\numbers.txt")
all_numbers=[i.rstrip("/n")for i in f]
print(all_numbers)
kl_numbers=[num for num in all_numbers if num.startswith("kl")]
print(kl_numbers)
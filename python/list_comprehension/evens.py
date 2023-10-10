lst=[7,9,5,4.,3,8]
evens=[i for i in lst if i%2==0]
print(evens)
odds=[i for i in lst if i%2!=0]
print(odds)
num_gtfive=[i for i in lst if i>=5]
print(num_gtfive)
lst=[9,6,8,2]
squares=[i**2 for i in lst ]
print(squares)
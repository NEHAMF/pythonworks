text="hello hai hello hai"
word_count={}
words=text.split(" ")
# print(words)
for w in words:
    if w in word_count:
     word_count[w]+=1  
    else:
       word_count[w]=1
print(word_count)  
# word_count={}




# []>list
# {}>set/empty dictionary
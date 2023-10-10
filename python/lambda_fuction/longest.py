text="hello hai hi goodafternoon"
words=text.split(" ")
# l_word=max(words,key=lambda n:len(n))
# print(l_word)
# # word=min(words,key=lambda w:len(w))
# # print(word)
srt=sorted(words,reverse=True,key=lambda w:len(w))
print(srt)
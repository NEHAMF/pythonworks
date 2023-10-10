text="python is a programming language"
# count_consonants=0
# count_vowels=0
vowels="aeiou"
words=text.split()
for w in words:
    # print(w)
    if w.casefold().startswith(vowels):
      print(w)
# for i in text:
#     if i in vowels:
#         count_vowels+=1
#     else:
#         count_consonants+=1 
# pr           


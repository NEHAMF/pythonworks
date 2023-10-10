text="pythonisanprogramminglanguage255255"
print(len(text))
count_vowels=0
count_consonants=0
# count_num=0
vowels="aeiouAEIOU"
for i in text:
    if i in vowels:
        count_vowels+=1
    else:
      count_consonants+=1
     
print(count_vowels)
print(count_consonants)        
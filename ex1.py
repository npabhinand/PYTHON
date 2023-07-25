# digit to word conversion
dict={"1":"one",
      "2":"two",
      "3":"three",
      "4":"four",
      "5":"five"}
ph=input("phone: ")
word=[]
for i in ph:
    if i in dict:
        word.append(dict[i])
print(word)
    



#emoji converter
dict={':)':'😀'
      ,':(':'😞'}

em=input(">")
em=em.split(' ')
for i in (0,len(em)-1):
    if em[i] in dict:
        em[i]=dict[em[i]]
result=' '.join(em)
print(result)
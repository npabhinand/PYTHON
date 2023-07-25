# function 
def convert(message):
    words=message.split(' ')
    dict={':)':'😀'
      ,':(':'😞'}
    # sent=''
    for i in range(0,len(words)):
        if words[i] in dict:
            words[i]=dict[words[i]]
    sent=' '.join(words)
    return sent
mess=input(">")
print(convert(mess))
   
    
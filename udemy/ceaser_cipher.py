
def ceaser_cipher(alphabet,message,shift,direction):
    cipher_message=""
    for i in message:
        if i in alphabet:
            index=alphabet.index(i)
            if direction=="encode":
                new_index=(index+shift)%len(alphabet)
                cipher_message+=alphabet[new_index]
            else:
                new_index=(index-shift)%len(alphabet)
                cipher_message+=alphabet[new_index]
    return cipher_message



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type encode to encrypt. type decode to decrypt \n")
message=input("Type your message \n").lower()
shift=int(input("Type shift Number \n"))
message=list(message)
print(ceaser_cipher(alphabet,message,shift,direction))


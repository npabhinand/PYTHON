
def encrypt(alphabet,message,shift):
    cipher_message=""
    for i in message:
        if i in alphabet:
            index=alphabet.index(i)
            new_index=(index+shift)%len(alphabet)
            cipher_message+=alphabet[new_index]
    return cipher_message
def decrypt(alphabet,message,shift):
    cipher_message=""
    for i in message:
        if i in alphabet:
            index=alphabet.index(i)
            new_index=(index-shift)%len(alphabet)
            cipher_message+=alphabet[new_index]
    return cipher_message
    


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type encode to encrypt. type decode to decrypt \n")
message=input("Type your message \n").lower()
shift=int(input("Type shift Number \n"))
message=list(message)
if direction=="encode":
    print(encrypt(alphabet,message,shift))
else:
    print(decrypt(alphabet,message,shift))


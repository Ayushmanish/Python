alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    newmessg=""
    for i in text:
        if(i in alphabet):
            pos=alphabet.index(i)
            pos1=(pos+shift)%26
            # if(pos1>25):
            #  x=alphabet[pos1-26]
            # else:
            #  x=alphabet[pos1] #maan lo ki agar shift kafi bada hota like 43
            x=alphabet[pos1]
            newmessg+=x
        else:
           newmessg+=i
    print(f'the encoded text is:{newmessg}')


def decrypt(text,shift):
    newmessg=""
    for i in text:
        if(i in alphabet):
           pos=alphabet.index(i)
           pos1=(pos-shift)%26
        #    if(pos1<=0):
        #     x=alphabet[26+pos1]  #kyonki pos1 khud hi negative hai, toh ultimately 26-pos1 hojayega
        #    else:
        #     x=alphabet[pos1]
           x=alphabet[pos1] 
           newmessg+=x
        else:
           newmessg+=i
    print(f'the decoded text is:{newmessg}')

ask='yes'
while(ask=='yes'):
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
   text = input("Type your message:\n").lower()
   shift = int(input("Type the shift number:\n"))
   if(direction=='encode'):
    encrypt(text,shift)
   elif(direction=='decode'):
    decrypt(text,shift)
   ask=input('want to continue:yes/no?')
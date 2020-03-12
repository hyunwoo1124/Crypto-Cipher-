def vigenereEnc(plaintext,key):
    index = 0
    i=0
    #store all char values from the ASCII position
    encString = []
    for index in range(len(plaintext)):
        #Gets the individual char from the plaintext and key strings
        textPos = plaintext[index]
        lengthkey =len(key)
        if i == lengthkey:
            i=0
            keyPos = key[i]
        else:
            keyPos = key[i]

        #Look at ASCII position of the Plaintext + ASCII Position of the Key mod 26 because there are 26 letters in the alphabet 
        posLetter = (ord(textPos)+ord(keyPos)) % 26

        #posLetter now gets its new position from the first ASCII value
        posLetter += ord("a")

        #we turn the ASCII value back to the char and add it to the list encString
        encString.append(chr(posLetter))
    return ("".join(encString))

########################################################################
#Vigenere Decryption
#Takes in a ciphertext string and key string and turns into dencrypted code
########################################################################
def vigenereDec(ciphertext,key):
    index = 0
    i=0
    #store all char values from the ASCII position
    decString = []
    for index in range(len(ciphertext)):
        #Gets the individual char from the plaintext and key strings
        textPos = ciphertext[index]
        lengthkey =len(key)
        if i == lengthkey:
            i=0
            keyPos = key[i]
        else:
            keyPos = key[i]

        #Look at ASCII position of the Plaintext - ASCII Position of the Key mod 26 because there are 26 letters in the alphabet
        posLetter = (ord(textPos)-ord(keyPos)+26)%26

        #posLetter now gets its position from the first ASCII value
        posLetter += ord("a")

        #we turn the ASCII value back to the char and add it to the list deccString
        decString.append(chr(posLetter))
    return ("".join(decString))
   
plaintext ="helloworld"
key="cat"

encrypt=vigenereEnc(plaintext,key)
print(encrypt)
decrypt=vigenereDec(encrypt,key)
print(decrypt)


def MonoalphabeticDec(ciphertext, key):
    key.lower()
    if len(key) != 26:
        print ("Please enter 26 key for this cipher")

    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherAlphabet = key
    decryptmessage = []
    for i in range(len(ciphertext)):
        for j in range(len(Alphabet)):
            if  cipherAlphabet[j] == ciphertext[i]:
                decryptmessage.append(Alphabet[j])
                break
    return ("".join(decryptmessage))

def MonoalphabeticEnc(plaintext, key):
    key.lower()
    if len(key) != 26:
        print ("Please enter 26 key for this cipher")
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherAlphabet = key
    encryptmessage = []
    for i in range(len(plaintext)):
        for j in range(len(Alphabet)):
            if  Alphabet[j] == plaintext[i]:
                encryptmessage.append(cipherAlphabet[j])
                break
    return ("".join(encryptmessage))
    
key  = "fghijklabcdemnopqrstuvwxyz"
plaintext = "hello dsadasas world"

encrypted = MonoalphabeticEnc(plaintext,key)
print (encrypted)
decrypted = MonoalphabeticDec(encrypted, key)
print (decrypted)
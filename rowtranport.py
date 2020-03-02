
def dec(ciphertext, key):
    key.lower()
    Aphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherAphabet = key + Aphabet
    decryptmessage = []
    for i in range(len(ciphertext)):
        for j in range(len(Aphabet)):
            if  cipherAphabet[j] == ciphertext[i]:
                decryptmessage.append(Aphabet[j])
                break
    return ("".join(decryptmessage))

def Monoalphabetic(plaintext, key):
    key.lower()
    Aphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherAphabet = key + Aphabet
    encryptmessage = []
    for i in range(len(plaintext)):
        for j in range(len(Aphabet)):
            if  Aphabet[j] == plaintext[i]:
                encryptmessage.append(cipherAphabet[j])
                break
    return ("".join(encryptmessage))
    
key  = "test"
plaintext = "helloworld"

encrypted = Monoalphabetic(plaintext,key)
print (encrypted)
decrypted = dec(encrypted, key)
print (decrypted)
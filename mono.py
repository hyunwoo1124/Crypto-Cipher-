import argparse
def main():
    parser = argparse.ArgumentParser(description="Five Classic Ciphers.")
    parser.add_argument('-C', '--Cipher', type = str, metavar='', required=True, help ='Choose Cipher: PLF, RTS, RFC, VIG, CES')
    parser.add_argument('-K', '--Key', type = str, metavar='', required=True, help ='Your Key to encrypt or decrypt')
    parser.add_argument('-T', '--Type', type = str, metavar='', required=True, help ='Encrypt: ENC or Decrypt: DEC')
    parser.add_argument('-I', '--Input', type = str, metavar='', required=True, help ='The file from which to read the input.')
    parser.add_argument('-O', '--Output', type = str, metavar='', required=True, help ='The file to which the output shall be written.')
    args = parser.parse_args()
    print(args)
    return args

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
plaintext = "helloworld"

encrypted = MonoalphabeticEnc(plaintext,key)
print (encrypted)
decrypted = MonoalphabeticDec(encrypted, key)
print (decrypted)

   if (args.Cipher == 'MAC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = MonoalphabeticEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)



   if (args.Cipher == 'MAC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = MonoalphabeticDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)

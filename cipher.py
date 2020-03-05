#!/usr/bin/python3

#parser that allows cmd line to take argument into the program
import argparse
#from itertools import cycle
#while (!success) { success = try() }
# that up there gents is the key to get a job at FANG
#Implementing flags...
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

# it shall be playfair(), vignere() and more

# Definitions to be implemented...

def info():
    print("The Classic 5 Cryptography Ciphers\n")
    print("Cipher Name: Is the name of the cipher. Valid names are:\n")
    print("\t -PLF: Playfair\n")
    print("\t -RTS: Row Trasposition\n")
    print("\t -RFC: Railfence\n")
    print("\t -VIG: Vigenre\n")
    print("\t -CES: Caesar\n")
    print("\nFormat: ./cipher  -C <CIPHERNAME> -K <KEY> -T <ENC/DEC>  -I <INPUTFILE> -O <OUTPUTFILE>\n")
    print("\nUse the flag -h to get help if needed...\n")

# This module takes the plaintext and key to encrypt into ciphertext
def RailfenceEnc(plaintext, key):

    result = ""

    #Creating a Matrix with for loop to expand the matrix
    #matrix = [["\n" for x in range(len(plaintext))] for y in range(key)]
    
    # The key index
    keyOffset = 0
    
    index = 0
    
    intKey = int(key)

    #key = int(args.Key)
    #key = 3
    #plaintext = "helloworld"
    while keyOffset < intKey:
               
        index = keyOffset

        while index < len(plaintext):
        
           if len(plaintext) > index:
               result += plaintext[index]

               index += intKey
        
        keyOffset += 1
        index = 0

    return result
   
# This module takes the ciphertext and key to decrypt into plaintext
def RailfenceDec(ciphertext, key):

    #length of key
    # should be ciphertext // key but ours have an input key section
    keyLength = int(key)
    key = int(key)

    #Remainder of key length with modulus
    keyRemainder = len(ciphertext) % key

    keylengths = key * [keyLength]

    for i in range(0, keyRemainder):
        keylengths[i] += 1
    keylengths.reverse()

    rails =[]

    for length in keylengths:
        length.append(ciphertext[0:length])
        ciphertext = ciphertext[length:]
    rails.reverse()

    string = ''

    for i in range(keylengths + 1):
        for rail in rails:
            if len(rail) > i:
                string += rail[i]
    return string
    
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


def menu_switch(args):
   if (args.Cipher == 'RFC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = RailfenceEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)
   if (args.Cipher == 'RFC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = RailfenceDec(rf.read(),args.Key)
            with open(args.Input, 'a') as wf:
                wf.write(answer)
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
                

if __name__ == '__main__':
    info()
    # Object of args passed into return value from main def
    args = main()
    menu_switch(args)

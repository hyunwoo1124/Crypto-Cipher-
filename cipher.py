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
    print("The Classic 6 Cryptography Ciphers\n")
    print("Cipher Name: Is the name of the cipher. Valid names are:\n")
    print("\t -PLF: Playfair\n")
    print("\t -RTS: Row Trasposition\n")
    print("\t -RFC: Railfence\n")
    print("\t -VIG: Vigenre\n")
    print("\t -CES: Caesar\n")
    print("\t -MAC: Monoalphabetic Cipher\n")
    print("\nFormat: ./cipher  -C <CIPHERNAME> -K <KEY> -T <ENC/DEC>  -I <INPUTFILE> -O <OUTPUTFILE>\n")
    print("\nUse the flag -h to get help if needed...\n")

'''
Monoalphabetic Cipher will take in 2 variable
Key = random alphabet order
example: fghijklabcdemnopqrstuvwxyz
plaintext for Encryption
ciphertext for Decryption
'''
# For Encryption, user will pass in a plain text and a key
def MonoalphabeticEnc(plaintext, key):
    #plaintext will be convert to lowercase for easy print result
    key.lower()

    #we required 26 unique key for this ciper
    if len(key) != 26:
        print ("Please enter 26 key for this cipher")
    else:
        #first we will inital an alphabet to encrypt plaintext
        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #Key is consider as cipherAlphabet cause the order is random
        cipherAlphabet = key
        #We will store encrypted character into an array encryptmessage
        encryptmessage = []
        #First, we will loop through the length of plaintext
        for i in range(len(plaintext)):
            #While looping through length of plaintext, we will loop through Alphabet
            for j in range(len(Alphabet)):
                #if we find a match of plaintext and alphabet
                if  Alphabet[j] == plaintext[i]:
                    #We will use the index found in the alphabet and search through our cipherAlphabet
                    #Then, we will pull out the character in cipherAlphabet where index = alphabet index
                    #and save it into encryptmessage
                    encryptmessage.append(cipherAlphabet[j])
                    #Once we found a index position we can break from alphabet loop and continue with plaintext loop
                    break
        #merge character in the array encryptmessage into a string
        return ("".join(encryptmessage))

def MonoalphabeticDec(ciphertext, key):
    #ciphertext will be convert to lowercase for easy print result
    key.lower()
    #we required 26 unique key for this cipher
    if len(key) != 26:
        print ("Please enter 26 key for this cipher")
    else: 
        #first we will inital an alphabet to decrypt ciphertext
        Alphabet = 'abcdefghijklmnopqrstuvwxyz'
        #Key is consider as cipherAlphabet cause the order is random
        cipherAlphabet = key
        #We will store decrypted character into an array decryptmessage
        decryptmessage = []
        #First, we will loop through the length of ciphertext
        for i in range(len(ciphertext)):
            #While looping through length of ciphertext, we will loop through cipherAlphabet
            for j in range(len(Alphabet)):
                #if we find a match of ciphertext and cipherAlphabet
                if  cipherAlphabet[j] == ciphertext[i]:
                    #We will use the index found in the cipherAlphabet and search through our Alphabet
                    #Then, we will pull out the character in Alphabet where index = cipherAlphabet index
                    #and save it into decryptmessage
                    decryptmessage.append(Alphabet[j])
                    #Once we found a index position we can break from alphabet loop and continue with ciphertext loop
                    break
        #merge character in the array decryptmessage into a string
        return ("".join(decryptmessage))

def menu_switch(args):
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

#!/usr/bin/python3

#parser that allows cmd line to take argument into the program
import argparse
#from itertools import cycle
#while (!success) { success = try() }
# that up there gents is the key to get a job at FANG
#Implementing flags...
def main():
    parser = argparse.ArgumentParser(description="Five Classic Ciphers.")
    parser.add_argument('-C', '--Cipher', type = str, metavar='', required=True, help ='Choose Cipher: PLF, RTS, RFC, VIG, CES, MAC')
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
    print("\t -MAC: Mono-Alphabetic\n")

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

    #print(result)
    #exit(1)
    """
    # intiail variable to further use for the next code
    increment = 1
    row, col = 0, 0

    for character in plaintext:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = character
        # add the increment for each row and col
        row += increment
        col += 1
    for list in matrix:
        #connecting each character one by one from the matrix; concatenating
        result += "".join(list)
    return result 
    """
   
# This module takes the ciphertext and key to decrypt into plaintext
def RailfenceDec(ciphertext, key):

    #length of the fence
    intKey = int(key)
    #Getting the char length
    keyLength = len(ciphertext) // intKey 
    #Getting the remainder of char length
    keyRemainder = len(ciphertext) % intKey
    #container
    totalLength = intKey * [keyLength]

    for i in range(0, keyRemainder):
        totalLength[i] += 1
    #After this you will get 4 3 3 if its helloworld
    #It is correct. I don't know why you need to reverse it because when you reverse it will be 3 3 4
    #it will mess up your string order
    #totalLength.reverse()
    storingChar = []
    for length in totalLength:
        storingChar.append(ciphertext[0:length])
        ciphertext = ciphertext[length:]
    #storingChar.reverse()
    #you will get 
    # hlod eor lwl which is correct
    # reverse will change to lwl eor hlod 
    # when you merge the string it will not be decrypting, it will create some new string text
    decrypted = ''
    #ERROR here because totalLength is an array kinda
    #array cant + 1. 
    #len(totalLength) + 1 look right
    mylength = len(totalLength)
    for i in range(mylength + 1):
        for char in storingChar:
            if len(char) > i:
                decrypted += char[i]
    return decrypted

# For Encryption, user will pass in a plain text and a key
def MonoalphabeticEnc(plaintext, key):
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
    if (args.Cipher == 'RFC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = RailfenceEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)
            # Alex write yourc cod here
      
    if (args.Cipher == 'RFC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = RailfenceDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
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

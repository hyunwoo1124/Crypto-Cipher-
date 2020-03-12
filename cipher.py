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
    print("\t -VIG: Vigenere\n")
    print("\t -CES: Caesar\n")
    print("\nFormat: ./cipher  -C <CIPHERNAME> -K <KEY> -T <ENC/DEC>  -I <INPUTFILE> -O <OUTPUTFILE>\n")
    print("\nUse the flag -h to get help if needed...\n")


########################################################################
#Vigenere Encryption
#Takes in a plaintext string and key string and turns into encrypted code
########################################################################
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
        posLetter = (ord(textPos) - 97 + ord(keyPos) - 97) % 26

        #posLetter now gets its new position from the first ASCII value
        posLetter += ord("a")

        #we turn the ASCII value back to the char and add it to the list encString
        encString.append(chr(posLetter))

        i+=1

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
        posLetter = ((ord(textPos) - 97) - (ord(keyPos) - 97) + 26) % 26
	
        #print((ord(textPos) - 97) - (ord(keyPos) - 97), end=" ")
        #print(keyPos)
	
		
        #print(posLetter)
        #posLetter now gets its position from the first ASCII value
        posLetter += ord("a")

        #we turn the ASCII value back to the char and add it to the list deccString
        decString.append(chr(posLetter))
        i+= 1
    return ("".join(decString))
   
def menu_switch(args):
    if (args.Cipher == 'VIG' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = vigenereEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)  

    if (args.Cipher == 'VIG' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = vigenereDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)

if __name__ == '__main__':
    info()
    # Object of args passed into return value from main def
    args = main()
    menu_switch(args)
    #print(vigenereDec(vigenereEnc("helloworld","cat"), "cat"))


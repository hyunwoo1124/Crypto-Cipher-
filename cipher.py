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
        posLetter = ((ord(textPos)-ord(keyPos))+26)%26

        #posLetter now gets its position from the first ASCII value
        posLetter += ord("a")

        #we turn the ASCII value back to the char and add it to the list deccString
        decString.append(chr(posLetter))
    return ("".join(decString))
   
   
    #Since we dont konw the  exact key at the moment we need
    #Boolean function to determine if its end of the row or 
    #the place value of the column
    '''
    result = []
    #The Matrix for the railfence decrypt
    matrix= [["" for x in range(len(ciphertext))] for y in range(key)]

    #Finding the correct direction of the position
    #initialize the Boolena and the position of row, col
    row, col = 0, 0
    goingDown = False

    for character in range(len(ciphertext)):
        #checking to see if the row is filled or not to the end
        if(row == 0) or (row == key-1):
            #checking the direction of the flow 
            # is it 0? 1 ,2 ,3? (row)
            goingDown = not goingDown

            #appending the characters
            matrix[row,col] = ciphertext[character]
            col += 1

            if goingDown:
                #Going to the next row incrementing
                row +=1
            else:
                #If not go up the row
                row -=1
    for col in range(key):
        for row in range(len(ciphertext)):
            if matrix[col, row] != "\n":
                result.append(matrix[col][row])
    return ("".join(result))
  '''

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

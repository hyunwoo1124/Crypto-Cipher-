#!/usr/bin/python3

#parser that allows cmd line to take argument into the program
import argparse
from math import floor, ceil

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


########################################################################
#Vigenere Encryption
#Takes in a plaintext string and key string and turns into encrypted code
########################################################################
def vigenereEnc(plaintext,key):
    index = 0
    #store all char values from the ASCII position
    encString = []
    for index in range(len(plaintext)):

        #Gets the individual char from the plaintext and key strings
        textPos = plaintext[index]
        keyPos = key[index]

        #Look at ASCII position of the Plaintext + ASCII Position of the Key mod 26 because there are 26 letters in the alphabet
        posLetter = (ord(textPos)+ord(keyPos)) % 26

        #posLetter now gets its new position from the first ASCII value
        posLetter += ord("A")

        #we turn the ASCII value back to the char and add it to the list encString
        encString.append(chr(posLetter))
        return encString

########################################################################
#Vigenere Decryption
#Takes in a ciphertext string and key string and turns into dencrypted code
########################################################################
def vigenereDec(ciphertext,key):
    index = 0
    #store all char values from the ASCII position
    decString = []
    for index in range(len(ciphertext)):

        #Gets the individual char from the plaintext and key strings
        textPos = ciphertext[index]
        keyPos = key[index]

        #Look at ASCII position of the Plaintext - ASCII Position of the Key mod 26 because there are 26 letters in the alphabet
        posLetter = (ord(textPos)-ord(keyPos)+26)%26

        #posLetter now gets its position from the first ASCII value
        posLetter += ord("A")

        #we turn the ASCII value back to the char and add it to the list deccString
        decString.append(chr(posLetter))
        return decString

    #Since we dont konw the  exact key at the moment we need
    #Boolean function to determine if its end of the row or
    #the place value of the column

########################################################################
#Row Transposition
#Takes in a plaintext string and key string and turns into encrypted code
########################################################################
def rowTranspositonEnc(plaintext,key):
    print("Row Transposition Encode")

    #initialize index for traversing ciphertext
    index = 0

    #Get string length for Row Transposition Matrix
    string_length = len(plaintext)
    key_length = len(key)

    #Get columns and rows for matrix
    row = ceil(string_length/key_length)
    column = key_length

    #Debug Outs
    # print("Plaintext: ", plaintext, "--length: ", string_length)
    # print("key: ", key, "--length: ", key_length)
    # print ("StringLength: ", string_length, ", Cols: ", column, ", Rows: ", row)

    if (row * column < string_length):
        row = column

    #initialize matrix with 0's
    matrix = [ [0 for j in range(column)] for i in range(row)]

    # convert the plaintext into grid
    for i in range(row):
        for j in range(column):
            #if index is bigger than plaintext length
            if index >= string_length:
                matrix[i][j] = " "
                index += 1
            else :
                matrix[i][j] = plaintext[index]
                index += 1

    print("\n--MATRIX--")
    # Printing the matrix out for reference
    for i in range(row):
        for j in range(column) :
            #end case
            if matrix[i][j] == " " :
                break
            print(matrix[i][j], end = "")
        print()
    print()

    result = ""

    #create ciphertext
    print("\n--RESULT--")
    for i in range(column):
        #print(key[i])
        for j in range(row):
            if matrix[j][int(key[i])-1] == " ":
                #print("x")
                result += "x"
            else:
                #print(matrix[j][int(key[i])])
                result += matrix[j][int(key[i])-1]

    #Print and return result
    print(result)
    return result

########################################################################
#Row Transposition
#Takes in a cipher string and key string and turns into decrypted code
########################################################################
# hell
# owor
# ld
def rowTranspositonDec(ciphertext,key):
    print("Row Transposition Decode")

    #initialize index for traversing ciphertext
    index = 0

    # Get row and column of matrix size
    column = len(key)
    row = floor(len(ciphertext)/column)

    # Debug print statements
    # print("ciphertext: ", ciphertext)
    # print ("Cols: ", column, ", Rows: ", row)

    #initialize matrix with 0's
    matrix = [ [0 for j in range(column)] for i in range(row)]

    #load in the ciphertext value into the matrix
    for i in range(column):
        for j in range (row):
            matrix[j][int(key[i])-1] = ciphertext[index]
            index += 1

    #define result to load decoded value into
    result = ""
    index = 0

    print("\n--MATRIX--")
    #Test Print Function
    for i in range(row):
        for j in range (column):
            if index % column == 0 and index != 0:
                print()
            print(matrix[i][j], end="")
            index += 1
            result += matrix[i][j]
    print()

    print("\n--RESULT--")
    #Print and return result
    print(result)
    return result

def menu_switch(args):
    if (args.Cipher == 'RFC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = RailfenceEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)

    if (args.Cipher == 'RFC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = RailfenceDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)

    # IF ROW TRANSPOSITION ENCODE
    if (args.Cipher == 'RTS' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = rowTranspositonEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)

    # IF ROW TRANSPOSITION DECODE
    if (args.Cipher == 'RTS' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = rowTranspositonDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)


if __name__ == '__main__':
    info()
    # Object of args passed into return value from main def
    args = main()
    menu_switch(args)

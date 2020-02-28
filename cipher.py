#!/usr/bin/python3

#parser that allows cmd line to take argument into the program
import argparse
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
    matrix = [["\n" for x in range(len(plaintext))] for y in range(key)]
    
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
# This module takes the ciphertext and key to decrypt into plaintext
def RailfenceDec(ciphertext, key):
    #Since we dont konw the  exact key at the moment we need
    #Boolean function to determine if its end of the row or 
    #the place value of the column

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
  
def menu_switch(args):
   if (args.Cipher == 'RFC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
          args.Output = RailfenceEnc(rf, args.Key)
          with open(args.output, 'a') as wf:
            print(wf)
            

   if (args.Cipher == 'RFC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            RailfenceDec(rf,args.Key)
        with open(args.Input, 'r') as rf:
            RailfenceDec(rf,args.Key)

if __name__ == '__main__':
    info()
    args = main()
    menu_switch(args)

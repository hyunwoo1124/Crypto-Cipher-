
#parser that allows cmd line to take argument into the program
import argparse
from math import floor, ceil


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

def playfairEnc(plaintext, key):
    pfkey=key
    pfkey=pfkey.replace(" ", "")
    pfkey=pfkey.upper()
    msg=plaintext
    msg=msg.upper()
    msg=msg.replace(" ", "")
    answer=str("")  

    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)]
        
    result=list()
    #storing key
    for c in pfkey: 
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    #filling in characters (ASCII)
    #I/J fixed
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    #matrix creation
    my_matrix=matrix(5,5,0) 
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    #get location of each character
    def locindex(c): 
        loc=list()
        #making sure J&I are the same
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc
        #add X if repeating character
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    #adding X if message is odd number of characters
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    i = 0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            answer=answer + ("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]))
        elif loc[0]==loc1[0]:
            answer=answer + ("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]))  
        else:
            answer=answer + ("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]))    
        i=i+2
    return answer

def playfairDec(ciphertext, key):
    pfkey=key
    pfkey=pfkey.replace(" ", "")
    pfkey=pfkey.upper()
    msg=ciphertext
    msg=msg.upper()
    msg=msg.replace(" ", "")
    answer=str("")              
    
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)]
        
    result=list()
    #storing key
    for c in pfkey: 
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    #filling in characters (ASCII)
    #I/J fixed
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    #matrix creation
    my_matrix=matrix(5,5,0) 
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    #get location of each character
    def locindex(c): 
        loc=list()
        #making sure J&I are the same
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            answer=answer + ("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]))
        elif loc[0]==loc1[0]:
            answer=answer + ("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]))  
        else:
            answer=answer + ("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]))    
        i=i+2  
    return answer

def CeasCrypt(plaintext, key):
    message = plaintext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "
    intKey = int(key)
    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + intKey) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter


    return result

def CeasDecrypt(ciphertext, key):
    message = ciphertext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "
    intKey = int(key)

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - intKey) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter


    return result

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

def rowTranspositonEnc(plaintext,key):

    if not (key.isdigit()):
        print("PLEASE ENTER VALID NUMBER KEY FOR ROW TRANSPOSITION")
        exit()

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

    # print("\n--MATRIX--")
    # # Printing the matrix out for reference
    # for i in range(row):
    #     for j in range(column) :
    #         #end case
    #         if matrix[i][j] == " " :
    #             break
    #         print(matrix[i][j], end = "")
    #     print()
    # print()

    result = ""

    #create ciphertext
    #print("\n--RESULT--")
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
    #print(result)
    return result

########################################################################
#Row Transposition
#Takes in a cipher string and key string and turns into decrypted code
########################################################################
# hell
# owor
# ld
def rowTranspositonDec(ciphertext,key):

    if not (key.isdigit()):
        print("PLEASE ENTER VALID NUMBER KEY FOR ROW TRANSPOSITION")
        exit()

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

    # print("\n--MATRIX--")
    #Test Print Function
    for i in range(row):
        for j in range (column):
            #if index % column == 0 and index != 0:
                # print()
            # print(matrix[i][j], end="")
            index += 1
            result += matrix[i][j]
    # print()

    # print("\n--RESULT--")
    #Print and return result
    # print(result)
    return result


def menu_switch(args):
    if (args.Cipher == 'RFC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = RailfenceEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)
               return(wf.name)
            # Alex write yourc cod here
      
    if (args.Cipher == 'RFC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = RailfenceDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)

    if (args.Cipher == 'MAC' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = MonoalphabeticEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)
                
    if (args.Cipher == 'MAC' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = MonoalphabeticDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)

    if (args.Cipher == 'PLF' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = playfairEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)
    if (args.Cipher == 'PLF' and args.Type == 'DEC'):
       with open(args.Input, 'r') as rf:
           answer = playfairDec(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)
    if (args.Cipher == 'CES' and args.Type == 'ENC'):
        with open(args.Input, 'r') as rf:
            answer = CeasCrypt(rf.read(), args.Key)
        with open (args.Output, 'a') as wf:
                wf.write(answer)
                return(wf.name)
                
    if (args.Cipher == 'CES' and args.Type == 'DEC'):
        with open(args.Input, 'r') as rf:
            answer = CeasDecrypt(rf.read(), args.Key)
        with open (args.Output, 'a') as wf:
                wf.write(answer)
                return (wf.name)
                
    if (args.Cipher == 'VIG' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = vigenereEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)  
               return(wf.name)


    if (args.Cipher == 'VIG' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = vigenereDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)
                return(wf.name)

    # IF ROW TRANSPOSITION ENCODE
    if (args.Cipher == 'RTS' and args.Type == 'ENC'):
       with open(args.Input, 'r') as rf:
           answer = rowTranspositonEnc(rf.read(), args.Key)
           with open (args.Output, 'a') as wf:
               wf.write(answer)
               return(wf.name)


    # IF ROW TRANSPOSITION DECODE
    if (args.Cipher == 'RTS' and args.Type == 'DEC'):
        with open(args.Input,'r') as rf:
            answer = rowTranspositonDec(rf.read(),args.Key)
            with open(args.Output, 'a') as wf:
                wf.write(answer)
                return(wf.name)


if __name__ == '__main__':
    info()
    # Object of args passed into return value from main def
    args = main()
    output = menu_switch(args)
    print("Your ENC/DEC file is {}...".format(output))

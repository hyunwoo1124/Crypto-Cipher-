# Convert ths letter to an alphabet position
# @param letter - the letter
# @return the letter 
def toAlphaPos(letter):

    return ord(letter) - 97

#####################################################
# Converts the letter alph position to a letter
# @param alpPos - the alphabet position of th eletter
# @return - the letter corresponding to the position
#####################################################
def alpPosToLetter(alpPos):
        
        return chr(alpPos + 97)

###################################
# @param key - the key
#



key = "hello"
index = 0

while True:
        
    print(key[index], end='')

    index = (index + 1) % len(key)

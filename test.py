def RailfenceEnc(plaintexts, key):
    result = ""

    #Creating a Matrix with for loop to expand the matrix
    matrix = [["\n" for x in range(len(plaintexts))] for y in range(key)]
    
    # intiail variable to further use for the next code
    increment = 1
    row, col = 0, 0

    for character in plaintexts:
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



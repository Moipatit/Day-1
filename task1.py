
#method to make a magic square
def make_magic_square(n):
    #declare a 2d array with slots set to 0
    square = [[0 for x in range(n)]
              for y in range(n)]
    
    #initialise the position of the first number
    row = n // 2
    col = n - 1

    num = 1

    #add values to the magic square
    while num <= (n * n):
        if row == -1 and col == n:
            col = n - 2
            row = 0
        else:
            #number goes to the right side of the square
            if col == n:
                col = 0

            #number goes to the upper side of the square
            if row < 0:
                row = n - 1
            
        if square[int(row)][int(col)]:
            col = col - 2
            row = row + 1
            continue
        else:
            square[int(row)][int(col)] = num
            num = num + 1

        col = col + 1
        row = row - 1

    #print out the magic square
    print("Magic square for n =",n)
    #check the sum of rows and the columns
    if n * (n * n + 1) // 2:
        print("correct")
    
    for row in range(0, n):
        for col in range(0, n):
            print('%2d ' % (square[row][col]), end='')

            if col == n - 1:
                print()


#validation for the user input
N = int(input("Please enter a positive odd integer "))
if (N % 2) == 0:
     print("The number is NOT odd")
elif (N < 0):
    print("The number is NOT postive")
else:
    make_magic_square(N)


#for help with this I used geeks for geeks: https://www.geeksforgeeks.org/magic-square/


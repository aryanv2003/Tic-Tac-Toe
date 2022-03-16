#author: Aryan Vahabpour
#date: 15th March 2022
import pygame

pygame.init()


#Variables:
sizeOfGrid = 3 #This the main size of Grid which is sizeOfGrid by sizeOfGrid
disp = pygame.display.set_mode ((800, 800))
done = False
sizeOfSquare = 140 #By changing the Variable you can change the size of squares
colorOfSquare = (255, 0, 0) #Can change the color of the squares by this
colorOfLetters = (0, 0, 255)#Can change the color of the letters with this
turn = 0 #This is to track whos turn is it, if 0 is X turn if 1 is O turn
grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]] #This is the list to track the squares (our dataBase) -1:not Occupied 0:Occupied by X, 1:Occupied by O
cour = pygame.font.Font('Anke.ttf', 50) #This is to pickup font and the size of Font
finalTextTie = cour.render('Finish, The Game is Tie', True, colorOfLetters)
finalTextXwin = cour.render('Finish, X wins the Game', True, colorOfLetters)
finalTextOwin = cour.render('Finish, O wins the Game', True, colorOfLetters)
listOfTurns = ['X', 'O']
#Functions:

def DrawTheGrid(): #This function is to draw our grid of Tic-Tac-Toe
    disp.fill((0, 0, 0))
    for i in range(9):
        startX = (sizeOfSquare + 10) * (i % sizeOfGrid) #The top left X coordinate of our square
        startY = (sizeOfSquare + 10) * (i // sizeOfGrid)#The top left y coordinate of our square
        pygame.draw.rect(disp, colorOfSquare, (startX, startY, sizeOfSquare, sizeOfSquare), 0) #draw the square
        if (grid[i % sizeOfGrid][i // sizeOfGrid] != -1): #check that it is occupied or not
            letter = cour.render(listOfTurns[grid[i % sizeOfGrid][i // sizeOfGrid]], True, colorOfLetters) #letter that should be printed in that square
            disp.blit(letter, (startX - 15 + sizeOfSquare // 2, startY - 15 + sizeOfSquare // 2)) #place the letter
            
    pygame.display.update()


def FindPressedSquare(x, y): #this Function recieves the coordinates that the user pressed and returns the square position which is pressed
    pos = [x // (sizeOfSquare + 10), y // (sizeOfSquare + 10)]
    return pos

def isVal(pos): #this Function checks that the pressed area is in bound or not
    return pos[0] < sizeOfGrid and pos[1] < sizeOfGrid and pos[0] >= 0 and pos[1] >= 0

def SearchForWinner():
    for i in range(sizeOfGrid): #Search for a row winner
        win = grid[i][0] #this is equal to the first element in each row and keep track of the row
        for j in range(sizeOfGrid): #check for row winning
            if (grid[i][j] == -1): #in case one of the squares is not filled this can't be end of the game
                win = -1 
            if (grid[i][j] != win): #in case two elements different in a row this can't be end of the game
                win = -1
        if (win != -1): #in case that our win is not 0 means that we have a row winner that we should announce
            return win
    for j in range(sizeOfGrid): # Search for a column winner
        win = grid[0][j] #this is equal to the first element in each column and keep track of the column 
        for i in range(sizeOfGrid):
            if (grid[i][j] == -1): #in case one of the squares is not filled this can't be end of the game
                win = -1
            if (grid[i][j] != win): #in case two elements different in a column this can't be end of the game
                win = -1
        if (win != -1): #in case that our win is not 0 means that we have a column winner that we should announce
            return win
    win  = grid[0][0] # Search for main diagonal winner
    for i in range(sizeOfGrid): 
        if (grid[i][i] == -1): #in case one of the squares is not filled this can't be end of the game
            win = -1
        if (grid[i][i] != win): #in case two elements different in a main diagonal this can't be end of the game
            win = -1
    if (win != -1): #in case that our win is not 0 means that we have a main diagonal winner that we should announce
        return win
    win = grid[0][2]
    for i in range(sizeOfGrid): 
        if (grid[i][2 - i] == -1): #in case one of the squares is not filled this can't be end of the game
            win = -1
        if (grid[i][2 - i] != win): #in case two elements different in a other diagonal this can't be end of the game
            win = -1
    if (win != -1): #in case that our win is not 0 means that we have a other diagonal winner that we should announce
        return win
    win = -1
    for i in range(sizeOfGrid):
        for j in range(sizeOfGrid):
            if (grid[i][j] == -1): # We still have an empty aquare
                return win
    return 3
    

while not done:
    for event in pygame.event.get():
        DrawTheGrid()
        if event.type == pygame.MOUSEBUTTONDOWN: #if out user has pressed the mousebutton we should take an action
            (xmouse,ymouse) = event.pos #find the place which is pressed
            pos = FindPressedSquare(xmouse,ymouse) #find the square which is pressed
            if (isVal(pos) and grid[pos[0]][pos[1]] == -1): #check that the square which is pressing is empty or not to avoid hacks
                grid[pos[0]][pos[1]] = turn #mutate the dataBase to keep track of the changes
                turn = (turn + 1) % 2 #update the turn
    result = SearchForWinner()
    if (result != -1): # We have find our final result
        disp.fill((0, 0, 0))
        DrawTheGrid() #draw the last view of our grid
        if (result == 3): #announce the results
            disp.blit(finalTextTie, (100, 500))
        if (result == 1): #announce the results
            disp.blit(finalTextOwin, (100, 500))
        if (result == 0): #announce the results
            disp.blit(finalTextXwin, (100, 500))
        pygame.display.update()
        done = True #finish our loop
            
                
                

        

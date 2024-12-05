import random

#creating the tic-tac-toe grid
def create_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

#printing the grid
def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell,end="|") #printing a seperator between cells
        print("\n","-"*5)    

#player's turn to enter the coordinates
def player_step(grid,symbol):
    while True:
        step=input("Enter the coordinates of the cell(b/w 0 to 2):")
        split_row_col=step.split()
        if len(split_row_col)!=2:
            print("Uh-oh!Enter coordinates properly as two digits")
            continue
        row=int(split_row_col[0])
        col=int(split_row_col[1])
        if 0<=row<=2 and 0<=col<=2:
            if grid[row][col] ==" ":
                grid[row][col]=symbol
                break
            else:
                print("The cell is filled already")
        else:
            print("Invalid Input.Enter the digits in the range[0,2]")
        
#computer's turn to enter the coordinates
def computer_step(grid,symbol):
    while True:
        row = random.randint(0, 2)
        col=random.randint(0, 2)
        if grid[row][col] == " ":
            grid[row][col] = symbol
            break

#finding the winner of the game
def find_winner(grid):
    #check column wise
    for col in range(3):
        if grid[0][col]!=" "and grid[0][col]==grid[1][col]==grid[2][col]:
            return True
    #check row wise
    for row in range(3):
        if grid[row][0]!=" "and grid[row][0]==grid[row][1]==grid[row][2]:
            return True
    #check diagonals
    if grid[0][0] != " " and grid[0][0] == grid[1][1] == grid[2][2]:
        return True
    if grid[0][2] != " " and grid[0][2] == grid[1][1] == grid[2][0]:
        return True
    
    return False

#writing loop code for the main game
def main():
    grid = create_grid()
    present_symbol = "X"
    while True:
        print_grid(grid)
        if present_symbol == 'X':
            player_step(grid, present_symbol)
        else:
            computer_step(grid,present_symbol)
        
        if find_winner(grid):
            print_grid(grid)
            print(f"{present_symbol} wins!")
            break
        else:
            flag=True
            for row in grid:
                if " " in row:
                    flag=False
                    break
            if flag:
                print_grid(grid)
                print("Wah!It's a Draw")
                break
        if present_symbol == "X":
            present_symbol = "O"
        else:
            present_symbol = "X"

if __name__ == "__main__":
    main()
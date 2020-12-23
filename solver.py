import math

puzzle = [
    [0,0,0,6,0,0,4,0,0],
    [7,0,0,0,0,3,6,0,0],
    [0,0,0,0,9,1,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,8,0,0,0,3],
    [0,0,0,3,0,6,0,4,5],
    [0,4,0,2,0,0,0,6,0],
    [9,0,3,0,0,0,0,0,0],
    [0,2,0,0,0,0,1,0,0]
]

def check_constraints(puzzle, x, y):
    current = puzzle[y][x]
    for number in puzzle[y]:
        print(number)
    
    for i in range(len(puzzle)):
        print(puzzle[i][x])
    
    region = get_region(puzzle, x, y)
    #for 

def get_region(puzzle, x, y):
    region = list()
    region_number = math.floor(x/) + math.floor(y)
    #for i in range(len(puzzle)):
    print(region_number)
        

get_region(puzzle, 7, 5)
#check_constraints(puzzle, 3,0)
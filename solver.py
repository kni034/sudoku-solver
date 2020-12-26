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
    new_puzzle = list(puzzle)
    row = new_puzzle[y]
    column = list()
    
    for i in range(len(puzzle)):
        column.append(puzzle[i][x])

    region = get_region(puzzle, x, y)

    if valid_row(region) and valid_row(row) and valid_row(column):
        return True
    return False

def get_region(puzzle, x, y):
    region = list()
    new_puzzle = list(puzzle)

    regions_sqrt = int(math.sqrt(len(puzzle[x])))
    x2 = round_down(x,regions_sqrt)
    y2 = round_down(y,regions_sqrt)

    for i in range(regions_sqrt):
        for j in range(regions_sqrt):
            region.append(new_puzzle[x2 + i][y2 + j])
    return region
        

def round_down(num, divisor):
    return num - (num%divisor)
        

def valid_row(row):
    seen = list(range(row))
    seen = [x+1 for x in seen]
    for num in row:
        if num != 0:
            if num in seen:
                seen.remove(num)
            else:
                return False
    return True

def solve(puzzle):
    new_puzzle = list(puzzle)
    numbers = []
    for y,row in enumerate(new_puzzle):
        for x,num in enumerate(row):
            if num == 0:
                numbers.append([num,x,y])

    stack = []
    i = 0
    while(i<len(new_puzzle)**2):
        current = numbers[i]
        #nå skal sudokuen løses med callback metoden
    


solve(puzzle)
'Added some changes'
##############################################
# APS106 Winter 2020 - Lab 8 - Maze Solver   #
##############################################

##############################################
# Helper functions
#
# These are provided to help you complete
# the lab. 
#
# YOU DO NOT NEED TO EDIT THIS FUNCTION 
##############################################

def print_maze(maze):
    """
    (tuple) -> None
    
    Input is a nested tuple representing a
    maze. Function prints the maze.
    
    """
    
    for row in maze:
        print("".join(row))
    

###########################################
# PART 1 - Read the maze from csv file    #
###########################################

import csv

def load_maze(filename):
    """
    (str) -> Maze-Tuple, Start-Coordinate, End-Coordinate
    
    Open a csv file containing a maze represented by ascii characters
    and return a nested tuple with each element representing a different
    square within the maze.
    
    Additionally, return the location of the start and end positions of the 
    maze as tuples representing x,y coordinates.
    
    For example, for the following maze:
        
        XXXXXXXXXXXXXXXXXX
        XOXOOOOOOOOOOOXOOE
        XOOOXOOXXXXXXOOOXX
        XXXOXXXXXXXXXXXXXX
        XOOOOOXXOOXXXXXXXX
        XXXXXOOOOXOOOOOXXX
        XXXXXXXOOOOXOXXXXX
        XXXXXXXXXXXXSXXXXX
    
    >>> load_maze_from_file(maze_file)
    ((('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'E'), 
    ('X', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X'), 
    ('X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'S', 'X', 'X', 'X', 'X', 'X')), 
    (7, 12), (1, 17))
        
    
    You may assume the following:
        1. Each line of the csv file has the same number of columns
        2. Each file will contain one and only one starting location ("S")
        3. Each file will contain one and only one exit location ("E")
        4. Each cell of the csv file will contain a single character
        
    """
    
    ## TODO - YOUR CODE HERE
    lst = []
    lst2 = []
    
    # Open the csv file 
    csvfile = open(filename, "r")
    
    grades_reader_2 = csv.reader(csvfile)
    
    # Append it to a list and remove the first row
    for row in grades_reader_2:
        lst.append(row)  
    
    # Convert each sublist into tuple 
    for sub_list in lst:
        tup = tuple(sub_list)
        lst2.append(tup)
    
    # Convert whole list into tuple
    tup_lst = tuple(lst2)
    
    # Locate where S and E are in the maze 
    for sub_tup in tup_lst:
        for structure in sub_tup:
            if structure == 'S':
                x_S = sub_tup.index(structure)
                y_S = tup_lst.index(sub_tup)
            if structure == 'E':
                x_E = sub_tup.index(structure)
                y_E = tup_lst.index(sub_tup)
                
    return tup_lst, (y_S, x_S), (y_E, x_E) 
###########################################
# PART 2 - Recursively solve the maze     #
###########################################

def solve_maze(maze,path,end):
    """
    (tuple,list,tuple) -> bool
    
    maze - a 2D tuple containing the characters defining the maze indexed by
            row and column
    path - a list of coordinates defining the current search path
    end  - the coordinate of the maze exit

    Recursively solve the maze stored as a 2D tuple of ASCII characters.
    Characters have the following meanings:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location 
    
    You may only move in horizontal or vertical directions. That is, the
    solution path, if it exists, should not contain any diagonal movements.
    
    The solution path, if it exists, should begin at the current location
    and end at the exit point.
    
    If no path exists, the path should be empty and the function should
    return "False"
    """
    
    ## TODO: YOUR CODE HERE

    # Current Coordinates
    (y, x) = path[len(path)-1]  
    
    # Ending Coordinate
    (a, b) = end    
    
    # Define Base Cases:
    # The coordinates must be inside the maze
    if (y >= len(maze) or x >= len(maze[0]) or x < 0 or y < 0):
        return False
    # Cannot move to a wall
    elif maze[y][x] == 'X':
        return False
    # Check if found end
    if y == a and x == b:
        return True
       
    
    # Recursive Case
    
    # Moving Right
    if contains_coordinate(path, y, x + 1) == False:
        path.append((y, x + 1))
        if solve_maze(maze, path, end) == False:
            path.pop()
        else:
            return solve_maze(maze, path, end)
    
    # Move Left 
    if contains_coordinate(path, y, x - 1) == False:
        path.append((y, x - 1))
        if solve_maze(maze, path, end) == False:
            path.pop()
        else:
            return solve_maze(maze, path, end)
        
    # Move Up 
    if contains_coordinate(path, y - 1, x) == False:
        path.append((y - 1, x))
        if solve_maze(maze, path, end) == False:
            path.pop()
        else:
            return solve_maze(maze, path, end)
        
    # Moving Down
    if contains_coordinate(path, y + 1, x) == False:
        path.append((y + 1, x))
        if solve_maze(maze, path, end) == False:
            path.pop()    
        else:
            return solve_maze(maze, path, end)   
    
    # Check to see if its possible
    if path[0][0] == y and path[0][1] == x:
        path.clear()
    return False
 
# Define a new function called contains_coordinate
def contains_coordinate(path,y,x):
    for coordinates in path:
        if coordinates[0] == y and coordinates[1] == x:
            return True
    return False 

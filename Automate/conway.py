#!/usr/bin/env python

###############
# Author : Matthew McCourry
# Contact: github.com/mbmcc
# Title : Conways Game of Life
# Description : 
"""
Conway’s Game of Life is an example of cellular automata: a set of rules governing the behavior of a field made up of discrete cells. In practice, it creates a pretty animation to look at. You can draw out each step on graph paper, using the squares as cells. A filled-in square will be “alive” and an empty square will be “dead.” 
If a living square has exactly two or three living neighbors, it continues to live on the next step. 
If a dead square has exactly three living neighbors, it comes alive on the next step. Every other square dies or remains dead on the next step.
"""
# Created : 20230721
# Last modified : 
###############

import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of a list for the cells
next_cells = []

for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cell
        else:
            column.append(' ') # Add a dead cell
    next_cells.append(column) # next_cells is a list of a column of lists.

while True: # Main Loop
    print('\n\n\n\n\n') # Separate each step with newlines.
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # Print the # or empty Space
        print() # Print a new line at the end of the row

    # Calculate the next step's cells based on the current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighbors coordinates
            # Note: `% WIDTH` ensures that the left_coord is always between 0 and WIDTH - 1
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH 
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            #Count number of living neighbors, each cell has eight neighbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1 # Top-Left neighbor is alive.
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1 # Top neighbor is alive.
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1 # Top-Right neighbor is alive.
            if current_cells[left_coord] == '#':
                num_neighbors += 1 # Left neighbor is alive.
            if current_cells[right_coord] == '#':
                num_neighbors += 1 # Right neighbor is alive.
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 # Below-Left neighbor is alive.
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1 # Below neighbor is alive.
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1 # Below-Right neighbor is alive.

            # Set cell based on 'Conways Game of Life' rules
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                # Dead cells with 3 neighbors become alive
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                next_cells[x][y] = ' '

    time.sleep(1) # Add a 1-second pause to reduce flicker



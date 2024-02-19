#!/bin/python
import sys

grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)
    
products=[]
for i in range(20):
    for j in range(17):
        products.append(grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])

for i in range(17):
    for j in range(20):
        products.append(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
        
for i in range(17):
    for j in range(3,20):
        products.append(grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3])

for i in range(17):
    for j in range(17):
        products.append(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])

print max(products)

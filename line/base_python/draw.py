from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts

def draw_lines( matrix, screen, color ):
    track = 0
    while track < matrix.len():
        pointlist1 = matrix[track]
        pointlist2 = matrix[track+1]
        numcolor = 0
        draw_line(screen, pointlist1[1], pointlist1[2], pointlist2[1], pointlist2[2], numcolor)
        track += 2
    
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):

    pointlist = [x,y,z,1]
    matrix.append(pointlist)

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    return "blah"

test = new_matrix(0,0)
add_edge(test,1,2,3,4,5,6)
print_matrix(test)

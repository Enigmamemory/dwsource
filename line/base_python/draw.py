from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts

def draw_lines( matrix, screen, color ):
    track = 0
    while track < len(matrix):
        pointlist1 = matrix[track]
        pointlist2 = matrix[track+1]
        draw_line(screen, pointlist1[0], pointlist1[1], pointlist2[0], pointlist2[1], color)
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
    x = x0
    y = y0
    A = 2*(y1-y0)
    B = -2*(x1-x0)
    if (B != 0):
        m = A / B * -1
    d = A + (B/2)
    if (x > x1):
        draw_line(screen, x1, y1, x0, y0, color)
    elif (B == 0):
        if (y >= y1):
            y = y1
            y1 = y0 #switches order of points so it can still be drawn bottom up
        while (y <= y1):
            plot(screen,color,x,y)
            y += 1
        #Need a code that draws vertical lines
    elif (m > 1):
        while (y <= y1):
            plot(screen,color,x,y)
            if d < 0:
                x += 1
                d += A
            y += 1
            d += B
    elif (m <= 1 and m > 0):
        while (x <= x1):
            plot(screen,color,x,y)
            if d > 0:
                y += 1
                d += B
            x += 1
            d += A
    elif (m <= 0 and m > -1):
        while (x <= x1):
            plot(screen,color,x,y)
            if d < 0:
                y -= 1
                d -= B
            x += 1
            d += A
            #check = [x,y]
            #print check
    elif (m <= -1):
        #print "Got to this point :^)"
        while (y >= y1):
            plot(screen,color,x,y)
            if d > 0:
                x += 1
                d += A
            y -= 1
            d -= B
            #check = [x,y]
            #print check


        
'''
test = new_matrix(0,0)
add_edge(test,0,0,0,50,10,160)
add_edge(test,0,0,0,50,50,0)
add_edge(test,0,0,0,20,100,0)
add_edge(test,0,100,50,50,0,0)
add_edge(test,0,50,0,100,0,0)
add_edge(test,50,0,0,50,100,0)
add_edge(test,25,100,0,25,0,0)
add_edge(test,200,160,0,150,150,0)
add_edge(test,170,250,0,150,150,0)
add_edge(test,200,200,0,150,150,0)
add_edge(test,200,150,0,150,250,0)
add_edge(test,200,250,0,200,150,0)
add_edge(test,250,150,0,150,200,0)

#print_matrix(test)
blah = new_screen()
nyeh = [100,100,0]
draw_lines(test,blah,nyeh)
display(blah)
'''

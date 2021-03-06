from display import *
from draw import *

screen = new_screen()
extra = new_screen()
color = [ 0, 120, 150]
color2 = [0,255,0]
matrix = []
matrix2 = []

#hat top outline
add_edge(matrix, 0, 48, 0, 24, 20, 0)
add_edge(matrix, 24, 20, 0, 52, 4, 0)
add_edge(matrix, 52, 4, 0, 64, 0, 0)
add_edge(matrix, 64, 0, 0, 78, 4, 0)
add_edge(matrix, 78, 4, 0, 116, 24, 0)
add_edge(matrix, 116, 24, 0, 112, 48, 0)
add_edge(matrix, 112, 48, 0, 64, 48, 0)
add_edge(matrix, 64, 48, 0, 24, 56, 0)
add_edge(matrix, 24, 56, 0, 8, 64, 0)
add_edge(matrix, 8, 64, 0, 0, 48, 0)

#hat top details

add_edge(matrix, 24, 56, 0, 16, 44, 0)
add_edge(matrix, 16, 44, 0, 24, 20, 0)

add_edge(matrix, 64, 48, 0, 56, 32, 0)
add_edge(matrix, 56, 32, 0, 56, 8, 0)

add_edge(matrix, 52, 4, 0, 56, 8, 0)
add_edge(matrix, 56, 8, 0, 64, 8, 0)
add_edge(matrix, 64, 8, 0, 72, 8, 0)
add_edge(matrix, 72, 8, 0, 78, 4, 0)

#hat bottom and rim

add_edge(matrix, 112, 48, 0, 114, 64, 0)
add_edge(matrix, 114, 64, 0, 68, 64, 0)
add_edge(matrix, 68, 64, 0, 16, 80, 0)
add_edge(matrix, 16, 80, 0, 8, 64, 0)

add_edge(matrix, 114, 64, 0, 122, 72, 0)
add_edge(matrix, 122, 72, 0, 116, 76, 0)
add_edge(matrix, 116, 76, 0, 108, 80, 0)
add_edge(matrix, 108, 80, 0, 104, 80, 0)
add_edge(matrix, 104, 80, 0, 96, 80, 0)
add_edge(matrix, 96, 80, 0, 68, 64, 0)

#hair - it gets nasty from here x(

#left
add_edge(matrix, 16, 80, 0, 18, 84, 0)
add_edge(matrix, 18, 84, 0, 16, 96, 0)
add_edge(matrix, 16, 96, 0, 24, 88, 0)
add_edge(matrix, 24, 88, 0, 23, 100, 0)
add_edge(matrix, 23, 100, 0, 16, 120, 0)
add_edge(matrix, 16, 120, 0, 23, 112, 0)
add_edge(matrix, 23, 112, 0, 25, 116, 0)
add_edge(matrix, 24, 116, 0, 28, 110, 0)
add_edge(matrix, 28, 110, 0, 34, 106, 0)
add_edge(matrix, 34, 106, 0, 33, 116, 0)
add_edge(matrix, 33, 116, 0, 32, 128, 0)
add_edge(matrix, 32, 128, 0, 40, 120, 0)
add_edge(matrix, 40, 120, 0, 40, 124, 0)
add_edge(matrix, 40, 124, 0, 48, 120, 0)
add_edge(matrix, 48, 120, 0, 52, 121, 0)

#middle
add_edge(matrix, 18, 82, 0, 24, 88, 0)
add_edge(matrix, 24, 88, 0, 28, 90, 0)
add_edge(matrix, 28, 90, 0, 36, 90, 0)

add_edge(matrix, 30, 80, 0, 36, 90, 0)
add_edge(matrix, 36, 90, 0, 40, 96, 0)
add_edge(matrix, 40, 96, 0, 45, 98, 0)

add_edge(matrix, 40, 88, 0, 45, 98, 0)
add_edge(matrix, 45, 98, 0, 56, 104, 0)
add_edge(matrix, 56, 104, 0, 54, 96, 0)

add_edge(matrix, 47, 80, 0, 48, 88, 0)
add_edge(matrix, 48, 88, 0, 56, 104, 0)
add_edge(matrix, 56, 104, 0, 64, 104, 0)
add_edge(matrix, 64, 104, 0, 61, 96, 0)
add_edge(matrix, 61, 96, 0, 60, 90, 0)
add_edge(matrix, 60, 90, 0, 56, 72, 0)
add_edge(matrix, 56, 72, 0, 64, 80, 0)
add_edge(matrix, 64, 80, 0, 58, 76, 0)
add_edge(matrix, 58, 76, 0, 64, 72, 0)
add_edge(matrix, 64, 72, 0, 72, 77, 0)
add_edge(matrix, 72, 77, 0, 80, 80, 0)
add_edge(matrix, 80, 80, 0, 93, 85, 0)
add_edge(matrix, 93, 85, 0, 96, 80, 0)

#right hair

add_edge(matrix, 116, 76, 0, 119, 100, 0)
add_edge(matrix, 119, 100, 0, 122, 102, 0)
add_edge(matrix, 122, 102, 0, 116, 96, 0)
add_edge(matrix, 116, 96, 0, 120, 104, 0)
add_edge(matrix, 120, 104, 0, 110, 98, 0)

#face + ear + mouth

add_edge(matrix, 108, 80, 0, 108, 86, 0)
add_edge(matrix, 108, 86, 0, 110, 98, 0)
add_edge(matrix, 110, 98, 0, 107, 106, 0)
add_edge(matrix, 107, 106, 0, 92, 130, 0)
add_edge(matrix, 92, 130, 0, 64, 124, 0)
add_edge(matrix, 64, 124, 0, 57, 120, 0)
add_edge(matrix, 57, 120, 0, 49, 114, 0)
add_edge(matrix, 49, 114, 0, 34, 106, 0)
add_edge(matrix, 34, 106, 0, 28, 90, 0)

add_edge(matrix, 49, 114, 0, 48, 106, 0)
add_edge(matrix, 48, 106, 0, 44, 104, 0)
add_edge(matrix, 44, 104, 0, 38, 102, 0)
add_edge(matrix, 38, 102, 0, 40, 96, 0)

add_edge(matrix, 44, 104, 0, 45, 98, 0)

add_edge(matrix, 88, 114, 0, 92, 112, 0)
add_edge(matrix, 92, 112, 0, 96, 112, 0)

#eyes

#left eye

add_edge(matrix, 62, 84, 0, 63, 90, 0)
add_edge(matrix, 63, 90, 0, 66, 94, 0)
add_edge(matrix, 66, 94, 0, 73, 98, 0)
add_edge(matrix, 73, 98, 0, 80, 100, 0)
add_edge(matrix, 80, 100, 0, 86, 96, 0)
add_edge(matrix, 86, 96, 0, 84, 88, 0)
add_edge(matrix, 84, 88, 0, 78, 85, 0)
add_edge(matrix, 78, 85, 0, 72, 83, 0)
add_edge(matrix, 72, 83, 0, 62, 84, 0)

add_edge(matrix, 78, 85, 0, 72, 86, 0)
add_edge(matrix, 72, 86, 0, 70, 90, 0)
add_edge(matrix, 70, 90, 0, 73, 94, 0)
add_edge(matrix, 73, 94, 0, 78, 96, 0)
add_edge(matrix, 78, 96, 0, 83, 92, 0)
add_edge(matrix, 83, 92, 0, 84, 88, 0)

add_edge(matrix, 63, 84, 0, 64, 90, 0)
add_edge(matrix, 64, 90, 0, 67, 94, 0)
add_edge(matrix, 61, 84, 0, 62, 90, 0)
add_edge(matrix, 62, 90, 0, 65, 94, 0)

add_edge(matrix, 72, 84, 0, 62, 85, 0)

#right eye

add_edge(matrix, 95, 84, 0, 101, 90, 0)
add_edge(matrix, 101, 90, 0, 108, 86, 0)

add_edge(matrix, 97, 80, 0, 98, 82, 0)
add_edge(matrix, 98, 82, 0, 102, 86, 0)
add_edge(matrix, 102, 86, 0, 104, 84, 0)
add_edge(matrix, 104, 84, 0, 104, 80, 0)

#shirt collar
#left

add_edge(matrix, 64, 124, 0, 68, 130, 0)
add_edge(matrix, 68, 130, 0, 70, 144, 0)
add_edge(matrix, 70, 144, 0, 88, 152, 0)
add_edge(matrix, 88, 152, 0, 86, 144, 0)
add_edge(matrix, 86, 144, 0, 84, 138, 0)
add_edge(matrix, 84, 138, 0, 64, 124, 0)

#right

add_edge(matrix, 107, 106, 0, 111, 110, 0)
add_edge(matrix, 111, 110, 0, 108, 122, 0)
add_edge(matrix, 108, 122, 0, 96, 132, 0)
add_edge(matrix, 96, 132, 0, 96, 140, 0)
add_edge(matrix, 96, 140, 0, 99, 146, 0)
add_edge(matrix, 99, 146, 0, 110, 136, 0)
add_edge(matrix, 110, 136, 0, 108, 122, 0)

#middle

add_edge(matrix, 86, 144, 0, 94, 150, 0)
add_edge(matrix, 94, 150, 0, 96, 140, 0)

#coat collar
#left

add_edge(matrix, 57, 120, 0, 52, 132, 0)
add_edge(matrix, 52, 132, 0, 64, 140, 0)
add_edge(matrix, 64, 140, 0, 70, 156, 0)
add_edge(matrix, 70, 156, 0, 52, 152, 0)
add_edge(matrix, 52, 152, 0, 42, 134, 0)
add_edge(matrix, 42, 134, 0, 48, 128, 0)
add_edge(matrix, 48, 128, 0, 52, 121, 0)
add_edge(matrix, 52, 121, 0, 57, 120, 0)

add_edge(matrix, 64, 140, 0, 70, 138, 0)

add_edge(matrix, 110, 136, 0, 118, 128, 0)
add_edge(matrix, 118, 128, 0, 124, 124, 0)
add_edge(matrix, 124, 124, 0, 125, 112, 0)
add_edge(matrix, 125, 112, 0, 120, 110, 0)
add_edge(matrix, 120, 110, 0, 107, 106, 0)
add_edge(matrix, 107, 106, 0, 116, 112, 0)
add_edge(matrix, 116, 112, 0, 118, 128, 0)

#random neck
add_edge(matrix, 107, 106, 0, 108, 122, 0)

#shoulder

#left

add_edge(matrix, 52, 152, 0, 44, 162, 0)
add_edge(matrix, 44, 162, 0, 38, 168, 0)

add_edge(matrix, 44, 162, 0, 68, 180, 0)
add_edge(matrix, 68, 180, 0, 72, 188, 0)
add_edge(matrix, 72, 188, 0, 74, 194, 0)
add_edge(matrix, 74, 194, 0, 72, 200, 0)

add_edge(matrix, 38, 168, 0, 40, 208, 0)

add_edge(matrix, 66, 188, 0, 67, 208, 0)

#right

add_edge(matrix, 124, 124, 0, 142, 122, 0)
add_edge(matrix, 142, 122, 0, 160, 128, 0)

add_edge(matrix, 142, 122, 0, 132, 144, 0)
add_edge(matrix, 132, 144, 0, 134, 156, 0)
add_edge(matrix, 134, 156, 0, 132, 164, 0)
add_edge(matrix, 132, 164, 0, 136, 168, 0)

add_edge(matrix, 134, 156, 0, 160, 160, 0)

add_edge(matrix, 132, 164, 0, 160, 168, 0)

#coat

add_edge(matrix, 64, 140, 0, 102, 168, 0)
add_edge(matrix, 102, 168, 0, 110, 136, 0)

add_edge(matrix, 102, 168, 0, 98, 176, 0)
add_edge(matrix, 98, 176, 0, 100, 178, 0)
add_edge(matrix, 100, 178, 0, 82, 188, 0)
add_edge(matrix, 82, 188, 0, 74, 194, 0)

add_edge(matrix, 118, 128, 0, 106, 168, 0)
add_edge(matrix, 106, 168, 0, 110, 172, 0)
add_edge(matrix, 110, 172, 0, 128, 166, 0)
add_edge(matrix, 128, 166, 0, 132, 164, 0)

add_edge(matrix, 128, 166, 0, 130, 170, 0)

add_edge(matrix, 110, 172, 0, 114, 180, 0)

add_edge(matrix, 100, 178, 0, 104, 184, 0)

add_edge(matrix, 82, 188, 0, 86, 194, 0)

add_edge(matrix, 103, 176, 0, 105, 181, 0)
add_edge(matrix, 105, 181, 0, 108, 179, 0)
add_edge(matrix, 108, 179, 0, 107, 175, 0)
add_edge(matrix, 107, 175, 0, 103, 176, 0)

#To finish the rest of this would probably take another two weeks.
#instead I'll just take what I have and enlarge it.

def enlarge(matrix, x):
    track = 0 #I swear I'll look at for loops one more time - when I HAVE time
    while track < len(matrix):
        (matrix[track])[0] = x*(matrix[track])[0]
        (matrix[track])[1] = x*(matrix[track])[1]
        track += 1

def translate(matrix,x,y): #I also could be doing matrix multiplication but
    track = 0
    while track < len(matrix):
        (matrix[track])[0] = x+(matrix[track])[0]
        (matrix[track])[1] = y+(matrix[track])[1]
        track += 1

def colorfy(screen,color):
    xcor = 0
    ycor = 0
    while xcor < XRES:
        while ycor < YRES:
            plot(screen,color,xcor,ycor)
            ycor += 1
        xcor += 1



    
enlarge(matrix,2)
translate(matrix,50,50)

#bluish = [0,0,155]

#colorfy(screen,bluish)
draw_lines( matrix,screen,color )
display(screen)

#Oh, and of course a test that all the lines actually work

#octant I
add_edge(matrix2, 0, 0, 0, XRES - 1, YRES - 75, 0)

#octant II
add_edge(matrix2, 0, 0, 0, XRES - 75, YRES - 1, 0)

#octant III
add_edge(matrix2, XRES - 75, 0, 0, 0, YRES - 1, 0)

#octant IV
add_edge(matrix2, XRES - 1, 75, 0, 0, YRES - 1, 0)

#octant V
add_edge(matrix2, XRES - 1, YRES - 75, 0, 0, 0, 0)

#octant VI
add_edge(matrix2, XRES - 75, YRES - 1, 0, 0, 0, 0)

#octant VIII
add_edge(matrix2, 0, YRES - 1, 0, XRES - 1, 75, 0)

#octant VII
add_edge(matrix2, 0, YRES - 1, 0, XRES - 75, 0, 0)

#horizontal line

add_edge(matrix2, 0, 100, 0, XRES - 1, 100, 0)

#vertical line

add_edge(matrix2, 100, 0, 0, 100, YRES - 1, 0)


draw_lines(matrix2,extra,color2)
display_new(extra, "test.ppm")

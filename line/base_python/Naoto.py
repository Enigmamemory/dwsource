from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0]
matrix = []

#hat top outline
add_edge(matrix, 0, 48, 0, 24, 20, 0)
add_edge(matrix, 24, 20, 0, 52, 4, 0)
add_edge(matrix, 52, 4, 0, 64, 0, 0)
add_edge(matrix, 64, 0, 0, 78, 4, 0)
add_edge(matrix, 78, 4, 0, 120, 24, 0)
add_edge(matrix, 120, 24, 0, 112, 48, 0)
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



draw_lines( matrix,screen,color )
display(screen)

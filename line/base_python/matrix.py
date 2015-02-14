"""
Points will be stored as 4 element lists: [x, y, z, 1]
Well will store all the points for an image is a list of points
that will be referred to as a matrix
"""

#Time to pretend I know what I'm doing - Alex


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ): #This better stay at 4
            m[c].append( 0 )
    return m

#Print the point list
#ayy no problem boss - Alex
def print_matrix( matrix ):
    for x in range(len(matrix)):
        strRtn = "[ "
        linelist = matrix[x] #drag out that list inside the list
        for y in range(len(linelist)):
            strRtn += " " + str(linelist[y]) + " " #put this list into string form
        strRtn += " ]"
        print strRtn #print that baby

test = new_matrix()
print_matrix(test)

#I guess I know what I'm doing?

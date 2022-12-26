def display_matrix():
    for i in range(nr):
        for j in range(nc):
            print("%5.3f" % (matrix[i][j]), end="\t")
        print()
    print("--------------------------------------------------------------------")
    return(matrix)
nr = int(input("no. of rows? "))
nc = int(input("no. of columns? "))
matrix = []
for i in range(nr):
    l = []
    for j in range(nc):
        element = int(input("Enter Number: "))
        l.append(element)
    matrix.append(l)
display_matrix()   


pr = int(input("enter pivot row "))
pc = int(input("enter pivot column "))

pr = pr - 1
pc = pc - 1

while  pr >= 0:        
    pivot_elem = matrix[pr][pc]
    #pivot row k har element ko divide kara rahe hain pivot element se
    for  i in range(nc):
        matrix[pr][i] = matrix[pr][i] / pivot_elem
    
    for i in range(nr):
        if i != pr:
            constant = matrix[i][pc]    
            for j in range(nc):
                matrix[i][j] = matrix[i][j] - constant * matrix[pr][j]
    display_matrix()            
    pr = int(input("enter pivot row "))
    pc = int(input("enter pivot column "))

    pr = pr - 1
    pc = pc - 1        

for i in range(nr):
    print(f"X{i+1} = {matrix[i][-1]}")


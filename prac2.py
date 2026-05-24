# 3 students, 3 exams
grades_matrix = [
    [80, 90, 100],  # Student 1
    [70, 80, 90],   # Student 2
    [60, 85, 75]    # Student 3
] 
n=len(grades_matrix) 
nc=len(grades_matrix[0]) 
c=0
row_avg=0 
col_avg=0
print("The average mark of the students are:",end=" ")
for m in grades_matrix:
    t=0 
    for e in m: 
        t+=e
        row_avg=t/nc
    print(f"{row_avg:.2f}",end=" ")  
print()
print("The average mark foe each exam are:",end=" ")
for x in range(nc): 
    f=0 
    for r in range(n):
        f+=grades_matrix[r][x]
        col_avg=f/n
    print(f"{col_avg:.2f}",end=" ")
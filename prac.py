matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
r=0
# Expected Output: ([6, 15], [5, 7, 9])
# Row sums: 1+2+3 = 6, 4+5+6 = 15
# Column sums: 1+4 = 5, 2+5 = 7, 3+6 = 9 
for m in matrix: 
    r+=1
    t=0
    for e in m: 
        t+=e  
    print(f"The sum of the {r}th row is: {t}")    
n=len(matrix)
nc=len(matrix[0])

for c in range(nc): 
    o=0
    for r in range(n): 
        o+=matrix[r][c] 
    print(f"the sum of the {c+1}th column is: {o}")    


    
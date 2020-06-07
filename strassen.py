A11 = 1
A12 = 3
A21 = 7
A22 = 5

B11 = 6
B12 = 8
B21 = 4
B22 = 2
#defining matrix
matrix1 = [[A11, A12], [A21, A22]]
matrix2 = [[B11, B12], [B21, B22]]
#Printing values to show the work
print("printing out values to show the matrix")
print(matrix1[0])
print(matrix1[1])
print("------ ")
print(matrix2[0])
print(matrix2[1])

#calc the sums, as described in the book(page 80):
S1 = B12 - B22
S2 = A11 + A12
S3 = A21 + A22
S4 = B21 - B11
S5 = A11 + A22
S6 = B11 + B22
S7 = A12 - A22
S8 = B21 + B22
S9 = A11 - A21
S10 = B11 + B12
#TheS = {S1: B12 - B22}
#printing out values
print(" ")
print("-----sums from the original matrix-----")
print(S1, S2, S3, S4, S5, S6, S7, S8, S9, S10)

#calculate the products
P1 = A11 * S1
P2 = S2 * B22
P3 = S3 * B11
P4 = A22 * S4
P5 = S5 * S6
P6 = S7 * S8
P7 = S9 * S10
print(" ")
print("-----products from the sums-----")
print(P1, P2, P3, P4, P5, P6, P7)

#the submatrix
C11 = P5 + P4 - P2 + P6
C12 = P1 + P2
C21 = P3 + P4
C22 = P5 + P1 - P3 - P7
print(" ")
print("-----values for the final matrix-----")
print(C11, C12, C21, C22)

#the answer
answer = [[C11, C12],[C21, C22]]
print(" ")
print("-----final matrix-----")
print(answer[0])
print(answer[1])
import numpy as np

def read_matrix():
    rows, cols = map(int, input().split())
    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def add_matrices():
    print("Enter size of first matrix:")
    a = read_matrix()
    print("Enter size of second matrix:")
    b = read_matrix()
    if a.shape != b.shape:
        print("The operation cannot be performed.")
        return
    result = a + b
    print("The result is:")
    print(result)

def multiply_by_constant():
    matrix = read_matrix()
    constant = float(input("Enter constant: "))
    result = matrix * constant
    print("The result is:")
    print(result)

def multiply_matrices():
    print("Enter size of first matrix:")
    a = read_matrix()
    print("Enter size of second matrix:")
    b = read_matrix()
    if a.shape[1] != b.shape[0]:
        print("The operation cannot be performed.")
        return
    result = np.dot(a, b)
    print("The result is:")
    print(result)

def transpose_matrix():
    print("1. Transpose by side diagonal")
    print("2. Transpose by vertical line")
    print("3. Transpose by horizontal line")
    choice = int(input())
    matrix = read_matrix()
    if choice == 1:
        result = np.transpose(matrix)
        result = np.flip(result, axis=0)
        result = np.flip(result, axis=1)
    elif choice == 2:
        result = np.flip(matrix, axis=1)
    elif choice == 3:
        result = np.flip(matrix, axis=0)
    else:
        print("Invalid choice.")
        return
    print("The result is:")
    print(result)

def determinant_matrix():
    print("Enter size of matrix:")
    matrix = read_matrix()
    if matrix.shape[0] != matrix.shape[1]:
        print("The matrix must be square.")
        return
    result = np.linalg.det(matrix)
    print("The result is:")
    print(result)

def inverse_matrix():
    print("Enter size of matrix:")
    matrix = read_matrix()
    if matrix.shape[0] != matrix.shape[1]:
        print("The matrix must be square.")
        return
    if np.linalg.det(matrix) == 0:
        print("This matrix doesn't have an inverse.")
        return
    result = np.linalg.inv(matrix)
    print("The result is:")
    print(result)

while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Find determinant of matrix")
    print("6. Find inverse of matrix")
    print("0. Exit")
    choice = int(input())
    if choice == 0:
        break
    elif choice == 1:
        add_matrices()
    elif choice == 2:
        multiply_by_constant()
    elif choice == 3:
        multiply_matrices()
    elif choice == 4:
        transpose_matrix()
    elif choice == 5:
        determinant_matrix()
    elif choice == 6:
        inverse_matrix()
    else:
        print("Invalid choice.")

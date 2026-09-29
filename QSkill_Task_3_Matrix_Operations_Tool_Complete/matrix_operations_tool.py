import numpy as np

def read_matrix(name):
    while True:
        try:
            rows=int(input(f"Enter number of rows for {name}: "))
            cols=int(input(f"Enter number of columns for {name}: "))
            if rows<=0 or cols<=0: raise ValueError
            matrix=[]
            for i in range(rows):
                while True:
                    values=input(f"Row {i+1}: ").split()
                    if len(values)!=cols:
                        print(f"Please enter exactly {cols} numbers."); continue
                    try:
                        matrix.append([float(x) for x in values]); break
                    except ValueError:
                        print("Enter numeric values only.")
            return np.array(matrix)
        except ValueError:
            print("Invalid dimensions. Enter positive integers.")

def main():
    print("QSkill Matrix Operations Tool")
    while True:
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Determinant\n6. Exit")
        choice=input("Enter choice (1-6): ").strip()
        if choice in ("1","2"):
            A=read_matrix("Matrix A"); B=read_matrix("Matrix B")
            if A.shape!=B.shape:
                print("Error: Addition/Subtraction require same dimensions."); continue
            print(A+B if choice=="1" else A-B)
        elif choice=="3":
            A=read_matrix("Matrix A"); B=read_matrix("Matrix B")
            if A.shape[1]!=B.shape[0]:
                print("Error: columns of A must equal rows of B."); continue
            print(A@B)
        elif choice=="4":
            print(read_matrix("Matrix").T)
        elif choice=="5":
            A=read_matrix("Matrix")
            if A.shape[0]!=A.shape[1]:
                print("Error: determinant requires a square matrix."); continue
            print(f"Determinant: {np.linalg.det(A):.4f}")
        elif choice=="6":
            print("Thank you!"); break
        else: print("Invalid choice.")
if __name__=="__main__": main()

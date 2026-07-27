#Inverse Of Matrix
def display(M,R,C):
    for i in range(R):
        for j in range(C):
            print(M[i][j],end="\t")
        print()
def take_input(M,R,C):
    for i in range(R):
        for j in range(C):
            M[i][j]=int(input("Enter the elements:="))
def inverse(M,R,C):
    if (R == C):
        a=[]
        inv=[]
        for i in range(R):
            a.append(M[i]+[0]*R)
            a[i][R + i] = 1
        for i in range(R):
            di=a[i][i]
            if (di==0):
                print("Matrix is singular, inverse not possible")
                return False
            for j in range(2*R):
                a[i][j]=a[i][j]/di
            for k in range(R):
                if (k!=i):
                    f=a[k][i]
                    for j in range(2*R):
                        a[k][j]=a[k][j]-f*a[i][j]
        for i in range(R):
            inv.append(a[i][R:])
        return inv
    else:
        print("Inverse is not possible")
if __name__ == '__main__':
    rows=int(input("Enter the number of rows:="))
    cols=int(input("Enter the number of columns:="))
    M1=[]
    for i in range(rows):
        M1.append([0]*cols)
    display(M1, rows, cols)
    print("Enter the Matrix:")
    take_input(M1, rows, cols)
    display(M1, rows, cols)
    print("The Inverse Of Matrix is:=")
    inv=inverse(M1, rows, cols)
    if inv:
        display(inv, rows, cols)
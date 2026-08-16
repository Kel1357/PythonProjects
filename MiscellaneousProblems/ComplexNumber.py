import math
class ComplexNumber:
    def __init__(self,real:float,imag:float):
        self.real=real
        self.imag=imag
    def add(self,sec):
        com=ComplexNumber(self.real+sec.real,self.imag+sec.imag)
        return com
    def sub(self,sec):
        com=ComplexNumber(self.real-sec.real,self.imag-sec.imag)
        return com
    def multi(self,sec):
        com=ComplexNumber(
            (self.real*sec.real)-(self.imag*sec.imag),
            (self.real*sec.imag)+(self.imag*sec.real)
        )
        return com
    def divide(self, sec):
       try:
           denominator=sec.real**2+sec.imag**2
           com=ComplexNumber(
               (self.real*sec.real+self.imag*sec.imag)/denominator,
               (self.imag*sec.real-self.real*sec.imag)/denominator
           )
           return com
       except ZeroDivisionError:
            print("Division by Zero Complex Number is Undefined")
            return None
    def magnitudes(c1, c2):
        mag=(
            math.sqrt(c1.real**2+c1.imag**2),
            math.sqrt(c2.real**2+c2.imag**2)
        )
        return mag
    def __str__(self):
        if self.imag>0:
            sign="+"
        elif self.imag<0:
            sign="-"
        else:
            sign=""
        if self.imag==0:
            return f"{self.real:.2f}"
        elif self.real==0:
            return f"{sign}{abs(self.imag):.2f}i"
        else:
            return f"{self.real:.2f} {sign} {abs(self.imag):.2f}i"
if __name__=='__main__':
    r1,i1=map(float,input("Enter the First Complex Number (real,imag):").split(','))
    r2,i2=map(float,input("Enter the Second Complex Number (real,imag):").split(','))
    c1=ComplexNumber(r1,i1)
    c2=ComplexNumber(r2,i2)
    while(True):
        print("\nChoose An Operation for Complex Number")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Magnitudes Of Both numbers")
        print("0. Exit")
        n=int(input("Enter the Choice Of Operation:"))
        if n==1:
            print("Addition:",c1.add(c2))
        elif n==2:
            print("Subtraction:",c1.sub(c2))
        elif n==3:
            print("Multiplication:",c1.multi(c2))
        elif n==4:
            res=c1.divide(c2)
            if res is not None:
                print("Division:",res)
        elif n==5:
            m1,m2=ComplexNumber.magnitudes(c1, c2)
            print(f"Magnitude Of First: {m1:.2f}")
            print(f"Magnitude Of Second: {m2:.2f}")
        elif n==0:
            break
        else:
            print("Invalid Choice, Please Try Again")
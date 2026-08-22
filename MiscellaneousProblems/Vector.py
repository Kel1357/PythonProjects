import math
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def add(self,sec):
        vec1=self.i+sec.i
        vec2=self.j+sec.j
        vec3=self.k+sec.k
        return Vector(vec1,vec2,vec3)
    def subtraction(self,sec):
        vec=Vector(self.i-sec.i,self.j-sec.j,self.k-sec.k)
        return vec
    def dot_product(self,sec):
        vec=self.i*sec.i+self.j*sec.j+self.k*sec.k
        return vec
    def cross_product(self,sec):
        vec=Vector(
            self.j*sec.k-self.k*sec.j,
            self.k*sec.i-self.i*sec.k,
            self.i*sec.j-self.j*sec.i
        )
        return vec
    def magnitude(self):
        mag=math.sqrt(self.i**2+self.j**2+self.k**2)
        return mag
    def unit_vector(self):
        mag=self.magnitude()
        vec=Vector(self.i/mag,self.j/mag,self.k/mag)
        return vec
    def projection(self,sec):
        dot=self.dot_product(sec)
        mag=sec.magnitude()**2
        scalar=dot/mag
        projection=Vector(sec.i*scalar,sec.j*scalar,sec.k*scalar)
        return projection
    def angle(self,sec):
        dot=self.dot_product(sec)
        mag1=self.magnitude()
        mag2=sec.magnitude()
        Cos_theta=dot/(mag1*mag2)
        return math.degrees(math.acos(Cos_theta))
    def __str__(self):
        return f"{self.i}i {self.j}j {self.k}k"
if __name__=='__main__':
    i1,j1,k1=map(int,input("Enter the First Vector (i,j,k):").split(','))
    v1=Vector(i1,j1,k1)
    i2,j2,k2=map(int,input("Enter the Second Vector (i,j,k):").split(','))
    v2=Vector(i2,j2,k2)
    while (True):
        print("\nChoose An Operation For Vector")
        print("1. Vector Addition")
        print("2. Vector Subtraction")
        print("3. Dot Product")
        print("4. Cross Product")
        print("5. Magnitude Of Both Vector")
        print("6. Unit Vector")
        print("7. Projection Of v1 onto v2")
        print("8. Angle Between Vectors")
        print("0. Exit The Program")
        n=int(input("Enter the Choice:"))
        if n==1:
            print("Addition:",v1.add(v2))
        elif n==2:
            print("Subtraction:",v1.subtraction(v2))
        elif n==3:
            print("Dot Product:",v1.dot_product(v2))
        elif n==4:
            print("Cross Product:",v1.cross_product(v2))    
        elif n==5:
            print("Magnitude of v1:",v1.magnitude())
            print("Magnitude of v2:",v2.magnitude())
        elif n==6:
            print("Unit Vector of v1:",v1.unit_vector())
            print("Unit Vector of v2:",v2.unit_vector())
        elif n==7:
            print("Projection Of v1 onto v2:",v1.projection(v2))
        elif n==8:
            print("Angle Between Vectors:",v1.angle(v2),"Degrees")
        elif n==0:
            print("Program Exited Successfully")
            break
        else:
            print("Invalid Choice, Please Try Again")
import math as mth

# Main functions used
def big_F(x):
    return ((x ** 4) / 2) + mth.sin(x)
    


def small_F(x):
    return 2 * (x ** 3) + mth.cos(x)
    


def Analitical(a, b):
    return big_F(b) - big_F(a)


# Simple Rectangle Method
def simpleRectangle(a, b):

    h = b - a
    midPoint = (a + b) / 2
    value = h * small_F(midPoint)
    error = Analitical(a, b) - value

    print("Value: " + str(value))
    print("Error: " + str(error))


# Simple Trapezoid Method (n = 1)
def simpleTrapezoid(a, b):

    h = b - a
    value = (h / 2) * (small_F(a) + small_F(b))
    error = Analitical(a, b) - value
    
    print("Value: " + str(value))
    print("Error: " + str(error))


# Simple Simpson Formula (n = 2)
def simpleSimpson(a, b):

    h = b - a
    h = h / 2
    x1 = (a + b) / 2.0
    value = (h * (1.0 / 3.0)) * (small_F(a) + 4 * (small_F(x1)) + small_F(b))

    # to change ->
    zeta = 0.5
    fourthDerivative = mth.cos(zeta)
    error = (-1 / 90) * (h ** 5) * fourthDerivative

    print("Value: " + str(value))
    print("Error: " + str(error))


# Simple n=4 Formula
#def simpleN_4:


# Simple Cheb. Method (n = 2)
def simpleCheb_n2(a, b):

    h = b - a
    t = 0.577350
    x1 = (b + a) / 2 + (b - a) / 2 * (-t)
    x2 = (b + a) / 2 + (b - a) / 2 * t
    value = (h / 2) * (small_F(x1) + small_F(x2))
    error = Analitical(a, b) - value
    print("Value: " + str(value))
    print("Error: " + str(error))


# Simple Cheb. Method (n = 4)
def simpleCheb_n4(a, b):

    h = b - a
    t1 = 0.794654
    t2 = 0.187592
    x1 = ((b + a) / 2) + ((b - a) / 2) * (-t1)
    x4 = ((b + a) / 2) + ((b - a) / 2) * t1
    x2 = ((b + a) / 2) + ((b - a) / 2) * (-t2)
    x3 = ((b + a) / 2) + ((b - a) / 2) * t2

    value = (h / 4) * (small_F(x1) + small_F(x2) + small_F(x3) + small_F(x4))
    error = Analitical(a, b) - value

    print("Value: " + str(value))
    print("Error: " + str(error))


# Composite Trapezoid Formula (n=1, m=4)
def compTrapezoid(a, b):

    m=4 
    distance=(a-b)/(m+1)
    x1=a+abs(distance)
    x2=x1+abs(distance)
    x3=x2+abs(distance)
    x4=x3+abs(distance)

    value=(((b-a)/(2*m))*(small_F(a)+small_F(b)+2*small_F(x1)+2*small_F(x2)+2*small_F(x3)+2*small_F(x4)))
    error=Analitical(a,b)-value

    print("Value: " + str(value))
    print("Error: " + str(error))


# Composite Simpson Formula (n=2, m=2)
def compSimpson(a,b):
  
    m=2
    distance=(a-b)/(2*m)
    x1=a+abs(distance)
    x2=x1+abs(distance)
    x3=x2+abs(distance)

    value=((abs(distance)/-3)*(small_F(a)+4*small_F(x1)+2*small_F(x2)+4*small_F(x3)+small_F(b)))

    # to change ->
    zeta = 0.5
    fourthDeriv = mth.cos(zeta)
    error = (-1 / 90) * m * (distance ** 5) * fourthDeriv
  
    print("Value: " + str(value))
    print("Error: " + str(error))

# Composite Rectangle Method (n=0, m=20)
def compRectangle(a,b):

    # Switch between m=4 and m=20
    m=20

    value=0.0

    distance=(b-a)/(m+1)

    node=a
    nodes=[]
    nodes.append(node)
  
    for i in range(0,m+1):
      node=node+distance
      nodes.append(node)

    middlePoints=[]

    for i in range(0,m+1):
      middlePoint=(nodes[i]+nodes[i+1])/2
      middlePoints.append(middlePoint)

    mpValues=[]

    for i in range(0,m+1):
      mpValue=distance*(small_F(middlePoints[i]))
      mpValues.append(mpValue)

    
    for i in range(0,m+1):
      value=value+mpValues[i]

    error=Analitical(a,b)-value

    print("Value: " + str(value))
    print("Error: " + str(error))


# Program input data
a = -1.0
b = 0.5

# Functions application
print("\nSimple Rectangle: ")
simpleRectangle(a, b)

print("\nSimple Trapezoid: ")
simpleTrapezoid(a, b)


print("\nSimple Simpson: ")
simpleSimpson(a, b)

print("\nSimple Cheb. n = 2: ")
simpleCheb_n2(a, b)

print("\nSimple Cheb. n = 4: ")
simpleCheb_n4(a, b,)

print("\nComposite Trapezoid: ")
compTrapezoid(a,b)

print("\nComposite Simpson: ")
compSimpson(a,b)

print("\nComposite Rectangle: ")
compRectangle(a,b)

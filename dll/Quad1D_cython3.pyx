#Typage statique des variables et de la fonction f avec cpdef.

cpdef double f(double x) except? -2:
    return x ** 2 + x
    
def integrate_f(double a, double b, int N):
    cpdef int i
    cpdef double s, dx
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
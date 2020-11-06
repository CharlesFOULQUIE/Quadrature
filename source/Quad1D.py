import time

def f(x):
    return x**2 + x
    
def integrate_f(a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
    
def main():
    start_time = time.time()

    a = 0
    b = 1
    N = 10**7
    res = integrate_f(a, b, N)

    print("--- value : %s  ---" % (res))
    print("--- time : %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
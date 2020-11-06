import time
import source.Quad1D as quad
import dll.Quad1D as quad
import dll.Quad1D_cython1 as quad
import dll.Quad1D_cython2 as quad
import dll.Quad1D_cython3 as quad

def main():
    start_time = time.time()

    a = 0
    b = 1
    N = 10**6
    res = quad.integrate_f(a, b, N)

    print("--- value : %s " % (res))
    print("--- time : %s s " % (time.time() - start_time))

if __name__ == '__main__':
    main()
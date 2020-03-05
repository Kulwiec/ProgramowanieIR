import time
import sys
#sys.setrecursionlimit(1000000000)
def zmierz(f,n=100):
    """Funkcja mierzy czas wykonania podanej funkcji"""
    t0 = time.time()
    f(n)
    t1= time.time()
    return t1 - t0

def silnia(n):
    if n>1:
        return silnia(n-1)*n
    else:
        return 1
print("silnia rekurencyjnie", zmierz(silnia))


def silnia2(n):
    b = 1
    for i in range(0,n):
        b = b*(i+1)
    return b 




print("silnia iteracyjnie", zmierz(silnia2, 100)) 


def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    elif n==1:
        return 1
    else:
        return 0
    
def fib2(n):
    a=1 
    b=1
    for i in range(0,n):
       a,b= b, a+b
       return a
       
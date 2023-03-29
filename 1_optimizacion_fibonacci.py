# DEPENDENCIAS ============================================
from time import time
import sys

# FUNCIONES ===============================================

def fibonacci_recursivo(n):

    

    print(f'Calculando fibonacci de {n}')
   
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):

    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado


# MAIN FUNCTION ===========================================

def main():

    sys.setrecursionlimit(5000)


    t0 = time()

    print(fibonacci_dinamico(4000))
    

    tf = time()

    print(f'Tiempo fibonacci dinamico: {tf - t0} segundos')
    




# ENTRY POINT =============================================

if __name__ == "__main__":
    main()
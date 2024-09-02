#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculer la factorielle d'un entier non négatif n de manière recursive

    Paramètres:
    n (int): un entier non negatif dont la factorielle doit être calculée

    Returns:
    int: la factorielle du nombre d'entrée n. si n est 0, ça renvoie 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# avoir le nombre d'entrée a partir d'arguments de la ligne de com
f = factorial(int(sys.argv[1]))

# Print la factorielle calculée 
print(f)

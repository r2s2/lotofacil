import math

def factorial(n):
    return math.factorial(n)

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n = 60
k = 6
total_combinations = combinations(n, k)
print(f"O número total de combinações possíveis é: {total_combinations}")



'''5. Leibniz harmonic triangle'''
def LeibnizHarmonicTriangle(n):
    C = [[0 for x in range(n + 1)]
         for y in range(n + 1)]

    for i in range(n + 1):                     # Calculate value of Binomial Coefficient in bottom up manner
        for j in range(min(i, n) + 1):

            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1
            else:                              # Calculate value using previously stored values
                C[i][j] = (C[i - 1][j - 1] +
                           C[i - 1][j])

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("1/", end="")
            print(i * C[i - 1][j - 1],
                  end=" ")
        print()

# LeibnizHarmonicTriangle(4)


import fractions
rownr = int(input())

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


for j in range(1, rownr + 1):
    for k in range(1, j + 1):
        ourvalue = k *(factorial(j) / (factorial(k) * factorial(j - k)))
        print(fractions.Fraction(1, int(ourvalue)), end = " ")
    print('')

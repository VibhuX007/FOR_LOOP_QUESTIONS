#DEFINE A FUNCTION TO FIND OUT SUN OF THE FOLLOWING WHERE NUMBER IS GIVEN BY THE USER?
def sum_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/factorial(i)
    return sum

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n=int(input('Enter the number: '))
print('Sum of series = ',sum_series(n))
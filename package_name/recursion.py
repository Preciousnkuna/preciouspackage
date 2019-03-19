def sum_array(array):
    return sum(items for items in array)


def fibonacci(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

   def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    word = word[::-1]
    return word

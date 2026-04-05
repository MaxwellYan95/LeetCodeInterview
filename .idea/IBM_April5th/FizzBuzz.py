#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for num in range(1, n+1):
        third = num % 3 == 0;
        fifth = num % 5 == 0;
        if third and fifth:
            print("FizzBuzz")
        elif third:
            print("Fizz")
        elif fifth:
            print("Buzz")
        else:
            print(num)
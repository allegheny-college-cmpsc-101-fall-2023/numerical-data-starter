# TODO: Make sure that you understand function compute_mean.
# TODO: Answer the quesions about compute_mean in the reflection.

# define a function that can compute the arithmetic
# mean of a list of numerical values; note that
# this function does not have type annotations
def compute_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N
    return mean
numbers = [5,1,7,99,4]
print(f'the mean of the ints in the list is: {compute_mean(numbers)}')

numbers = [5.1,1.1,7.1,99.1,4.1]
print(f'the mean of the floats in the list is: {compute_mean(numbers)}')


# TODO: convert the following code from a past class into a function
# that returns the largest_divisor of an input number, x.
# TODO: use type annotations for the input and output.
# TODO: use the function to find the largest divisor of 1717.
# TODO: answer the questions about your new function in the reflection.

x = int(101)

# initialize the final solution
largest_divisor = None

# test every number from 2 to x-1 and check divisibility exhaustively with a for loop
for divisor in range(2,x):

  if x % divisor == 0: # % operator returns remainders
    largest_divisor = x/divisor
    break

print(f'the largest divisor of {x} is {largest_divisor}')

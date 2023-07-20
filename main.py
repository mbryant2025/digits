import time

input = [5,7,9,11,13,23]
target = 463

start_time = time.perf_counter()

# Operations
operations = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: y - x, lambda x, y: x * y, lambda x, y: x / y, lambda x, y: y / x]

# Operation strings
operation_strings = ["+", "-", "--", "*", "/", "\\"]

# Operation dictionary
operation_dict = {operations[i]: operation_strings[i] for i in range(len(operations))}

# Class to store digits and the list of operations that got to that point
class DigitHistory:
    def __init__(self, digits, history = []):
        self.digits = digits
        self.history = history

solutions = []

print_spacer = '--------------------------------------------------------'

# Recursively reduce the input digits by performing one operation at a time
def reduce(digits: DigitHistory):

    # Add all the digits to the list of possible answers
    if target in digits.digits:
        if not solutions:
            print("First solution found:")
            print(digits.history)
            print(print_spacer)
        solutions.append(digits.history)

    if len(digits.digits) == 1:
        return

    # Loop through all operations on every pair of digits
    for i in range(len(digits.digits)):
        # Loop over triangular region as we have all operations for all pairs (communative + and *, both directions for - and /)
        for j in range(i):
            for op in operations:
                # Skip if potential division by zero
                # Perform operation
                try:
                    result = op(digits.digits[i], digits.digits[j])
                except ZeroDivisionError:
                    continue
                # If the result is not a whole number, skip it
                if int(result) != result:
                    continue
                if result < 0:
                    continue
                # Find the digits in the list and remove them
                remove_1 = digits.digits[i]
                remove_2 = digits.digits[j]
                # Make a copy of digits without the two digits
                new_digits = digits.digits.copy()
                new_digits.remove(remove_1)
                new_digits.remove(remove_2)
                # Add the result of the operation to the list
                new_digits.append(result)
                # print(new_digits)
                new_dh = DigitHistory(new_digits, digits.history.copy())
                # Add the history of the operation to the list
                new_dh.history.append((remove_1, operation_dict[op], remove_2))
                # Recursively reduce the new list
                reduce(new_dh)


print(print_spacer)

print(f'Input: {input}')
print(f'Target: {target}')

print(print_spacer)

reduce(DigitHistory(input))

print(f'Execution time: {round(time.perf_counter() - start_time, 2)} seconds')

# Sort the solutions by length
solutions.sort(key = lambda x: len(x))

# Print the shortest solution
if solutions:
    print(f'Number of solutions found: {len(solutions)}')
    print('Shortest solution:')
    print(solutions[0])
else:
    print('No solutions found.')

# CSES Problem: Number Spiral
# URL: https://cses.fi/problemset/task/1071

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    input_data = [int(i) for i in input_data]

    t = input_data[0]
    iterator = range(1, 2 * t + 1, 2)
    # TODO: Write your solution logic here

    for i in iterator:
        if i + 1 >= len(input_data):
            break  # Prevent out of bounds if input is malformed
        
        # Get row & col
        y = input_data[i]
        x = input_data[i+1]

        # If col is greater
        if x > y:
            # The spiral fills downwards along this column.
            if x % 2 == 0:
                print((x - 1) ** 2 + y)

            # The spiral fills upwards along this column.
            else:
                print((x ** 2) + 1 - y)
        
        # If row is greater
        else:
            # The spiral fills backwards from the end of the y x y block.
            if y % 2 == 0:
                print((y ** 2) + 1 - x)

            # The spiral fills forwards across this row.
            else:
                print((y - 1) ** 2 + x)
                

if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Looping on N numbers list
# S.C: O(N)     --> Creeating list of ~ N numbers combine

# python run_tests.py "Introductory-Problems/6. Number Spiral"
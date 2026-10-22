# CSES Problem: Number Spiral
# URL: https://cses.fi/problemset/task/1071

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    # TODO: Write your solution logic here

    for i in range(1, len(input_data), 2):
        y = input_data[i]
        x = input_data[i+1]
        print(y, x)



if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Looping on N numbers
# S.C: O(N)     --> Creeating list of ~ N numbers combine

# python run_tests.py "Introductory-Problems/6. Number Spiral"
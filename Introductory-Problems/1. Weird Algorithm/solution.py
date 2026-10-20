# CSES Problem: Weird Algorithm
# URL: https://cses.fi/problemset/task/1068

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here
    # Create a copy
    num = n

    print(num, end=" ")

    while num != 1:
        # Even, divide it by 2
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1

        print(num, end=" ")


if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Loop till constant no. of steps
# S.C: O(1)     --> Variables storing int value

# python run_tests.py "Introductory-Problems/1. Weird Algorithm"
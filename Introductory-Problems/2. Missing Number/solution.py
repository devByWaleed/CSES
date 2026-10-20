# CSES Problem: Missing Number
# URL: https://cses.fi/problemset/task/1083

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    # Sum of all numbers in range(1, n) includive
    range_sum = n * (n + 1) // 2

    # List of all numbers in int form
    list_int = [int(input_data[i]) for i in range(1,len(input_data))]

    # Subtraction gives the missing number
    print(range_sum - sum(list_int))


if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Creating + SUM of N size array
# S.C: O(N)     --> Array of size N used

# python run_tests.py "Introductory-Problems/2. Missing Number"
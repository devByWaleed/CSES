# CSES Problem: Trailing Zeros
# URL: https://cses.fi/problemset/task/1618

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    # Will not work for 10⁹ int
    # fact = math.factorial(n)

    zeros = 0
    num = n

    while num >= 5:
        # Remainder will be count for trailing zeros
        remainder = num // 5
        zeros += remainder

        # Continue the division process
        num //= 5

    print(zeros)


if __name__ == '__main__':
    solve()

# T.C: O(LOG•5 N)   --> Log 5 division of N
# S.C: O(1)         --> Variables storing int value

# python run_tests.py "Introductory-Problems/10. Trailing Zeros"
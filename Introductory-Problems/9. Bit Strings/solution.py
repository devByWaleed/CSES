# CSES Problem: Bit Strings
# URL: https://cses.fi/problemset/task/1617

import sys

# Bit manipulation
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    # Final answer
    result = 1

    # Base for calculation
    base = 2

    # Exponent
    exponent = n

    # Modulo to keep intgere limit
    MOD = 1_000_000_007

    while exponent != 0:
        # If rightmost bit is 1, mul base into result
        if (exponent & 1) == 1:
            result = (result * base) % MOD

        # Double the base
        base = (base ** 2) % MOD

        # Drop that bit
        exponent >>= 1

    print(result)       

if __name__ == '__main__':
    solve()

# T.C: O(LOG N)     --> Log times: number of bits in N ∝ log2(N)
# S.C: O(1)         --> Storing variables


# Built-in pow()
'''
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    modulo = 1_000_000_000 + 7
    bit_strings = pow(2, n, modulo)

    print(bit_strings)


if __name__ == '__main__':
    solve()

# T.C: O(LOG N)     --> Modular Exponential calculation for N
# S.C: O(1)         --> memory to store 2 ^ N answer
'''


# Brute Force (Accepted)
'''
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    bit_strings = 2 ** n

    print(bit_strings % (1_000_000_000 + 7))


if __name__ == '__main__':
    solve()

# T.C: O(N LOG N)     --> Exponential calculation for N
# S.C: O(N)           --> memory to store 2 ^ N answer
'''

# python run_tests.py "Introductory-Problems/9. Bit Strings"
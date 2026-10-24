# CSES Problem: Two Knights
# URL: https://cses.fi/problemset/task/1072

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    for k in range(1, n+1):
        # Total pairs in grid
        total_pairs = (k**2 * (k**2 - 1)) // 2

        # Total attacking points * total valid configs of grid
        # Possible grids in k x k: row & col
        attacking = 2 * 2 * (k - 1) * (k - 2)

        print(total_pairs - attacking)


if __name__ == '__main__':
    solve()

# T.C: O(K)     --> K times loop
# S.C: O(1)     --> Variables storing int value

# python run_tests.py "Introductory-Problems/7. Two Knights"
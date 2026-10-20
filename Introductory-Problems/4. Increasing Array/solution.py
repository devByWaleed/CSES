# CSES Problem: Increasing Array
# URL: https://cses.fi/problemset/task/1094

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    array = input_data[1:]
    # TODO: Write your solution logic here

    array = [int(i) for i in array]

    moves = 0

    for i in range(1, n):
        # If smaller, add the difference and modify the array value
        if array[i] < array[i-1]:
            moves += (array[i-1] - array[i])
            array[i] = array[i-1]

    print(moves)


if __name__ == '__main__':
    solve()

# T.C: O(N)     --> str-to-int conversion + N times loop
# S.C: O(N)     --> Array of size N used

# python run_tests.py "Introductory-Problems/4. Increasing Array"
# CSES Problem: Permutations
# URL: https://cses.fi/problemset/task/1070/

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    # Creating lists for even and odd numbers
    even = [i for i in range(1, n+1) if i % 2 == 0]
    odd = [i for i in range(1, n+1) if i % 2 == 1]

    # Combine it by even 1st
    combine = even + odd

    # For printing last number
    flag = True

    for i in range(0, n-1):
        # If rule follows, print beautiful permutation
        if abs(combine[i] - combine[i+1]) > 1:
            print(combine[i], end=" ")
        
        # Print message and restrict to display last number
        else:
            print("NO SOLUTION")
            flag = False
            break

    if flag:
        print(combine[-1], end=" ")


if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Looping on N numbers
# S.C: O(N)     --> Creeating list of ~ N numbers combine

# python run_tests.py "Introductory-Problems/5. Permutations"
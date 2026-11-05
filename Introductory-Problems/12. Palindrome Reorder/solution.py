# CSES Problem: Palindrome Reorder
# URL: https://cses.fi/problemset/task/1755

import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    n = len(s)
    # TODO: Write your solution logic here

    # Edge case: single character
    if n == 1:
        print(s)
        return

    # Frequncy map
    frequency = Counter(s)

    odd_chars = [char for char, count in frequency.items() if count % 2 != 0]

    if (n % 2 == 0 and len(odd_chars) > 0) or (n % 2 == 1 and len(odd_chars) != 1):
        print("NO SOLUTION")
        return

    left_half = []
    middle = ""

    # Appending left half + checking middle char (frequency 1)
    for char, count in frequency.items():
        if count % 2 != 0:
            middle = char
        left_half.append(char * (count // 2))

    left_str = "".join(left_half)
    right_str = left_str[::-1]  # Mirror the left half to create the right half

    # Assemble the final palindrome
    palindrome = left_str + middle + right_str
    print(palindrome)


if __name__ == '__main__':
    solve()

# T.C: O(N)     --> Looping through string + MAP
# S.C: O(N)     --> String of length N stored

# python run_tests.py "Introductory-Problems/12. Palindrome Reorder"
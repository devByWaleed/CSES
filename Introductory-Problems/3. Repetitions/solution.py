# CSES Problem: Repetitions
# URL: https://cses.fi/problemset/task/1069

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    # TODO: Write your solution logic here
    
    left = 0

    # Final length
    max_length = 0

    for right in range(len(s)):
        # If not same, update final length
        if s[right] != s[left]:
            max_length = max(max_length, right - left)

            # Update the window
            while left != right:
                left += 1

        # If chars are same, final update as edge
        max_length = max(max_length, right - left + 1)
        

    print(max_length)


if __name__ == '__main__':
    solve()

# python run_tests.py "Introductory-Problems/3. Repetitions"
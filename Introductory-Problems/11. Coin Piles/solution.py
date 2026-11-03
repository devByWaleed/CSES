# CSES Problem: Coin Piles
# URL: https://cses.fi/problemset/task/1754

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    input_data = [int(i) for i in input_data]
    
    t = input_data[0]
    iterator = range(1, 2 * t + 1, 2)
    # TODO: Write your solution logic here


    for i in iterator:
        if i + 1 >= len(input_data):
            break  # Prevent out of bounds if input is malformed

        a = input_data[i]
        b = input_data[i+1]

        # We are negating 3 piles at a time, means sum will be multiple of 3
        if (a + b) % 3 == 0:
            max_pile = max(a, b)
            min_pile = min(a, b)

            # Larger pile can't be > twice the size of smaller pile
            if max_pile <= 2 * min_pile:
                print("YES")
            else:
                print("NO")
        
        # Sum is not multiple of 3
        else:
            print("NO")


if __name__ == '__main__':
    solve()

# T.C: O(T)   --> Loop through Number of test cases time
# S.C: O(T)         --> Array storing T size data

# python run_tests.py "Introductory-Problems/11. Coin Piles"
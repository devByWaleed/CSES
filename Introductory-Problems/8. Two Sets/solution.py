# CSES Problem: Two Sets
# URL: https://cses.fi/problemset/task/1092

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    # TODO: Write your solution logic here

    total_sum = n * (n + 1) // 2

    if total_sum % 2 != 0:
        print("NO")
    else:
        print("YES")

        # Target su for single set
        target_sum = total_sum // 2

        # 2 sets
        set1 = set()
        set2 = set()

        # PART 1: Calculation
        for i in range(n, 0, -1):
            # If i in target_sum range, add and decrement sum
            if target_sum >= i:
                set1.add(i)
                target_sum -= i
            else:
                # Should be add to 2nd set
                set2.add(i)

        # PART 2: Printing
        print(len(set1))
        for i in set1:
            print(i, end=" ")
        print()

        print(len(set2))
        for j in set2:
            print(j, end=" ")
        print()



if __name__ == '__main__':
    solve()

# T.C: O(N)
# S.C: O(N)

# python run_tests.py "Introductory-Problems/8. Two Sets"
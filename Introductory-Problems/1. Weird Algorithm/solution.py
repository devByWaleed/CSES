# CSES Problem: Weird Algorithm
# URL: https://cses.fi/problemset/task/1068

# def solve(n):
def solve():
    # Read the single integer from standard input
    n = int(input())
    # Create a copy
    num = n

    print(num, end=" ")

    while num != 1:
        # Even, divide it by 2
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1

        print(num, end=" ")


if __name__ == "__main__":
  solve()

# solve(3)      # 3 10 5 16 8 4 2 1
# solve(13)      # 13 40 20 10 5 16 8 4 2 1
# solve(7)      # 13 40 20 10 5 16 8 4 2 1
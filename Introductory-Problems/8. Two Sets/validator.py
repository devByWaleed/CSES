
def validate(input_text, expected_output, actual_output):
    try:
        n = int(input_text.split()[0])
        tokens = actual_output.split()

        if not tokens:
            return False

        total = n * (n + 1) // 2

        if total % 2:
            return tokens == ["NO"]

        if len(tokens) < 3 or tokens[0] != "YES":
            return False

        a_count = int(tokens[1])

        if a_count < 0 or 2 + a_count >= len(tokens):
            return False

        a = list(map(int, tokens[2:2 + a_count]))
        pos = 2 + a_count

        b_count = int(tokens[pos])

        if b_count < 0 or pos + 1 + b_count != len(tokens):
            return False

        b = list(map(int, tokens[pos + 1:]))

        if len(a) != a_count or len(b) != b_count:
            return False

        if any(x < 1 or x > n for x in a + b):
            return False

        if len(set(a)) != len(a) or len(set(b)) != len(b):
            return False

        if set(a) & set(b):
            return False

        if sorted(a + b) != list(range(1, n + 1)):
            return False

        return sum(a) == sum(b)

    except (ValueError, IndexError):
        return False

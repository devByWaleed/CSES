import os
import subprocess
import sys


def run_tests_for_folder(folder_name):
    tests_folder = os.path.join(folder_name, "tests")
    solution_path = os.path.join(folder_name, "solution.py")

    if not os.path.exists(folder_name):
        print(f"❌ Error: Folder '{folder_name}' does not exist.")
        return

    if not os.path.exists(tests_folder):
        print(f"❌ Error: No 'tests' folder found inside '{folder_name}'.")
        return

    if not os.path.exists(solution_path):
        print(f"❌ Error: No 'solution.py' found inside '{folder_name}'.")
        return

    in_files = sorted(
        [
            f
            for f in os.listdir(tests_folder)
            if f.endswith(".in") and not f.endswith(".out")
        ],
        key=lambda x: int(os.path.splitext(x)[0])
        if os.path.splitext(x)[0].isdigit()
        else x,
    )

    if not in_files:
        print("⚠️ No input test files found in the tests directory.")
        return

    print(f"\n🚀 Running {len(in_files)} test cases for: {folder_name}...")
    print("-" * 50)

    passed_count = 0

    for in_file in in_files:
        test_id = os.path.splitext(in_file)[0]
        in_path = os.path.join(tests_folder, in_file)
        out_path = os.path.join(tests_folder, f"{test_id}.out")

        if not os.path.exists(out_path):
            print(f"Test {test_id}: ⚠️ Skipping (Missing corresponding .out file)")
            continue

        with open(out_path, "r", encoding="utf-8") as f:
            expected_output = f.read().strip()

        try:
            with open(in_path, "r", encoding="utf-8") as inf:
                result = subprocess.run(
                    [sys.executable, solution_path],
                    stdin=inf,
                    capture_output=True,
                    text=True,
                    timeout=5,
                )

            actual_output = result.stdout.strip()

            if actual_output == expected_output:
                print(f"Test {test_id}: ✅ PASSED")
                passed_count += 1
            else:
                print(f"Test {test_id}: ❌ FAILED")
                print(f"  Expected: {repr(expected_output)}")
                print(f"  Got:      {repr(actual_output)}")

        except subprocess.TimeoutExpired:
            print(f"Test {test_id}: ❌ FAILED (Time Limit Exceeded)")
        except Exception as e:
            print(f"Test {test_id}: ❌ ERROR ({e})")

    print("-" * 50)
    print(f"🎯 Results: {passed_count}/{len(in_files)} test cases passed.\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <path_to_problem_folder>")
        print(
            "Example: python run_tests.py"
            ' "Introductory-Problems/Missing Number"'
        )
    else:
        run_tests_for_folder(sys.argv[1])
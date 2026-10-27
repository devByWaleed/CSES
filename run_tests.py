
import importlib.util
import os
import subprocess
import sys


def natural_sort_key(filename):
    """Sort numbered tests numerically: 1, 2, 10 instead of 1, 10, 2."""
    name = os.path.splitext(filename)[0]

    if name.isdigit():
        return (0, int(name))

    return (1, name.lower())


def load_validator(folder_name):
    """
    Load an optional validator.py from the problem folder.

    Expected function:
        validate(input_text, expected_output, actual_output) -> bool
    """
    validator_path = os.path.join(folder_name, "validator.py")

    if not os.path.isfile(validator_path):
        return None

    spec = importlib.util.spec_from_file_location(
        "problem_validator", validator_path
    )

    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load validator.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not callable(getattr(module, "validate", None)):
        raise RuntimeError(
            "validator.py must define validate("
            "input_text, expected_output, actual_output)"
        )

    return module.validate


def show_difference(expected, actual):
    """Show the first differing token and character for debugging."""
    expected_tokens = expected.split()
    actual_tokens = actual.split()

    if expected_tokens == actual_tokens:
        print("  Token sequences match; check the custom validator.")
        return

    for i in range(max(len(expected_tokens), len(actual_tokens))):
        e = expected_tokens[i] if i < len(expected_tokens) else "<MISSING>"
        a = actual_tokens[i] if i < len(actual_tokens) else "<MISSING>"

        if e != a:
            print(f"  First differing token: {i + 1}")
            print(f"  Expected token: {e!r}")
            print(f"  Actual token:   {a!r}")
            break

    # Find the first differing character in the raw output.
    limit = min(len(expected), len(actual))
    index = next(
        (i for i in range(limit) if expected[i] != actual[i]),
        limit,
    )

    if index < limit or len(expected) != len(actual):
        start = max(0, index - 20)
        end_expected = min(len(expected), index + 40)
        end_actual = min(len(actual), index + 40)

        print(f"  First differing character index: {index}")
        print(
            f"  Expected near difference: "
            f"{expected[start:end_expected]!r}"
        )
        print(
            f"  Actual near difference:   "
            f"{actual[start:end_actual]!r}"
        )
        print(
            f"  Character codes: expected="
            f"{ord(expected[index]) if index < len(expected) else 'END'}, "
            f"actual="
            f"{ord(actual[index]) if index < len(actual) else 'END'}"
        )

    print(
        f"  Output lengths: expected={len(expected)}, "
        f"actual={len(actual)}"
    )


def run_tests_for_folder(folder_name):
    tests_folder = os.path.join(folder_name, "tests")
    solution_path = os.path.join(folder_name, "solution.py")

    if not os.path.isdir(folder_name):
        print(f"❌ Error: Folder '{folder_name}' does not exist.")
        return

    if not os.path.isdir(tests_folder):
        print(f"❌ Error: No 'tests' folder found inside '{folder_name}'.")
        return

    if not os.path.isfile(solution_path):
        print(f"❌ Error: No 'solution.py' found inside '{folder_name}'.")
        return

    try:
        validator = load_validator(folder_name)
    except Exception as exc:
        print(f"❌ Error loading validator: {exc}")
        return

    in_files = sorted(
        [
            f
            for f in os.listdir(tests_folder)
            if f.endswith(".in")
        ],
        key=natural_sort_key,
    )

    if not in_files:
        print("⚠️ No input test files found.")
        return

    print(f"\n🚀 Running {len(in_files)} test cases for: {folder_name}...")
    print("-" * 60)

    if validator:
        print("🧪 Using custom validator.py")
    else:
        print("🔎 Using whitespace-insensitive token comparison")

    passed_count = 0
    failed_count = 0
    skipped_count = 0

    for in_file in in_files:
        test_id = os.path.splitext(in_file)[0]
        in_path = os.path.join(tests_folder, in_file)
        out_path = os.path.join(tests_folder, f"{test_id}.out")

        if not os.path.isfile(out_path):
            print(f"Test {test_id}: ⚠️ SKIPPED (missing .out file)")
            skipped_count += 1
            continue

        try:
            # utf-8-sig also handles files containing a UTF-8 BOM.
            with open(in_path, "r", encoding="utf-8-sig") as f:
                input_text = f.read()

            with open(out_path, "r", encoding="utf-8-sig") as f:
                expected_output = f.read()

            result = subprocess.run(
                [sys.executable, solution_path],
                input=input_text,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=5,
            )

            actual_output = result.stdout

            if result.returncode != 0:
                print(f"Test {test_id}: ❌ RUNTIME ERROR")
                print(f"  Exit code: {result.returncode}")

                if result.stderr:
                    print(f"  Error:\n{result.stderr.strip()}")

                failed_count += 1
                continue

            if validator is not None:
                passed = bool(
                    validator(
                        input_text,
                        expected_output,
                        actual_output,
                    )
                )
            else:
                # Ignore spaces, tabs, and newlines between tokens.
                passed = (
                    actual_output.split()
                    == expected_output.split()
                )

            if passed:
                print(f"Test {test_id}: ✅ PASSED")
                passed_count += 1
            else:
                print(f"Test {test_id}: ❌ FAILED")

                if validator is None:
                    show_difference(expected_output, actual_output)
                else:
                    print("  Custom validator rejected the output.")
                    show_difference(expected_output, actual_output)

        except subprocess.TimeoutExpired:
            print(f"Test {test_id}: ❌ TIME LIMIT EXCEEDED")
            failed_count += 1

        except Exception as exc:
            print(f"Test {test_id}: ❌ ERROR ({exc})")
            failed_count += 1

    print("-" * 60)
    print(f"✅ Passed:  {passed_count}")
    print(f"❌ Failed:  {failed_count}")
    print(f"⚠️ Skipped: {skipped_count}")
    print(f"🎯 Results: {passed_count}/{len(in_files)} test cases passed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <path_to_problem_folder>")
        print(
            'Example: python run_tests.py '
            '"Introductory-Problems/1. Weird Algorithm"'
        )
    else:
        run_tests_for_folder(sys.argv[1])

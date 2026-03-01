# Simple test script for jump_k C++ binary
import subprocess


def run_test(input_str, expected_output):
    proc = subprocess.run(['./jump_k'], input=input_str.encode(), capture_output=True, timeout=5)
    output = proc.stdout.decode().strip()
    print(f"Input: {input_str!r}\nExpected: {expected_output!r}\nGot: {output!r}\nTest: {'PASS' if output == expected_output else 'FAIL'}\n")
    return output == expected_output

if __name__ == "__main__":
    # Add your test cases here (input, expected_output)
    tests = [
        ("3 2 1 2 3\n", "..."),  # TODO: Replace ... with actual expected output
        ("5 1 2 3 4 5\n", "..."),
        ("1 42\n", "..."),
    ]
    all_passed = True
    for inp, exp in tests:
        if not run_test(inp, exp):
            all_passed = False
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")

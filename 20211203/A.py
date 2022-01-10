def resolve():
    N = int(input())
    if N<10:
        print(f"AGC00{N}")
    elif N < 42:
        print(f"AGC0{N}")
    else:
        print(f"AGC0{N+1}")

resolve()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """42"""
        output = """AGC043"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19"""
        output = """AGC019"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """AGC001"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """50"""
        output = """AGC051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

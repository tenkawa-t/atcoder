def resolve():
    t = int(input())
    print(f(f(f(t)+t) + f(f(t))))

def f(x):
    return x * x + 2 * x +3

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
        input = """0"""
        output = """1371"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """722502"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10"""
        output = """1111355571"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

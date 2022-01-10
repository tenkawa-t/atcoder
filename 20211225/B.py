def resolve():
    L, R = map(int, input().split())
    S = input()
    output = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(output)

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
        input = """3 7
abcdefgh"""
        output = """abgfedch"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 7
reviver"""
        output = """reviver"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 13
merrychristmas"""
        output = """meramtsirhcyrs"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()

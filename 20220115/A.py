def resolve():
    # X, Y = map(int, input().split())
    S = input()
    a = S[0]
    b = S[1]
    c = S[2]
    print(int(a+b+c)+int(b+c+a)+int(c+a+b))
resolve()

import sys
from io import StringIO
import unittest
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
        input = """123"""
        output = """666"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999"""
        output = """2997"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

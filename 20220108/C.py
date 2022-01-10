import math
def resolve():
    k = int(input())
    b = bin(k)
    b = b.replace("0b", "")
    b = b.replace("1", "2")
    print(b)


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
        input = """3"""
        output = """22"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11"""
        output = """2022"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """923423423420220108"""
        output = """220022020000202020002022022000002020002222002200002022002200"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

import itertools
import operator
import functools
import math

def resolve():
    n = input()
    h_list = list(map(int, input().split()))
    h0 = h_list[0]
    for h in h_list[1:]:
        if h > h0:
            h0 = h
        else:
            break
    print(h0)
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
        input = """5
1 5 10 4 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
100 1000 100000"""
        output = """100000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
27 1828 1828 9242"""
        output = """1828"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

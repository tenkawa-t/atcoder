import itertools
import operator
import functools
import math

def resolve():
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    for i in point:
        for j in point:
            temp = distance(i, j)
            if temp > max:
                max = temp

    print(max)


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)


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
        input = """3
0 0
0 1
1 1"""
        output = """1.4142135624"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
315 271
-2 -621
-205 -511
-952 482
165 463"""
        output = """1455.7159750446"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

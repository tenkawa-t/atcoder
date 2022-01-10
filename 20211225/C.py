import itertools
import operator
import functools

def resolve():
    import sys
    input = sys.stdin.readline
    N,X = map(int, input().split())
    L_list = [list(map(int, input().split()[1:])) for _ in range(N)]
    prod = list(map(func, list(itertools.product(*L_list))))
    count = prod.count(X)
    print(count)

def func(li):
    return functools.reduce(operator.mul, li)





    # for i in range(P, Q + 1):
    #     for j in range(R, S + 1):
    #         dx = A - i
    #         dy = B - j
    #         print('#' if (dx == dy or dx == -dy) else '.', end='')
    #         # if (i, j) in black:
    #         #
    #         #     temp += "#"
    #         # elif
    #         #
    #         # else:
    #         #
    #         #     temp += "."
    #     print()
        # print("".join(temp))
    mass = [["."]*(S-R+1) for i in range(Q - P + 1)]
    x = max(P-A, R-B)
    y = min(Q-A, S-B)
    for i in range(x, y+1):
        mass[a + i -p][b +i -r] = "#"


    x = max(p-a, r-b)
    y = min(q-a, s-b)
    for i in range(x, y+1):
        mass[a + i -p][b +i -r] = "#"
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
        input = """2 40
3 1 8 4
2 10 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 200
3 10 10 10
3 10 10 10
5 2 2 2 2 2"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1000000000000000000
2 1000000000 1000000000
2 1000000000 1000000000
2 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

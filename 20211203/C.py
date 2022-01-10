def resolve():
    import sys
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

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
        input = """5 3 2
1 5 1 5"""
        output = """...#.
#.#..
.#...
#.#..
...#."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3 3
4 5 2 5"""
        output = """#.#.
...#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000"""
        output = """#.#
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

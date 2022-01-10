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
        input = """3 5
3 1
4 2
2 3"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100
6 2
1 5
3 9
8 7"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291"""
        output = """2357689932073"""
        self.assertIO(input, output)

def resolve():
    N, W = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i, (v, w) in enumerate(vw):
        for j in range(W + 1):
            for k in range(w):
                dp[i + 1][j] = dp[i][j]
                if j - w >= 0:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
    print(dp[-1][-1])

if __name__ == "__main__":
    unittest.main()

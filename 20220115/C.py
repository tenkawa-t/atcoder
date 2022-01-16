from collections import defaultdict
import sys

def resolve():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    y = defaultdict(lambda : [])
    for i in range(n):
        y[a_list[i]].append(i + 1)
    for _ in range(q):
        x, k = map(int, input().split())
        ans = -1
        if len(y[x]) >= k:
            ans = y[x][k-1]
        print(ans)
# resolve()




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
        input = """6 8
1 1 2 3 1 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1"""
        output = """1
2
5
-1
3
6
-1
-1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
0 1000000000 999999999
1000000000 1
123456789 1"""
        output = """2
-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    r, ans, tmp = 0, 0, 0
    for l in range(n):
        while r < n :
            tmp += s[r]
            r += 1
            if tmp == k:
                ans += 1
        if l == r:
            r += 1
        else:
            tmp = 0
            r = l +1
    print(ans)


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
        input = """6 5
8 -3 5 7 0 -4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 -1000000000000000
1000000000 -1000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
    from itertools import product

    N, M = map(int, input().split())
    sw_list = [list(map(int, input().split()[1:])) for _ in range(M)]
    p = list(map(int, input().split()))

    ans = 0
    for bits in product([0, 1], repeat=N):
        check = [0]*M

        for i, sw in enumerate(sw_list):
            temp = 0
            for s in sw:
                if bits[s-1]== 1:
                    temp += 1  # bit tentou sw kakunin
            if temp % 2 == p[i]:
                check[i] = 1
        if all(check):
            ans += 1
    print(ans)

if __name__ == "__main__":
    unittest.main()

def resolve():
    from heapq import heappop, heappush
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    heap = []
    for i in range(K):
        heappush(heap, P[i])
    print(heap[0])
    for i in range(K, N):
        x = heappop(heap)
        heappush(heap, max(x, P[i]))
        print(heap[0])

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
        input = """3 2
1 2 3"""
        output = """1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 5
3 7 2 5 11 6 1 9 8 10 4"""
        output = """2
3
3
5
6
7
7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

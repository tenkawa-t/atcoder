# def resolve():
#     a, n = map(int, input().split())
#
#     if n%a!=0 and alt(n)%a!=0:
#         print(-1)
#     else:
#
#         count = 0
#         target = 1
#         for i in range(100000):
#             if target >10:
#                 if alt(target)==n:
#                     count += 1
#                     print(count)
#                     break
#             count += 1
#             target *= a
#             if target==n:
#
#                 print(count)
#                 break
#
# def alt(a):
#     if a<10:
#         return a
#     a = str(a)
#     if len(a)==2:
#         return int(a[1]+a[0])
#     else:
#         return int(a[int(len(a))]+a[1:int(len(a))-1] + a[0])
#
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i and n//i<10:
#                 upper_divisors.append(n//i)
#         i += 1
#     return reversed(lower_divisors + upper_divisors[::-1])

from collections import deque
def resolve():
    INF = 10 ** 9
    MAX = 10 ** 6

    a, N = map(int, input().split())
    dist = [INF] * (MAX + 10)
    dist[1] = 0
    q = deque([1])
    while q:
        v = q.popleft()
        if v % 10:
            s = str(v)
            nv = int(s[-1] + s[:-1])
            if dist[nv] > dist[v] + 1:
                dist[nv] = dist[v] + 1
                q.append(nv)
        nv = v * a
        if nv >= MAX:
            continue
        if dist[nv] > dist[v] + 1:
            dist[nv] = dist[v] + 1
            q.append(nv)

    answer = dist[N]
    if answer == INF:
        answer = -1
    print(answer)


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
        input = """3 72"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 611"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 767090"""
        output = """111"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

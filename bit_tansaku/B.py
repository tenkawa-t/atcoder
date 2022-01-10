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
        input = """229 390"""
        output = """Hard"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789 9876543210"""
        output = """Easy"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """223456789 9876543210"""
        output = """Hard"""
        self.assertIO(input, output)

# def resolve():
#     A, B = input().split()
#     num_a = len(A)
#     num_b = len(B)
#
#     if num_a == num_b:
#         for i in range(num_a - 1, 0, -1):
#             if int(A[i]) + int(B[i]) >= 10:
#                 print('Hard')
#                 break
#         else:
#             print('Easy')
#     elif num_a > num_b:
#         dif = num_a - num_b
#         for i in range(num_a-1, dif-1, -1):
#             if int(A[i]) + int(B[i-dif]) >= 10:
#                 print('Hard')
#                 break
#         else:
#             print('Easy')
#     elif num_a < num_b:
#         dif = num_b-num_a
#         for i in range(num_b-1, dif-1, -1):
#             if int(A[i-dif]) + int(B[i]) >= 10:
#                 print('Hard')
#                 break
#         else:
#             print('Easy')


def resolve():
    A, B = input().split()
    A = list(reversed(A))
    B = list(reversed(B))
    num_a = len(A)
    num_b = len(B)
    min_ab = min(num_a, num_b)

    for i in range(min_ab):
        if int(A[i]) + int(B[i]) >= 10:
            print('Hard')
            break
    else:
        print('Easy')


if __name__ == "__main__":
    unittest.main()

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
        input = """##
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """.#
#."""
        output = """No"""
        self.assertIO(input, output)

def resolve():
    S1 = input()
    S2 = input()
    S1_1 = S1[0]
    S1_2 = S1[1]

    S2_1 = S2[0]
    S2_2 = S2[1]

    if S1_1 =='#' and S1_2 =='#':
        print("Yes")
    elif S2_1 =='#' and S2_2 =='#':
        print("Yes")
    elif S1_1 =='#' and S2_1 =='#':
        print("Yes")
    elif S1_2 == '#' and S2_2 == '#':
        print("Yes")
    else:
        print('No')

if __name__ == "__main__":
    unittest.main()

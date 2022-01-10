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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)
def resolve():
    abcd = input()
    n = 4 -1
    ans = 0

    for bit in range(1 << n):
        N = abcd[0]
        for i in range(n):
            N += " "
            if bit & (1 << i):
                N += '-'
            else:
                N += '+'
            N += abcd[i + 1]
            N += ' '
        N_int = sum(map(int, N.split()))
        if N_int == 7:
            ans = N.replace(' ', '')
            print(f"{ans}=7")
            break

if __name__ == "__main__":
    unittest.main()

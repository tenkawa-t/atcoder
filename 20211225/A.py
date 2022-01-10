
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
        input = """80 94"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000 63"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """270 750"""
        output = """48"""
        self.assertIO(input, output)

def resolve():
    X, Y = map(int, input().split())
    if Y - X < 0:
        print(0)
    else:
        kitte = (Y - X) // 10
        if (Y - X) % 10 != 0:
            kitte += 1
        print(kitte)

# resolve()
if __name__ == "__main__":
    unittest.main()

# 英小文字で構成された、ランダムな100文字を生成
import random
import string
n = 100
val_str = ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
print(val_str)

from collections import defaultdict
d = defaultdict(list)


for key in val_str:
    d[key] += 1

print(d)
import time
dict = {i: i for i in range(10_000_000)}

start = time.time()
count = 0
for _ in range(10_000_200):
    if 9_999_999 in dict.keys():
        count += 1
print(time.time() - start)

start = time.time()
count = 0
for _ in range(10_000_200):
    if dict.get(9_999_999) is not None:
        count += 1
print(time.time() - start)

start = time.time()
count = 0
for i in range(10_000_200):
    if i in dict.keys():
        count += 1
print(time.time() - start)

start = time.time()
count = 0
for i in range(10_000_200):
    if dict.get(i) is not None:
        count += 1
print(time.time() - start)

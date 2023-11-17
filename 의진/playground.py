import time
dict = {i: i for i in range(10_000_000)}
# 1
start = time.time()
count = 0
for i in range(10_000_000):
    if i in list(dict.keys()):
        count += 1
print(time.time() - start)

# 2
start = time.time()
count = 0
for i in range(10_000_000):
    if dict.get(i) is not None:
        count += 1
print(time.time() - start)

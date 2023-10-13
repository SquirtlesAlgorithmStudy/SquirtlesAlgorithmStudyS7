import time


def sorting_rule(x):
    return (x[1], x[0])


start_time = time.time()

a = [(i**2, ((-1)**i)-i) for i in range(1000000)]
a.sort(key=lambda x: (x[1], x[0]))
# a.sort(key=sorting_rule)

end_time = time.time()
elapse_time = end_time - start_time
print(elapse_time)

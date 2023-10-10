import time
import copy

start_time = time.time()
a = "뉴진쓰"
b = a
a = b.replace("뉴", "유")
print(a)
print(b)
finish_time = time.time()

elapse_time = finish_time - start_time
print(elapse_time)

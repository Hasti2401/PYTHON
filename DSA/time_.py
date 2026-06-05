import time

start = time.time()

for i in range(10):
    print(i)

end = time.time()

print(end - start)

"""
timeit - 0.0033978000001297914

time - 0.000308990478515625

"""
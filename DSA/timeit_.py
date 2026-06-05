import timeit

code = """for i in range(10):
            print(i)
    
    """

t = timeit.timeit(code,number=1)
print(t)

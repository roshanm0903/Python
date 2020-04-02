def create_cubes(n):
    for i in range(n):
        yield i**3     # yield keyword instead of return. values generated arent stored 


# for x in create_cubes(10):
#     print(x)


def simple_gen(x):
    for x in range(x):
        yield x

# for num in simple_gen(3):
#     print(num)

# g= simple_gen()
# next(g)


s ="hello"
s_iter = iter(s)  # convert iterable objects like string to a generator so that next function can be used
next(s_iter)

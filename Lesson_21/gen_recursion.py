def func_gen(items):
    if len(items) == 0:
        yield []
    else:
        pi = items[:]
        for i in range(len(pi)):
            pi[0], pi[i] = pi[i], pi[0]
            for p in func_gen(pi[1:]):
                yield [pi[0]] + p


for p in func_gen([1, 2, 3]):
    print(p)

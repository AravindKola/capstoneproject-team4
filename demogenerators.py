def demo():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'

d=demo()
print(next(d))
print(next(d))
print(next(d))


num=(d*d for d in range(10000))
print(num)
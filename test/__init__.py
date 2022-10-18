def mean1(x):
    import statistics
    return statistics.mean(x)

def mean2(x):
    s = sum(x)
    d = len(x)
    return s / d

def mean3(x):
    s = 0
    for i in x:
        s += i
    return s / len(x)


from combat import analyze
import random

t = [random.random() for x in range(30)]
print(analyze(mean1, t))
print(analyze(mean2, t))
print(analyze(mean3, t))

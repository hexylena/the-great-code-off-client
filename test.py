import tgco
def mean1(x):
    import statistics
    return statistics.mean(x)

print(tgco.submit(mean1, [1,2,3,4,5]))

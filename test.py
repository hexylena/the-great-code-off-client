import tcgo
def mean1(x):
    import statistics
    return statistics.mean(x)

print(tcgo.submit(mean1, [1,2,3,4,5]))

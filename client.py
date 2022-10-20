from radon.visitors import ComplexityVisitor
import time
import ast
import dis
import inspect
import statistics
import random


def execution_time(func, *args, **kwargs):
    times = []
    for i in range(10):
        t0 = time.perf_counter_ns()
        func(*args, **kwargs)
        t1 = time.perf_counter_ns()
        times.append(t1 - t0)
    return statistics.mean(times)


def complexity_bytecode(func):
    return len(list(dis.get_instructions(func)))


def complexity_cyclomatic(func):
    v = ComplexityVisitor.from_code(inspect.getsource(func))
    return v.functions[0].complexity


def analyze(func, *args, **kwargs):
    print(
        execution_time(func, *args, **kwargs),
        complexity_bytecode(func) * 0.5 * complexity_cyclomatic(func),
    )


def mean1(x):
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


t = [random.random() for x in range(30)]
analyze(mean1, t)
analyze(mean2, t)
analyze(mean3, t)

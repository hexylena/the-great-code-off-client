from radon.visitors import ComplexityVisitor
from memory_profiler import memory_usage
import os
import requests
import time
import dis
import inspect
import statistics


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


def memory(func, *args, **kwargs):
    return max(memory_usage((func, args, kwargs)))

def analyze(func, *args, **kwargs):
    t = execution_time(func, *args, **kwargs)
    c = complexity_bytecode(func) * 0.5 * complexity_cyclomatic(func),
    m = memory(func, *args, **kwargs)
    return t, c, m

def submit(func, *args, **kwargs):
    t, c, m = analyze(func, *args, **kwargs)

    payload = {
        'user': os.environ['USER'],
        'name': func.__name__,
        'time': t,
        'complexity': c,
        'memory': m,
    }

    resp = requests.post(
        "https://cocalc.atgm.avans.nl/the-great-code-off/",
        # "http://localhost:9091/the-great-code-off/",
        data=payload
    )
    return resp.content.decode('utf-8')

def bake(func, *args, **kwargs):
    contents = submit(func, *args, **kwargs)
    from IPython.core.display import HTML
    HTML(contents)

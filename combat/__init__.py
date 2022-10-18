from radon.visitors import ComplexityVisitor
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


def analyze(func, *args, **kwargs):
    t = execution_time(func, *args, **kwargs)
    c = complexity_bytecode(func) * 0.5 * complexity_cyclomatic(func),
    return t, c

def submit(func, *args, **kwargs):
    t, c = analyze(func, *args, **kwargs)

    payload = {
        'user': os.environ['USER'],
        'name': func.__name__,
        'time': t,
        'complexity': c,
    }

    resp = requests.post(
        "https://cocalc.atgm.avans.nl/code-combat-server/",
        # "http://localhost:9091/code-combat-server/",
        data=payload
    )
    return resp.content

def fight(func, *args, **kwargs):
    contents = submit(func, *args, **kwargs)
    from IPython.display import display_html
    display_html(contents)

import time


def timer(func, *args):
    startTime = time.perf_counter_ns()
    func(*args)
    return time.perf_counter_ns() - startTime

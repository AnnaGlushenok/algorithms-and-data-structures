import time


def timer(func, *args):
    startTime = time.perf_counter_ns()
    func(*args)
    return (time.perf_counter_ns() - startTime) / 1e9


def combine_comparators(*comparators):
    def combined_comparator(a, b):
        for i in range(len(comparators)):
            rightCompare = comparators[i](a, b)
            reversedCompare = comparators[i](b, a)
            if rightCompare or reversedCompare:
                return rightCompare
        return True

    return combined_comparator

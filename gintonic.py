import time


def timer(func, *args):
    startTime = time.perf_counter_ns()
    func(*args)
    return (time.perf_counter_ns() - startTime) / 1e9


class MemoResult:
    def __init__(self, args, value):
        self.args = args
        self.value = value

    def compare(self, args):
        if len(self.args) != len(args):
            return False

        length = len(self.args)
        for i in range(length):
            if type(args[i]) is not type(self.args[i]):
                return False

        for i in range(length):
            if isinstance(args[i], list):
                for j in range(len(self.args[i])):
                    if args[i][j] != self.args[i][j]:
                        return False

            elif isinstance(args[i], int):
                if args[i] != self.args[i]:
                    return False

        return True


def use_memo(func):
    results = []

    def memoized(*args):
        for result in results:
            if result.compare(args):
                return result.value

        value = func(*args)
        results.append(MemoResult(args, value))
        return value

    return memoized

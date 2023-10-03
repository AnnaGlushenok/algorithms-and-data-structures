import random
import string
import time

import numpy as np

import matplotlib.pyplot as plt
from Object import Object
from gintonic import timer

array = []

MAX_SIZE = 10000
xs = np.linspace(10, MAX_SIZE, 20)


def search(arr, el, comparator):
    for i in range(len(arr)):
        if comparator(arr[i], el):
            return i

    return -1


def binary_search(arr, start, end, searching_val, comparator):
    if end <= start:
        return -1

    middle = int((end + start) / 2)
    if comparator(arr[middle], searching_val):
        return middle
    elif comparator(arr[middle], searching_val):
        return binary_search(arr, 0, middle - 1, searching_val, comparator)

    elif comparator(arr[middle], searching_val):
        return binary_search(arr, middle + 1, end, searching_val, comparator)

    return searching_val


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def min_sort(arr, comparator):
    for i in range(len(arr) - 1):
        print(i)
        min_index = i
        for j in range(i + 1, len(arr)):
            if comparator(arr[j], arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


random.seed(1)
for _ in range(0, MAX_SIZE):
    array.append(Object(random.randint(-100000, 100000), random_word(10), time.perf_counter_ns()))


def draw(figure, title, xs, *yss):
    plt.figure(figure)
    plt.title(title)
    for ys in yss:
        plt.plot(xs, ys)
    plt.grid()


resultD = [[], []]

for i in range(2, len(MAX_SIZE.__str__())):
    x = 10 ** (i + 1) - 1
    y = timer(search, array[0:x], array[5000], (lambda a, b: a.int > b.int))
    resultD[0].append(x)
    resultD[1].append(y)

draw(1, "Линейный поиск", resultD[0], resultD[1])

resultA = [[], []]
min_sort(array, (lambda a, b: a.int > b.int))
for i in range(2, len(MAX_SIZE.__str__())):
    x = 10 ** (i + 1) - 1
    y = timer(binary_search, array[0:x], 0, x, array[5000], (lambda a, b: a.int > b.int))
    resultA[0].append(x)
    resultA[1].append(y)

draw(2, "Бинарный поиск", resultA[0], resultA[1])

plt.show()

import time
import string
import random
from Object import Object
from gintonic import timer, combine_comparators
import matplotlib.pyplot as plt
import numpy as np

comparator_int = lambda a, b: a.int > b.int
comparator_string = lambda a, b: a.string > b.string
comparator_time = lambda a, b: a.time > b.time

comparator_time_and_string = combine_comparators(comparator_time, comparator_string)
comparator_time_and_int = combine_comparators(comparator_time, comparator_int)
comparator_string_and_int = combine_comparators(comparator_string, comparator_int)

comparator_all = combine_comparators(comparator_string, comparator_int, comparator_time)


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def min_sort(arr, comparator):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if comparator(arr[j], arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def min_sort_with_check(arr, comparator):
    for i in range(len(arr) - 1):
        if is_sorted(arr, comparator):
            return
        min_index = i
        for j in range(i + 1, len(arr)):
            if comparator(arr[j], arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


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


def min_sort_rev(arr, comparator):
    for i in range(len(arr) - 1, -1, -1):
        min_index = i
        for j in range(i - 1, -1, -1):
            if not comparator(arr[j], arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def max_sort(arr, comparator):
    for i in range(len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if comparator(arr[j], arr[max_index]):
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


def max_sort_rev(arr, comparator):
    for i in range(len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if not comparator(arr[j], arr[max_index]):
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


def max_sort_with_check(arr, comparator):
    for i in range(len(arr) - 1):
        max_index = i
        if is_sorted(arr, comparator):
            return
        for j in range(i + 1, len(arr)):
            if comparator(arr[j], arr[max_index]):
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


def is_sorted(arr, comparator):
    for i in range(len(arr) - 1):
        if comparator(arr[i], arr[i + 1]):
            return False
    return True


def search(arr, el, comparator):
    for i in range(len(arr)):
        if comparator(arr[i], el):
            return i

    return -1


def draw(figure, title, xs, *yss):
    plt.figure(figure)
    plt.title(title)
    for ys in yss:
        plt.plot(xs, ys)
    plt.grid()


array = []
res_int = [[], []]
res_string = [[], []]
res_time = [[], []]
res_with_check = []
res_search = []

res_string_int = [[], []]
res_time_int = [[], []]
res_time_string = [[], []]

res_all = [[], []]

MAX_SIZE = 100
xs = np.linspace(10, MAX_SIZE, 20)
for i in xs:
    for _ in range(0, int(i)):
        array.append(Object(random.randint(-20, 20), random_word(10), time.perf_counter_ns()))
    print(i, " элементов")
    res_int[0].append(timer(min_sort, array.copy(), comparator_int))
    res_string[0].append(timer(min_sort, array.copy(), comparator_string))
    res_time[0].append(timer(min_sort, array.copy(), comparator_time))

    res_string_int[0].append(timer(min_sort, array.copy(), comparator_string_and_int))
    res_time_int[0].append(timer(min_sort, array.copy(), comparator_time_and_int))
    res_time_string[0].append(timer(min_sort, array.copy(), comparator_time_and_string))

    res_all[0].append(timer(min_sort, array.copy(), comparator_all))

    res_int[1].append(timer(min_sort_rev, array.copy(), comparator_int))
    res_string[1].append(timer(min_sort_rev, array.copy(), comparator_string))
    res_time[1].append(timer(min_sort_rev, array.copy(), comparator_time))

    res_string_int[1].append(timer(min_sort_rev, array.copy(), comparator_string_and_int))
    res_time_int[1].append(timer(min_sort_rev, array.copy(), comparator_time_and_int))
    res_time_string[1].append(timer(min_sort_rev, array.copy(), comparator_time_and_string))

    res_all[1].append(timer(min_sort, array.copy(), comparator_all))

    print("Количество сравнений: ", sum(range(2, len(array))))
    print("Количество перестановок: ", len(array) - 1)

    res_with_check.append(timer(min_sort_with_check, array, comparator_int))

    res_search.append(timer(binary_search, array, 0, len(array), Object(0, "", 0), comparator_int))

draw(1, "Сортировка по возрастанию с 1 ключом", xs, res_int[0], res_string[0], res_time[0])
draw(2, "Сортировка по убыванию с 1 ключом", xs, res_int[1], res_string[1], res_time[1])
draw(3, "Сортировка по возрастанию с 2 ключами", xs, res_string_int[0], res_time_int[0], res_time_string[0])
draw(4, "Сортировка по убыванию с 2 ключами", xs, res_string_int[1], res_time_int[1], res_time_string[1])
draw(5, "Сортировка с проверкой", xs, res_with_check)
draw(6, "Линейный поиск", xs, res_search)
draw(7, "Сортировка по возрастанию с 3 ключами", xs, res_all[0])
draw(8, "Сортировка по убыванию с 3 ключами", xs, res_all[1])
array = []
res_int = [[], []]
res_string = [[], []]
res_time = [[], []]
res_with_check = []
res_search = []

res_string_int = [[], []]
res_time_int = [[], []]
res_time_string = [[], []]

res_all = [[], []]
for i in xs:
    for _ in range(0, int(i)):
        array.append(Object(random.randint(-20, 20), random_word(10), time.perf_counter_ns()))
    print(i, " элементов")
    res_int[0].append(timer(max_sort, array.copy(), comparator_int))
    res_string[0].append(timer(max_sort, array.copy(), comparator_string))
    res_time[0].append(timer(max_sort, array.copy(), comparator_time))

    res_string_int[0].append(timer(max_sort, array.copy(), comparator_string_and_int))
    res_time_int[0].append(timer(max_sort, array.copy(), comparator_time_and_int))
    res_time_string[0].append(timer(max_sort, array.copy(), comparator_time_and_string))

    res_all[0].append(timer(max_sort, array.copy(), comparator_all))

    res_int[1].append(timer(max_sort_rev, array.copy(), comparator_int))
    res_string[1].append(timer(max_sort_rev, array.copy(), comparator_string))
    res_time[1].append(timer(max_sort_rev, array.copy(), comparator_time))

    res_string_int[1].append(timer(max_sort_rev, array.copy(), comparator_string_and_int))
    res_time_int[1].append(timer(max_sort_rev, array.copy(), comparator_time_and_int))
    res_time_string[1].append(timer(max_sort_rev, array.copy(), comparator_time_and_string))

    res_all[1].append(timer(max_sort, array.copy(), comparator_all))

    print("Количество сравнений: ", sum(range(2, len(array))))
    print("Количество перестановок: ", len(array) - 1)

    res_with_check.append(timer(max_sort_with_check, array, comparator_int))

    res_search.append(timer(search, array, Object(0, "", 0), comparator_int))

draw(1, "Сортировка по возрастанию с 1 ключом", xs, res_int[0], res_string[0], res_time[0])
draw(2, "Сортировка по убыванию с 1 ключом", xs, res_int[1], res_string[1], res_time[1])
draw(3, "Сортировка по возрастанию с 2 ключами", xs, res_string_int[0], res_time_int[0], res_time_string[0])
draw(4, "Сортировка по убыванию с 2 ключами", xs, res_string_int[1], res_time_int[1], res_time_string[1])
draw(5, "Сортировка с проверкой", xs, res_with_check)
draw(6, "Бинарный поиск", xs, res_search)
draw(7, "Сортировка по возрастанию с 3 ключами", xs, res_all[0])
draw(8, "Сортировка по убыванию с 3 ключами", xs, res_all[1])
plt.show()

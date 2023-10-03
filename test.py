from Object import Object
from gintonic import timer, combine_comparators
from main import min_sort

arr = [
    Object(1, "ба", 1),
    Object(1, "аб", 2),
    Object(2, "аб", 3),
    Object(3, "ав", 4),
    Object(2, "ав", 5)
]

comparator_int = lambda a, b: a.int > b.int
comparator_string = lambda a, b: a.string > b.string

comparator_int_and_string = combine_comparators(comparator_int, comparator_string)


def display(arr):
    for el in arr:
        print(el.to_string())


display(arr)
print("------------------")
min_sort(arr, comparator_int_and_string)
display(arr)

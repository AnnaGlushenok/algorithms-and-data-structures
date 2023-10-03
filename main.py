import time

from List import List
import random
import matplotlib.pyplot as plt
from Array import Array
from gintonic import timer


def paint(figure, title, arr, count):
    plt.figure(figure)
    plt.title(title)
    plt.plot([i for i in range(count)], arr[0])
    plt.plot([i for i in range(count)], arr[1])
    plt.grid()
    plt.show()


list1 = List(1)
list2 = List(1)

arr1 = Array()
arr2 = Array()
arr1.append(1)
arr2.append(1)

addInListTime = [[], []]
addInArrTime = [[], []]
COUNT = 1000
for i in range(COUNT):
    num = random.randint(-20, 20)
    addInListTime[0].append(timer(list1.add, num))
    addInListTime[1].append(timer(list2.add, num))
    addInArrTime[0].append(timer(arr1.append, num))
    addInArrTime[1].append(timer(arr2.append, num))

index = list1.findMinValueIndex()
print("Время поиска минимального элемента: ", timer(list1.findMinValueIndex))
print("Индекс: ", index)
print("Время удаления после минимального индекса: ", timer(list1.removeAfter, index))
index = list1.findFirstZeroIndex()
print("Время поиска нулевого элемента: ", timer(list1.findFirstZeroIndex))
print("Индекс: ", index)

index = list2.findMaxValueIndex()
print("Время поиска максимального элемента: ", timer(list2.findMaxValueIndex))
print("Индекс: ", index)
print("Время удаления до максимального индекса: ", timer(list2.removeBefore, index))

print("Время сортировки 1 списка: ", timer(list1.sort))
print("Время сортировки 2 списка: ", timer(list2.sort))

print("---------------------- Массивы ----------------------")
minIndex = arr1.findMinValueIndex()
maxIndex = arr2.findMaxValueIndex()
print("Время поиска минимального элемента: ", timer(arr1.findMinValueIndex))
print("Индекс: ", minIndex)
print("Время поиска максимального элемента: ", timer(arr2.findMaxValueIndex))
print("Индекс: ", maxIndex)
index = arr1.findFirstZeroIndex()
print("Время копирования до индекса: ", timer(arr1.copy, 0, index - 1))
print("Время копирования после индекса: ", timer(arr1.copy, index + 1, list1.len))

startTime = time.perf_counter_ns()
for i in range(minIndex + 1, arr1.size):
    arr1.delete(i)
startTime = time.perf_counter_ns() - startTime
print("Время удаления после минимального индекса: ", startTime)

startTime = time.perf_counter_ns()
for i in range(maxIndex - 1, -1, -1):
    arr2.delete(i)
startTime = time.perf_counter_ns() - startTime
print("Время удаления до максимального индекса: ", startTime)

paint(1, "Добавление в лист", addInListTime, COUNT)
paint(2, "Добавление в массив", addInArrTime, COUNT)

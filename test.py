from gintonic import timer
from List import List
import random

list = List(0)


random.seed(1)
for i in range(100000):
    list.add(random.randint(-20, 20))

for _ in range(10):
    time = timer(list.findMinValueIndex)
    print(time)



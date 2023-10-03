class Array:
    arr = []
    size = 0

    def __init__(self):
        arr = []

    def append(self, el):
        arr = [None] * (self.size + 1)
        for i in range(self.size):
            arr[i] = self.arr[i]

        arr[self.size] = el
        self.arr = arr
        self.size += 1

    def delete(self, index):
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        del self.arr[self.size - 1]
        self.size -= 1

    def findMinValueIndex(self):
        minValue = self.arr[0]
        index = 0
        for i in range(self.size):
            if self.arr[i] < minValue:
                minValue = self.arr[i]
                index = i
        return index

    def findMaxValueIndex(self):
        maxValue = self.arr[0]
        index = 0
        for i in range(self.size):
            if self.arr[i] > maxValue:
                maxValue = self.arr[i]
                index = i
        return index

    def findFirstZeroIndex(self):
        index = 0
        for i in range(self.size):
            if self.arr[i] == 0:
                index = i
        return index

    def copy(self, start, end):
        len = (end - start)
        arr = [None] * len
        for i in range(len):
            arr[i] = self.arr[i + start]

        return arr

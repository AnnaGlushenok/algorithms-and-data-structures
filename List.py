from Node import Node


class List:
    startNode = None
    lastNode = None
    len = 1

    def __init__(self, value):
        self.startNode = Node(value)
        self.lastNode = self.startNode

    def add(self, value):
        el = Node(value)
        if self.lastNode is not None:
            self.lastNode.next = el
        else:
            self.startNode = el
        self.lastNode = el
        self.len += 1

    def delete(self, index):
        if index >= self.len:
            raise Exception("Wrong index")

        node = self.startNode
        while index > 1:
            node = node.next
            index -= 1

        if index == 0:
            if self.lastNode == self.startNode:
                self.lastNode = None

            self.startNode = node.next
        elif node.next.next is None:
            node.next = None
            self.lastNode = node
        else:
            node.next = node.next.next
        self.len -= 1

    def findFirstZeroIndex(self):
        node = self.startNode
        index = 0
        while node is not None:
            if node.value == 0:
                return index
            index += 1
            node = node.next
        return -1

    def copy(self, start, end):
        list = List()
        node = self.startNode

        for i in range(start):
            node = node.next

        for i in range(end - start + 1):
            list.add(node.value)
            node = node.next

        return list

    def findMinValueIndex(self):
        node = self.startNode
        index = 0
        min = self.startNode.value
        minIndex = 0
        while node is not None:
            if node.value < min:
                min = node.value
                minIndex = index
            index += 1
            node = node.next

        return minIndex

    def findMaxValueIndex(self):
        node = self.startNode
        index = 0
        max = 0
        maxIndex = 0
        while node is not None:
            if node.value > max:
                max = node.value
                maxIndex = index
            index += 1
            node = node.next
        return maxIndex

    def removeBefore(self, index):
        if index >= self.len:
            raise Exception("Bad index")

        self.len -= index
        node = self.startNode

        if index == 0:
            return

        while index > 1:
            index -= 1
            node = node.next

        self.startNode = node.next
        node.next = None

    def removeAfter(self, index):
        if index >= self.len:
            raise Exception("Bad index")

        self.len -= self.len - index + 1
        node = self.startNode
        while index != 0:
            index -= 1
            node = node.next

        self.lastNode = node
        node.next = None

    def sort(self):
        i = 0
        while i < self.len:
            j = 0
            maxNode = self.startNode
            jNode = self.startNode
            while j < (self.len - i):
                if maxNode.value < jNode.value:
                    maxNode = jNode
                j += 1
                jNode = jNode.next

            k = 0
            endNode = self.startNode
            while k < (self.len - i - 1):
                endNode = endNode.next
                k += 1
            self.swap(maxNode, endNode)
            i += 1

    def swap(self, first, second):
        if first is second:
            pass

        prev1, node1 = self.getNodes(first)
        prev2, node2 = self.getNodes(second)

        if prev1 is not None:
            prev1.next = node2
        else:
            self.startNode = node2

        if prev2 is not None:
            prev2.next = node1
        else:
            self.startNode = node1
        tempNode = node1.next
        node1.next = node2.next
        node2.next = tempNode

    def getNodes(self, el):
        if self.startNode == el:
            return None, self.startNode

        prev = self.startNode
        node = self.startNode.next

        while node is not el:
            prev = node
            node = node.next

        return prev, node

    def toList(self):
        collection = []
        node = self.startNode
        while node is not None:
            collection.append(node.value)
            node = node.next
        return collection

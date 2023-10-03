from collections import deque

from Node import Node


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._rec_add(value, self.root)

    def _rec_add(self, value, node):
        if node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._rec_add(value, node.right)
        else:
            if node.left is None:
                node.left = Node(value)
            else:
                self._rec_add(value, node.left)

    def bfs(self):
        queue = deque()
        queue.append((self.root, 0))
        prev_rank = 0
        while queue:
            node, rank = queue.popleft()

            if prev_rank != rank:
                print()
            print(node.value, " ", end="")

            if node.left is not None:
                queue.append((node.left, rank + 1))
            if node.right is not None:
                queue.append((node.right, rank + 1))

            prev_rank = rank

    def dfs(self):
        self._dfs(self.root)

    def _dfs(self, node):
        if node is None:
            return

        if node.left is not None:
            self._dfs(node.left)
        if node.right is not None:
            self._dfs(node.right)
        print(node.value)

    def count_right_nodes(self):
        if self.root is None:
            return 0
        return self._count_right_nodes(self.root.right)

    def _count_right_nodes(self, node):
        if node is None:
            return 0

        count = 0
        if node.right is not None:
            count += self._count_right_nodes(node.right)
        if node.left is not None:
            count += self._count_right_nodes(node.left)

        return count + (1 if node.right is not None or node.left is not None else 0)

    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, node):
        if node is None:
            return None

        if node.value == value:
            return node

        if node.value < value and node.right is not None:
            return self._find(value, node.right)
        elif node.value >= value and node.left is not None:
            return self._find(value, node.left)

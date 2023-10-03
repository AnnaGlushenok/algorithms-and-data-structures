from Tree import Tree

arr = [10, 5, 20, 3, 6, 15, 30, 11, 16, 25, 31, 17, 21, 27, 23]

tree = Tree()
for a in arr:
    tree.add(a)

tree.bfs()
# tree.dfs()
print()
print()

node = tree.find(15)
node1 = tree.find(27)
[node.value, node1.value] = [node1.value, node.value]
tree.bfs()

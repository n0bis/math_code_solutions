from binarytree import build

values = [5, 2, 11, 1, 4, 6, 12, 3, 8, 7, 10]
root = build(values)
root.pprint(index=True)
del root[0]
print(root)
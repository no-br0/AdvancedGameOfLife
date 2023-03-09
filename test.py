#from LifeManager import calc

#print(calc(3, -10,1))


#data = [0,1,2,3,4,5,6,7,8]

#print(7%3)
#for item in data:
#    col = (item%3)-1
#    row = (item//3)-1
#    print(f'Num: {item}')
#    print(f'Col: {col}')
#    print(f'Row: {row}')
#    print()


class Node:
    def __init__(self, nw, ne, sw, se):
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.level = nw.level + 1

    def compute_next(self):
        if self.level < 2:
            return self
        else:
            nw_n = self.nw.compute_next()
            ne_n = self.ne.compute_next()
            sw_n = self.sw.compute_next()
            se_n = self.se.compute_next()
            return Node(
                Node(nw_n.nw, nw_n.ne, nw_n.sw, ne_n.nw),
                Node(nw_n.ne, ne_n.nw, sw_n.ne, se_n.nw),
                Node(nw_n.sw, sw_n.ne, sw_n.sw, se_n.sw),
                Node(ne_n.sw, se_n.nw, se_n.sw, se_n.se)
            ).simplify()

    def simplify(self):
        if self.level < 2:
            return self
        else:
            nw_n = self.nw.simplify()
            ne_n = self.ne.simplify()
            sw_n = self.sw.simplify()
            se_n = self.se.simplify()
            if nw_n == ne_n and nw_n == sw_n and nw_n == se_n:
                return nw_n
            else:
                return Node(nw_n, ne_n, sw_n, se_n)

class Leaf:
    def __init__(self, value):
        self.value = value
        self.level = 0

    def compute_next(self):
        return self

    def simplify(self):
        return self

def make_leaf(value):
    if value == 0:
        return Leaf(0)
    else:
        return Leaf(1)

def make_tree(grid):
    if len(grid) == 1:
        return make_leaf(grid[0][0])
    else:
        half = len(grid) // 2
        nw = make_tree([row[:half] for row in grid[:half]])
        ne = make_tree([row[half:] for row in grid[:half]])
        sw = make_tree([row[:half] for row in grid[half:]])
        se = make_tree([row[half:] for row in grid[half:]])
        return Node(nw, ne, sw, se)

def print_tree(tree):
    if isinstance(tree, Leaf):
        print(f'Tree: {tree.value}')
    else:
        print_tree(tree.nw)
        print_tree(tree.ne)
        print_tree(tree.sw)
        print_tree(tree.se)

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

tree = make_tree(grid)
print(grid)
print_tree(tree)

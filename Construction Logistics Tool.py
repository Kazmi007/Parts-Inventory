
def calculate_price(part_list):
    rt = find_root(part_list)  # finds root node
    tr = make_tree(1, rt, part_list)  # constructs tree (root given a part count of 1 for simplification purposes)
    return calculate_price_helper(tr)


def calculate_price_helper(tr):  # calculates total price for the tree
    if len(tr) == 3 and isinstance(tr[2], float):  # checks if at terminal node
        return tr[0] * tr[2]
    total = 0
    for a in tr[2:]:
        total += calculate_price_helper(a)  # recursive call to add each child node's price to the total
    return tr[0] * total  # multiplies the total for one node by number of nodes and returns


def required_parts(part_list):
    rt = find_root(part_list)  # finds root
    tr = make_tree(1, rt, part_list)  # constructs tree (root given a part count of 1 for simplification purposes)
    return required_parts_helper(tr)


def required_parts_helper(tr):  # returns required basic parts for the tree
    if len(tr) == 3 and isinstance(tr[2], float):  # checks if at terminal node
        return tuple(tr[:2])
    temp = []
    result = []
    for a in tr[2:]:
        temp_var = required_parts_helper(a)  # temporary variable to hold the recursive result
        if isinstance(temp_var, list):  # checks if the previous call is returning from a terminal node or not
            temp += temp_var
        else:
            temp += [temp_var]
    for b in temp:
        parts = (tr[0] * b[0], b[1])  # edits the node's amount according to requirement of the parent node
        result += [parts]
    return result


def stock_check(part_list, stock_list):
    r_parts = required_parts(part_list)  # list of required parts
    result = []
    for n, part in r_parts:
        found = False
        for i, stock in stock_list:
            if part == stock:
                if i < n:
                    result += [(part, (n - i))]
                found = True
        if not found:  # if part not found in stock
            result += [(part, n)]
    return result


def make_tree(i, root, nodes):  # constructs a tree implemented as a nested list
    for a in nodes:
        if a[0] == root:
            if is_leaf(a):
                return [i, root, a[1]]  # returns just the terminal node if at terminal node
            else:
                tr = [i, root]
                for b in a[1:]:
                    tr += [make_tree(b[0], b[1], nodes)]  # recursive call to build the nested list
                return tr


def find_root(lst):  # finds the root node of a given list of nodes
    for a in lst:
        if not is_leaf(a):
            found = False
            node = a[0]
            for b in lst:  # loop to check if the node exists as a child node
                if not is_leaf(b):
                    for c in b[1:]:
                        if c[1] == node:
                            found = True
            if not found:  # if node not found as a child node
                rt = a[0]
                return rt
    return False  # returns False if no root found


def is_leaf(lst):  # checks if a given node is a terminal node (in its part_list representation)
    if len(lst) == 2 and isinstance(lst[1], float):
        return True
    return False

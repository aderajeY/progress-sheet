class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # We use union-find (or called disjoint-set) in this problem
        # the basic idea of union-find is to connect the components that share a same root
        # e.g. a == b, b == c, c == d, then a, b, c, d should be put together
        # we pick up a root for these connected components, this root could be a, b, c, or d , we actually don't care :)
        # we just want them be together!
        
        # initialize an array, where the root of each element is itself at the begining
        root = list(range(26))
        
        # find the root of x
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        # merge the connected components that x and y belong to respectively
        def union(x, y):
            root_x, root_y = find(x), find(y)
            root[root_x] = root_y
        
        # build the connected components with the equal equations
        for equation in equations:
            if equation[1] == '=':
                x, y = ord(equation[0])-ord('a'), ord(equation[3])-ord('a')
                # x and y should share a same root, so we use union here
                union(x, y)
        
        # traverse the unequal equations to obtain the final result
        for equation in equations:
            if equation[1] == '!':
                x, y = ord(equation[0])-ord('a'), ord(equation[3])-ord('a')
                # x, y should have different roots, so here we find their roots respectively
                if find(x) == find(y):
                    return False
        
        return True
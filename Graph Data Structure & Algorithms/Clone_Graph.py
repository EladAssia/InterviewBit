Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

########################################################################################################################################

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        d = {}
        if not node:
            return node
        new_node = UndirectedGraphNode(node.label)
        d[node] = new_node
        lst = [node]
        
        while lst:
            tmp = lst.pop(0)
            for ii in tmp.neighbors:
                if ii not in d:
                    d[ii] = UndirectedGraphNode(ii.label)
                    lst.append(ii)
                d[tmp].neighbors.append(d[ii])

        return new_node

########################################################################################################################################

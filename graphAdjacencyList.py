import collections

class Graph:
    def __init__(self, nodes, graph_list=collections.defaultdict(list), is_directed = False):
        self.nodes = nodes
        self.graph_list = graph_list
        self.is_directed = is_directed
        
    def add_nodes(self):
        for u,v in self.nodes:
            self.graph_list[u].append(v)
            
            # This will be implemented if not directed.
            if not self.is_directed:
                self.graph_list[v].append(u)
        
    def print_graph(self):
        for i in self.graph_list:
            print(str(i)+'------->'+ str(self.graph_list[i]))
        
if __name__ == '__main__':
    
    L = [(1,2), (3,4), (1,3), (4,5), (4,2)]
    # If we want directed graph: is_directed=True
    gp = Graph(L, is_directed=False)
    gp.add_nodes()
    gp.print_graph()

"""
Kruskal's algorithm implementation
"""
import networkx as nx

class DisjointSet:
    """
    Disjoin set class;
    """
    def __init__(self, graph: nx.Graph)-> None:
        self.parents={node: node for node in graph.nodes}
    def find(self, u):
        """
        Recursively finds node's parent
        """
        if self.parents[u]==u:
            return u
        return self.find(self.parents[u])
    def union(self, u, v):
        """
        Unites 2 different nodes
        """
        if self.find(u)!=self.find(v):
            self.parents[self.find(u)]=v

def kruskal(graph: nx.Graph)-> nx.Graph | None:
    """
    Finds a MST for the graph using Kruskal's algorithm.
    Returns none if graph is disconnected
    """
    if not nx.is_connected(graph):
        return None
    graph_set=DisjointSet(graph)
    result_graph=nx.Graph()
    edges=sorted([(u,v,w['weight']) for u,v,w in graph.edges(data=True)],key=lambda x:x[2])
    while len(result_graph.edges)<len(graph.nodes)-1:
        curr_edge=edges.pop(0)
        if graph_set.find(curr_edge[0])!=graph_set.find(curr_edge[1]):
            result_graph.add_edge(curr_edge[0],curr_edge[1],weight=curr_edge[2])
            graph_set.union(curr_edge[0],curr_edge[1])
    return result_graph

if __name__=='__main__':
    import graph as gr
    from networkx.algorithms import tree
    while 1:
        G = gr.gnp_random_connected_graph(6,50,False)
        mstp = tree.minimum_spanning_tree(G, algorithm="kruskal")
        mstp_kruskal = kruskal(G)
        print(mstp.edges,'\n',mstp_kruskal.edges)
        edge_weights = nx.get_edge_attributes(mstp, 'weight')
        edge_weights_prim = nx.get_edge_attributes(mstp_kruskal, 'weight')
        print(sum(edge_weights.values()),sum(edge_weights_prim.values()))
        if sum(edge_weights.values())!=sum(edge_weights_prim.values()):
            gr.draw(mstp_kruskal)
            break
        gr.draw(mstp_kruskal)

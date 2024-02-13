"""
Prim's algorithm implementation
"""
import networkx as nx

def prim(graph,start=0):
    """
    Prim's MST algorithm
    """
    if not nx.is_connected(graph):
        return None
    visited=set()
    res_graph=nx.Graph()
    edges=sorted([(u,v,w['weight']) for u,v,w in graph.edges(data=True)],key=lambda x:x[2])
    visited.add(start)
    while len(visited)!=len(graph.nodes):
        for u,v,w in edges:
            if (u in visited and v not in visited) or (v in visited and u not in visited):
                res_graph.add_edge(u,v,weight=w)
                visited.add(v)
                visited.add(u)
    return res_graph

if __name__=='__main__':
    import matplotlib.pyplot as plt
    import graph as gr
    from networkx.algorithms import tree
    G = gr.gnp_random_connected_graph(10,50,False)
    mstp = tree.minimum_spanning_tree(G, algorithm="prim")
    mstp_prim = prim(G)
    print(mstp.edges,'\n',mstp_prim.edges)
    edge_weights = nx.get_edge_attributes(mstp, 'weight')
    edge_weights_prim = nx.get_edge_attributes(mstp_prim, 'weight')
    print(sum(edge_weights.values()),sum(edge_weights_prim.values()))

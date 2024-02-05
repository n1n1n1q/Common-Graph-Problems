"""
Prim's algorithm implementation
"""
import networkx as nx

def prim(graph: nx.Graph) -> nx.Graph or None:
    """
    Finds a MST for given graph.
    Returns none if graph is disconnected
    """
    if not nx.is_connected(graph):
        return None
    result_graph=nx.Graph()
    result_graph.add_node(0)
    while set(result_graph.nodes)!=set(graph.nodes):  
        min_edge=min(((u,v,weight['weight']) for u,v,weight in graph.edges(data=True) \
            if (u in result_graph.nodes and v not in result_graph.nodes) or\
                  (u not in result_graph.nodes and v in result_graph.nodes)),\
                    key=lambda x:x[2])
        result_graph.add_edge(min_edge[0],min_edge[1],weight=min_edge[2])
    return result_graph


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

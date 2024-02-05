"""
Graph generator
"""
import random
from itertools import combinations, groupby
import networkx as nx
import matplotlib.pyplot as plt

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               directed: bool = False):
    """
    Generates a random graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted (in case of undirected graphs)
    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    edges = combinations(range(num_of_nodes), 2)
    G.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        if random.random() < 0.5:
            random_edge = random_edge[::-1]
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(-5, 20)
    return G

def draw(graph: nx.Graph | nx.DiGraph):
    """
    Draws the given graphh
    """
    plt.figure(figsize=(10,6))
    pos = nx.arf_layout(graph)
    nx.draw(graph,pos, node_color='lightblue',
            with_labels=True,
            node_size=500,
            arrowsize=20,
            arrows=True)
    labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx_edge_labels(graph, pos,edge_labels=labels)
    plt.show()

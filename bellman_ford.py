"""
Bellman Ford shortest path algorithm implementation
"""
import networkx as nx
def bellman_ford(graph: nx.Graph):
    """
    Finds shortest path with Bellman Ford algorithm
    """
    distance=[float('inf') for _ in range(len(graph.nodes))]
    predecessor=[float('inf') for _ in range(len(graph.nodes))]
    visited=[False for _ in range(len(graph.nodes))]
    distance[0]=0
    for _ in range(len(graph.nodes)-1):
        for u,v,w in graph.edges(data=True):
            if distance[u]+w['weight']<distance[v]:
                distance[v]=distance[u]+w['weight']
                predecessor[v]=u
    for u,v,w in graph.edges(data=True):
        if distance[u]+w['weight']<distance[v]:
            predecessor[v]=u
            visited[v]=True
            while not visited[u]:
                visited[u]=True
                u=predecessor[u]
            cycle=[u]
            v=predecessor[u]
            while v!=u:
                cycle.append(v)
                v=predecessor[v]
            raise ValueError(f'Negative cycle detected, {cycle}')
    return distance

if __name__=='__main__':
    import graph as gr
    G=gr.gnp_random_connected_graph(5, 100, True)
    print(bellman_ford(G))
    from networkx.algorithms import bellman_ford_predecessor_and_distance
    try:
        pred, dist = bellman_ford_predecessor_and_distance(G, 0)
        for k, v in dist.items():
            print(f"Distance to {k}:", v)
    except:
        print("Negative cycle detected")

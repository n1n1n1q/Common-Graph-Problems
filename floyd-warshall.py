"""
Floyd-warshall algorithm implementation
"""
import networkx as nx

def floyd_warshall(graph: nx.Graph):
    """
    Finds shortest path between all the pairs of nodes
    """
    distance=[[float('inf') if i!=j else 0 for j in range(len(graph.nodes))]\
             for i in range(len(graph.nodes))]
    for u,v,w in graph.edges(data=True):
        distance[u][v]=w['weight']
    for k in range(len(graph.nodes)):
        for i in range(len(graph.nodes)):
            for j in range(len(graph.nodes)):
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]
    return distance

if __name__=='__main__':
    import graph as gr
    from networkx.algorithms import floyd_warshall_predecessor_and_distance
    G=gr.gnp_random_connected_graph(5, 100, True)
    print(floyd_warshall(G))
    try:
        pred, dist = floyd_warshall_predecessor_and_distance(G) 
        for k, v in dist.items():
            print(f"Distances with {k} source:", dict(v))
    except:
        print("Negative cycle detected")

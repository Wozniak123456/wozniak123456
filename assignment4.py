
#=======================================
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

def create_random_network(N, p):
    G = nx.Graph()
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < p:
                G.add_edge(i, j)
    return G

def create_ring_network(N):
    G = nx.cycle_graph(N)
    return G

def create_small_world_network(N, p=0.2):
    G = nx.watts_strogatz_graph(N, k=4, p=p)
    return G

def draw_circular_graph(G, title):
    pos = nx.circular_layout(G)
    plt.title(title)
    nx.draw(G, pos, with_labels=True)
    plt.show()
if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "-ring_network":
        N = int(sys.argv[2])
        ring_network = create_ring_network(N)
        draw_circular_graph(ring_network, f"Ring Network(range 1) (Nodes={N})")
    elif len(sys.argv) == 3 and sys.argv[1] == "-small_world":
        N = 10  # 默认大小
        small_world_network = create_small_world_network(N)
        draw_circular_graph(small_world_network, f"Small Worlds Network (Nodes={N})")
    elif len(sys.argv) == 5 and sys.argv[1] == "-small_world" and sys.argv[3] == "-re_wire":
        N = int(sys.argv[2])
        p = float(sys.argv[4])
        small_world_network = create_small_world_network(N, p)
        draw_circular_graph(small_world_network, f"Small Worlds Network (Nodes={N}, re-wire prob={p})")
    elif len(sys.argv) == 4 and sys.argv[1] == "-random_network":
        N = int(sys.argv[2])
        p = float(sys.argv[3])
        random_network = create_random_network(N, p)
        draw_circular_graph(random_network, f"Random Network (Nodes={N}, re-wire prob={p})")
    else:
        print("Usage:")
        print("For ring network: python3 assignment.py -ring_network <N>")
        print("For default small world network: python3 assignment.py -small_world <N>")
        print("For custom small world network with re-wiring probability: python3 assignment.py -small_world <N> -re_wire <probability>")
        print("For random network: python3 assignment.py -random_network <N> <p>")
#TEST
# python assignment.py -ring_network 10
# python assignment.py -small_world 10
# python assignment.py -small_world 10 -re_wire 0.98
# python assignment.py -random_network 10 0.5
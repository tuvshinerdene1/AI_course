import ast
import networkx as nx
import matplotlib.pyplot as plt

# 1. Load your data
with open('Mongolian_map.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()
    graph_data = ast.literal_eval(file_content)

# 2. Create a NetworkX Graph object
# nx.Graph is undirected by default
G = nx.Graph()

# 3. Add nodes and edges from your dictionary
G.add_nodes_from(graph_data['nodes'])

# We can pass the edges directly from your 'edges' list 
# because it's already in the format (node1, node2, {'weight': value})
G.add_edges_from(graph_data['edges'])

# 4. Set up the visual layout
plt.figure(figsize=(12, 8))
# 'spring_layout' calculates positions so nodes don't overlap too much
pos = nx.spring_layout(G, seed=42, k=2) 

# 5. Draw the components
# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

# Draw edges (lines)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='gray')

# Draw labels (City Names)
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Draw edge weights (The distances)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# 6. Show the plot
plt.title("Mongolian Cities Connectivity Graph (TSP)")
plt.axis('off') # Hide the x/y axis
plt.tight_layout()
plt.show()
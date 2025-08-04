import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add nodes (stations)
stations = ["Hyde Park Corner", "Green Park", "Piccadilly Circus", "Leicester Square", "Covent Garden", "Holborn"]
G.add_nodes_from(stations)

# Add edges with estimated distances (km)
edges = [
    ("Hyde Park Corner", "Green Park", 1.2),  # Estimated distance
    ("Green Park", "Piccadilly Circus", 0.8),
    ("Piccadilly Circus", "Leicester Square", 0.5),
    ("Leicester Square", "Covent Garden", 0.4),
    ("Covent Garden", "Holborn", 0.6)
]
G.add_weighted_edges_from(edges)

# Draw graph
pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='blue')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Add key
plt.text(1.1, 0.9, "Key", transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1.1, 0.85, "____ Piccadilly", transform=plt.gca().transAxes, fontsize=10)

# Display and save graph
plt.title("Piccadilly Line Segment")
plt.axis('off')
plt.savefig("piccadilly_line_task1.png")  # Save image
plt.show()
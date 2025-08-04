import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add nodes (stations) for 4 lines
stations = {
    "Piccadilly": ["Hyde Park Corner", "Green Park", "Piccadilly Circus", "Leicester Square", "Covent Garden", "Holborn"],
    "Central": ["Oxford Circus", "Bond Street", "Marble Arch", "Lancaster Gate", "Queensway", "Notting Hill Gate"],
    "Northern": ["Camden Town", "Euston", "King's Cross St. Pancras", "Angel", "Old Street", "Moorgate"],
    "Jubilee": ["Waterloo", "Westminster", "Green Park", "Bond Street", "Baker Street", "St. John's Wood"]
}
all_stations = [station for line in stations.values() for station in line]
G.add_nodes_from(all_stations)

# Add edges with estimated distances (km) - including interchange stations
edges = [
    # Piccadilly Line
    ("Hyde Park Corner", "Green Park", 1.2), ("Green Park", "Piccadilly Circus", 0.8),
    ("Piccadilly Circus", "Leicester Square", 0.5), ("Leicester Square", "Covent Garden", 0.4),
    ("Covent Garden", "Holborn", 0.6),
    # Central Line
    ("Oxford Circus", "Bond Street", 0.9), ("Bond Street", "Marble Arch", 1.0),
    ("Marble Arch", "Lancaster Gate", 1.2), ("Lancaster Gate", "Queensway", 0.7),
    ("Queensway", "Notting Hill Gate", 0.8),
    # Northern Line
    ("Camden Town", "Euston", 1.5), ("Euston", "King's Cross St. Pancras", 1.0),
    ("King's Cross St. Pancras", "Angel", 0.9), ("Angel", "Old Street", 0.8),
    ("Old Street", "Moorgate", 0.7),
    # Jubilee Line
    ("Waterloo", "Westminster", 1.3), ("Westminster", "Green Park", 0.9),
    ("Green Park", "Bond Street", 1.1), ("Bond Street", "Baker Street", 1.0),
    ("Baker Street", "St. John's Wood", 1.2),
    # Interchange connections
    ("Green Park", "Oxford Circus", 0.6), ("Bond Street", "Oxford Circus", 0.5),
    ("Green Park", "Westminster", 0.9), ("Bond Street", "Baker Street", 0.4)
]
G.add_weighted_edges_from(edges)

# Assign colors to each line
colors = {
    "Piccadilly": "blue",
    "Central": "red",
    "Northern": "black",
    "Jubilee": "grey"
}
edge_colors = [colors["Piccadilly"] if e[0] in stations["Piccadilly"] and e[1] in stations["Piccadilly"] else
               colors["Central"] if e[0] in stations["Central"] and e[1] in stations["Central"] else
               colors["Northern"] if e[0] in stations["Northern"] and e[1] in stations["Northern"] else
               colors["Jubilee"] for e in G.edges()]

# Draw graph
pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color=edge_colors)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Add key
plt.text(1.1, 0.9, "Key", transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))
plt.text(1.1, 0.85, "____ Piccadilly", transform=plt.gca().transAxes, fontsize=10, color='blue')
plt.text(1.1, 0.80, "____ Central", transform=plt.gca().transAxes, fontsize=10, color='red')
plt.text(1.1, 0.75, "____ Northern", transform=plt.gca().transAxes, fontsize=10, color='black')
plt.text(1.1, 0.70, "____ Jubilee", transform=plt.gca().transAxes, fontsize=10, color='grey')

# Display and save graph
plt.title("London Transport Network Segment")
plt.axis('off')
plt.savefig("london_transport_task2.png")  # Save image
plt.show()
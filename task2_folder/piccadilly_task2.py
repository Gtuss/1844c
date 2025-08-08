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
    ("Green Park", "Westminster", 0.9), ("Bond Street", "Baker Street", 0.4),
    ("King's Cross St. Pancras", "Holborn", 1.5),  # Nối Northern với Piccadilly
    ("Waterloo", "Oxford Circus", 1.8)  # Nối Jubilee với Central
]
G.add_weighted_edges_from(edges)

# Kiểm tra số lượng thành phần liên thông
components = list(nx.connected_components(G))
print(f"Số lượng thành phần liên thông: {len(components)}")
print("Các thành phần liên thông:")
for i, component in enumerate(components, 1):
    print(f"Thành phần {i}: {component}")

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

# Layout for visualization with real coordinates
pos = {
    "Hyde Park Corner": (51.5027, -0.1527),
    "Green Park": (51.5067, -0.1428),
    "Piccadilly Circus": (51.5098, -0.1342),
    "Leicester Square": (51.5113, -0.1281),
    "Covent Garden": (51.5129, -0.1243),
    "Holborn": (51.5174, -0.1200),
    "Oxford Circus": (51.5151, -0.1415),
    "Bond Street": (51.5142, -0.1494),
    "Marble Arch": (51.5136, -0.1586),
    "Lancaster Gate": (51.5119, -0.1756),
    "Queensway": (51.5104, -0.1872),
    "Notting Hill Gate": (51.5091, -0.1962),
    "Camden Town": (51.5392, -0.1426),
    "Euston": (51.5282, -0.1337),
    "King's Cross St. Pancras": (51.5308, -0.1238),
    "Angel": (51.5322, -0.1058),
    "Old Street": (51.5263, -0.0873),
    "Moorgate": (51.5186, -0.0881),
    "Waterloo": (51.5036, -0.1133),
    "Westminster": (51.5010, -0.1250),
    "Baker Street": (51.5226, -0.1571),
    "St. John's Wood": (51.5304, -0.1743)
}

# Draw graph
node_colors = ['red' if G.degree(node) == 1 else 'lightblue' for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_weight='bold', edge_color=edge_colors)
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

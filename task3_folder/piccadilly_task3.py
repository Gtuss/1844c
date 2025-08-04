import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Create graph (copied from Task 2)
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

# Add edges with estimated distances (km)
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

# Calculate metrics
total_length = sum(nx.get_edge_attributes(G, 'weight').values())
distances = list(nx.get_edge_attributes(G, 'weight').values())
average_distance = np.mean(distances)
std_deviation = np.std(distances)

# Print results
print(f"Total network length: {total_length:.2f} km")
print(f"Average distance between stations: {average_distance:.2f} km")
print(f"Standard deviation of distances: {std_deviation:.2f} km")

# Create bar chart for visualization
metrics = ['Total Length', 'Average Distance', 'Standard Deviation']
values = [total_length, average_distance, std_deviation]

plt.bar(metrics, values, color=['blue', 'green', 'red'])
plt.title("Network Analysis Results")
plt.ylabel("Distance (km)")
plt.ylim(0, max(values) + 1)  # Set y-axis limit for clarity
for i, v in enumerate(values):
    plt.text(i, v + 0.1, f"{v:.2f}", ha='center')

# Save and display chart
plt.savefig("task3_results.png")  # Save image
plt.show()
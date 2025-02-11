# Define the dataset as a list of points
points = {
    "A1": (2, 10), "A2": (2, 5), "A3": (8, 4),
    "B1": (5, 8), "B2": (7, 5), "B3": (6, 4),
    "C1": (1, 2), "C2": (4, 9)}

# Initial cluster centers
centroids = {
    "Cluster1": points["A1"],
    "Cluster2": points["B1"],
    "Cluster3": points["C1"]}

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return round(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5, 2)

# Function to assign points to the nearest cluster
def assign_clusters():
    clusters = {"Cluster1": [], "Cluster2": [], "Cluster3": []}
    distance_table = []
    for label, point in points.items():
        distances = {cluster: euclidean_distance(point, centroid) for cluster, centroid in centroids.items()}
        nearest_cluster = min(distances, key=distances.get)
        clusters[nearest_cluster].append(label)
        distance_table.append([label, point[0], point[1], distances["Cluster1"], distances["Cluster2"], distances["Cluster3"], nearest_cluster])
    return clusters, distance_table

# Function to update centroids
def update_centroids(clusters):
    new_centroids = {}
    for cluster, members in clusters.items():
        if members:
            avg_x = round(sum(points[m][0] for m in members) / len(members), 2)
            avg_y = round(sum(points[m][1] for m in members) / len(members), 2)
            new_centroids[cluster] = (avg_x, avg_y)
        else:
            new_centroids[cluster] = centroids[cluster]
    return new_centroids

# Perform K-Means Clustering with manual iterations
iterations = 5
for i in range(iterations):
    print(f"\nIteration {i+1}:")
    clusters, distance_table = assign_clusters()
    print("Data Points | X  | Y  | Dist to A1 | Dist to B2 | Dist to C3 | Assigned Cluster")
    print("-" * 75)
    for row in distance_table:
        print(f"{row[0]:<12} | {row[1]:<2} | {row[2]:<2} | {row[3]:<10.2f} | {row[4]:<10.2f} | {row[5]:<10.2f} | {row[6]}")

    new_centroids = update_centroids(clusters)
    print("\nNew Centroids:")
    for cluster, centroid in new_centroids.items():
        print(f"{cluster}: {centroid}")

    if new_centroids == centroids:
        break  # Stop if centroids do not change
    centroids = new_centroids

# Output the final clusters and centroids
print("\nFinal Cluster Assignments:")
for cluster, members in clusters.items():
    print(f"{cluster}: {members}")

print("\nFinal Centroids:")
for cluster, centroid in centroids.items():
    print(f"{cluster}: {centroid}")
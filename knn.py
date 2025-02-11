#Example from the lesson
dataset = [
    {"brightness": 40, "saturation": 20, "class": "Red"},
    {"brightness": 50, "saturation": 50, "class": "Blue"},
    {"brightness": 60, "saturation": 90, "class": "Blue"},
    {"brightness": 10, "saturation": 25, "class": "Red"},
    {"brightness": 70, "saturation": 70, "class": "Blue"},
    {"brightness": 60, "saturation": 10, "class": "Red"},
    {"brightness": 25, "saturation": 80, "class": "Blue"},]

# Predict the class of this new point
new_point = {"brightness": 20, "saturation": 35}

# Function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Compute distances from the new point to each point in the dataset
distances = []
for entry in dataset:
    dist = euclidean_distance(new_point["brightness"], new_point["saturation"], entry["brightness"], entry["saturation"])
    distances.append((dist, entry["class"]))

# Sort distances in ascending order
distances.sort()

# Set k value
k = 5

# Get the k nearest neighbors
k_nearest = distances[:k]

# Count class occurrences
class_counts = {}
for _, class_label in k_nearest:
    if class_label in class_counts:
        class_counts[class_label] += 1
    else:
        class_counts[class_label] = 1

# Determine the predicted class
predicted_class = max(class_counts, key=class_counts.get)

# Output the result
print(f"The predicted class for the new point {new_point} is: {predicted_class}")
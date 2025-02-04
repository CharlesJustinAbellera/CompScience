class NaiveBayesClassifier:
    def __init__(self):
        self.class_priors = {}  # Stores P(y)
        self.feature_probs = {}  # Stores P(x_i | y)

    def fit(self, X, y):
        n_samples = len(y)
        unique_classes = list(set(y))

        # Compute class priors P(y)
        for label in unique_classes:
            self.class_priors[label] = sum(1 for c in y if c == label) / n_samples

        # Compute likelihoods P(x_i | y)
        self.feature_probs = {label: {} for label in unique_classes}

        for label in unique_classes:
            total_count = sum(1 for c in y if c == label)
            feature_counts = {}

            for i in range(len(X[0])):  # Loop through each feature index
                feature_counts[i] = {}

            for xi, yi in zip(X, y):
                if yi == label:
                    for i, feature in enumerate(xi):
                        if feature not in feature_counts[i]:
                            feature_counts[i][feature] = 0
                        feature_counts[i][feature] += 1

            for i in feature_counts:
                self.feature_probs[label][i] = {}
                for feature, count in feature_counts[i].items():
                    self.feature_probs[label][i][feature] = count / total_count

    def predict(self, X):
        predictions = []
        for x in X:
            class_scores = {}
            for label in self.class_priors:
                likelihood = self.class_priors[label]  # Start with P(y)
                for i, feature in enumerate(x):
                    if feature in self.feature_probs[label][i]:
                        likelihood *= self.feature_probs[label][i][feature]
                    else:
                        likelihood *= 1e-6  # Small probability to avoid zero division

                class_scores[label] = likelihood

            # Choose the class with the highest probability
            predictions.append(max(class_scores, key=class_scores.get))
        return predictions
    
if __name__ == "__main__":
    # Example dataset from Quiz 1
    X_train = [['Red', 'Sports', 'Domestic'],
               ['Red', 'Sports', 'Domestic'],
               ['Red', 'Sports', 'Domestic'],
               ['Yellow', 'Sports', 'Domestic'],
               ['Yellow', 'Sports', 'Domestic'],
               ['Yellow', 'SUV', 'Imported'],
               ['Yellow', 'SUV', 'Imported'],
               ['Yellow', 'SUV', 'Imported'],
               ['Red', 'SUV', 'Imported'],
               ['Red', 'Sports', 'Imported']]
    
    y_train = ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']

    model = NaiveBayesClassifier()
    model.fit(X_train, y_train)

    Test1 = [['Red', 'SUV', 'Domestic']]
    print("Test 1\nRed, SUV, Domestic")
    print("Is it Stolen?: ", model.predict(Test1))

    print("\nTest 2\nYellow, SUV, Domestic")
    Test2 = [['Yellow', 'SUV', 'Domestic']]
    print("Is it Stolen?: ", model.predict(Test2))
import numpy as np
import matplotlib.pyplot as plt

def calculate_regression(x, y):
    n = len(x)
    #Calculate thr sum of x, y, xy, and x^2
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)

    # Formula to calculate slope(m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    # Formula to calculate intercept (b)
    b = (sum_y - m * sum_x) / n

    return m, b

# Function to plot the regression model
def plot_regression(x, y, m, b):
    
    plt.figure(figsize=(8, 6))
    
    # Scatter plot for data points
    plt.scatter(x, y, color='blue', label='Data points')
    
    # Regression line
    reg_line = m * x + b
    plt.plot(x, reg_line, color='red', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')

    # Add labels, title, and legend
    plt.title('Linear Regression', fontsize=14)
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(alpha=0.5)
    plt.show()

# Sample Data
x = np.array([140, 155, 159, 179, 192, 200, 212])
y = np.array([60, 62, 67, 70, 71, 72, 75])

# Perform regression calculations
m, b = calculate_regression(x, y)

# Print results
print("Slope (m):", m)
print("Intercept (b):", b)
print(f"Regression Line: y = {m:.2f}x + {b:.2f}")

# Plot the data and regression line
plot_regression(x, y, m, b)
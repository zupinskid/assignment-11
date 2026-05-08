"""
File: system_usage.py

Generates synthetic CPU usage data for an eight‑hour shift, computes
basic statistics using the provided stats module, and renders a line
chart of the usage over time.  The resulting graph is saved as a
PNG file in the current directory.  You can adjust the data
generation logic or choose a different chart type as needed.

This script demonstrates how to combine simple data analysis with
visualization using matplotlib, as discussed in Chapter 11.
"""

import random
import matplotlib.pyplot as plt
from stats import mean, median, std, mode
import os

# Generate eight hours of CPU usage data (integers between 20 and 95)
cpu_usage = [random.randint(20, 95) for _ in range(8)]

# Compute basic statistics using functions from stats.py
avg_usage = mean(cpu_usage)
median_usage = median(cpu_usage)
std_dev_usage = std(cpu_usage)
mode_usage = mode(cpu_usage)

# Print the statistics to the console
print(f"CPU usage data: {cpu_usage}")
print(f"Mean CPU usage: {avg_usage:.2f}%")
print(f"Median CPU usage: {median_usage:.2f}%")
print(f"Standard deviation: {std_dev_usage:.2f}%")
print(f"Mode CPU usage: {mode_usage}%")

# Create a line chart
plt.figure(figsize=(8, 4))
hours = list(range(1, len(cpu_usage) + 1))
plt.plot(hours, cpu_usage, marker='o', linestyle='-', color='blue')
plt.title('CPU Usage Over 8‑Hour Shift')
plt.xlabel('Hour')
plt.ylabel('CPU Usage (%)')
plt.grid(True)
plt.xticks(hours)

# Save the figure in the same directory as this script
script_dir = os.path.dirname(__file__)
output_file = os.path.join(script_dir, 'system_usage_line.png')
plt.savefig(output_file)
print(f"Line chart saved as {output_file}")

# Optionally display the plot when running interactively
# plt.show()

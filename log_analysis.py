"""
File: log_analysis.py

Reads a server log CSV file containing API response times, cleans the data
by replacing missing entries with the mean of their columns, computes the
mean response time per service, and visualizes the distribution of
averages using a pie chart.  The resulting chart is saved as a PNG
file in the current directory.  Pandas is used for data handling and
matplotlib for plotting, following the guidelines in Chapter 11.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Determine the path to the CSV file relative to this script
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'server_log.csv')

# Read the CSV while ignoring comment lines
df = pd.read_csv(csv_path, comment='#')

# Convert numeric columns to floats for mean calculation
numeric_cols = df.columns[1:]  # skip the timestamp column
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Fill missing values with column means
for col in numeric_cols:
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)

# Compute mean response times for each service
mean_response_times = df[numeric_cols].mean()

# Print the means to the console
print("Mean response times (ms):")
print(mean_response_times)

# Plot and save the distribution of mean response times
plt.figure(figsize=(6, 6))
plt.pie(mean_response_times, labels=mean_response_times.index, autopct='%1.1f%%', startangle=140)
plt.title('Average Response Time by Service')
plt.axis('equal')  # Ensure pie is drawn as a circle

# Save the plot in the same directory as this script
output_file = os.path.join(script_dir, 'server_log_response_time_pie.png')
plt.savefig(output_file)
print(f"Pie chart saved as {output_file}")

# Optionally display the plot when running interactively
# plt.show()

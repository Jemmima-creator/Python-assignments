# Week 7 Assignment
# Author: Jemmimah Mwithalii
# Objective:
#   - Load and analyze a dataset using pandas
#   - Perform some basic analysis
#   - Visualize the data with matplotlib (and seaborn for styling)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

# For this assignment, I chose the classic Iris dataset.
# I am loading it directly from sklearn so that I don’t need an external CSV file.
iris = load_iris(as_frame=True)
df = iris.frame

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nChecking for missing values:")
print(df.isnull().sum())

# The dataset does not have missing values, but if it had,
# I would either drop them or fill them appropriately.
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

print("\nDescriptive statistics:")
print(df.describe())

# Grouping by the target column (species) and computing mean of numerical columns
grouped = df.groupby("target").mean(numeric_only=True)
print("\nMean values grouped by species:")
print(grouped)

# -------------------------------
# Task 3: Data Visualization
# -------------------------------
sns.set(style="whitegrid")  # make plots look nicer

# 1. Line chart (cumulative sum of sepal length)
plt.figure(figsize=(8, 5))
df["sepal length (cm)"].cumsum().plot()
plt.title("Cumulative Sepal Length over Entries")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8, 5))
df.groupby("target")["petal length (cm)"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Petal Length by Species")
plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
plt.ylabel("Petal Length (mean)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=20, color="orange", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8, 5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], 
            c=df["target"], cmap="viridis", alpha=0.7)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

# -------------------------------
# Observations
# -------------------------------
print("\n--- Observations ---")
print("1. The dataset has no missing values.")
print("2. The descriptive statistics show the range and spread of the flower measurements.")
print("3. Grouping by species reveals differences in average petal and sepal sizes.")
print("4. The scatter plot shows a clear positive correlation between sepal length and petal length.")

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

# Count ratings
rating_counts = df["Rating"].value_counts()

# Plot bar chart
plt.figure(figsize=(8,5))
rating_counts.plot(kind='bar')

plt.title("Books Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")

plt.show()
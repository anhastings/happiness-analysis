import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/world_happiness_2019.csv")

# Top 10 happiest countries
top10 = df.sort_values(by="Score", ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.barh(top10['Country or region'], top10['Score'], color='skyblue')
plt.xlabel("Happiness Score")
plt.title("Top 10 Happiest Countries in 2019")
plt.gca().invert_yaxis()

# Save plot as PNG
plt.savefig("reports/top10_happiest.png", bbox_inches='tight')
plt.show()


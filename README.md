# World Happiness Analysis (2019)

This project analyzes the World Happiness Report dataset to explore patterns and insights related to happiness scores across countries.

## Project Goals
- Analyze key factors influencing happiness scores
- Perform data cleaning and exploratory data analysis (EDA)
- Create visualizations to communicate insights

## Tools & Technologies
- Python
- Pandas
- Matplotlib & Seaborn
- Jupyter Notebook

## Dataset
- **World Happiness Report (2019)**
- CSV format, includes country, region, happiness score, and key factors

## Key Insights (example)
- Higher GDP per capita and social support are strongly correlated with higher happiness scores
- Generosity and healthy life expectancy also show positive trends

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/anhastings/happiness-analysis.git

## Example Plot

This simple example shows the top 10 happiest countries in 2019:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/world_happiness_2019.csv")

# Top 10 happiest countries
top10 = df.sort_values(by="Score", ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.barh(top10['Country'], top10['Score'], color='skyblue')
plt.xlabel("Happiness Score")
plt.title("Top 10 Happiest Countries in 2019")
plt.gca().invert_yaxis()
plt.show()


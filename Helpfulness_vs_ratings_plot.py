import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the output
ratings = []
avg_helpfulness = []

# Always fix encoding issue
with open('helpfulness_rating.txt', 'r', encoding='utf-8') as file:
    for line in file:
        rating, helpfulness = line.strip().split('\t')
        rating = float(rating.replace('"', ''))
        helpfulness = float(helpfulness)
        ratings.append(rating)
        avg_helpfulness.append(helpfulness)

# Sort values
sorted_indices = np.argsort(ratings)
ratings = np.array(ratings)[sorted_indices]
avg_helpfulness = np.array(avg_helpfulness)[sorted_indices]

# Set a nice Seaborn theme
sns.set_theme(style="whitegrid")

# Create a color palette
palette = sns.color_palette("coolwarm", len(ratings))

# Create figure
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x=ratings, y=avg_helpfulness, palette=palette)

# Add trendline
#z = np.polyfit(ratings, avg_helpfulness, 1)
#p = np.poly1d(z)
#plt.plot(ratings, p(ratings), "r--", label='Trendline', linewidth=2)

# Customize plot
plt.title('⭐ Average Helpfulness Score vs Star Rating ⭐', fontsize=18, weight='bold')
plt.xlabel('Star Rating', fontsize=14)
plt.ylabel('Average Helpfulness Score', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.tight_layout()

# Save and show
plt.savefig('beautiful_helpfulness_vs_star_rating.png', dpi=300)
plt.show()

print("Beautiful plot saved as 'beautiful_helpfulness_vs_star_rating.png'!")

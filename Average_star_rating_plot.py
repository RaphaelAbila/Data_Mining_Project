import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('averagescores.txt', sep='\t', header=None, names=['Title', 'AvgRating'], encoding='utf-8')

df['Title'] = df['Title'].str.replace('"', '')

df = df.sort_values(by='AvgRating', ascending=False)

top_n = 50
top_df = df.head(top_n)

plt.figure(figsize=(12, 8))
bars = plt.barh(top_df['Title'], top_df['AvgRating'], color='mediumseagreen')
plt.xlabel('Average Rating', fontsize=12)
plt.ylabel('Book Title', fontsize=12)
plt.title(f'Total Average Rating Per Product', fontsize=14)
plt.xlim(0, 5)
plt.gca().invert_yaxis()

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.05, bar.get_y() + bar.get_height() / 2, f"{width:.2f}", ha='left', va='center', fontsize=9)

plt.tight_layout()
plt.savefig("average_ratings_horizontal.png")
plt.show()

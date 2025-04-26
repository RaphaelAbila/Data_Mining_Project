import matplotlib.pyplot as plt

def get_first_4_words(title):
    return ' '.join(title.split()[:4])

product_data = []
with open("topreviews.txt", "r") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            try:
                title = parts[0].strip('"') 
                count = int(parts[1])
                product_data.append((title, count))
            except Exception:
                pass

# Sort by count just in case
product_data.sort(key=lambda x: x[1], reverse=True)

# Get titles and counts
titles = [get_first_4_words(item[0]) for item in product_data]
counts = [item[1] for item in product_data]

# Plot
plt.figure(figsize=(12, 8))
bars = plt.barh(titles, counts, color='skyblue')
plt.xlabel("Number of Reviews", fontsize=12)
plt.ylabel("Product Title", fontsize=12)
plt.title("Top 10 Products by Review Count", fontsize=14)
plt.gca().invert_yaxis()

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, str(width), va='center')

plt.tight_layout()
plt.savefig("top_10_product_reviews.png")
plt.show()

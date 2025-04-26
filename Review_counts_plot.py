import matplotlib.pyplot as plt

def get_first_4_words(title):
    """Extract first 4 words from a string"""
    return ' '.join(title.split()[:4])

# Read MRJob output
product_data = []
with open("reviewcounts.txt", "r") as f:
    for line in f:
        # Split into key (product_id) and value (title, count)
        parts = line.strip().split("\t")
        if len(parts) == 2:
            product_id = parts[0]
            title, count = eval(parts[1])  # Convert string to tuple
            product_data.append((title, count))

# Sort by review count (descending)
product_data.sort(key=lambda x: x[1], reverse=True)

# Extract top N products for plotting (adjust N as needed)
N = 35  # Show top 15 products
top_products = product_data[:N]
titles = [get_first_4_words(item[0]) for item in top_products]  # Modified this line
counts = [item[1] for item in top_products]

# Plotting
plt.figure(figsize=(12, 8))
bars = plt.barh(titles, counts, color='skyblue')
plt.xlabel("Number of Reviews", fontsize=12)
plt.ylabel("Product Title", fontsize=12)  # Updated label
plt.title(f"Total review count per product for {N} Products", fontsize=14)
plt.gca().invert_yaxis()  # Highest reviews at the top

# Add count labels on bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f"{int(width)}", ha='left', va='center')

plt.tight_layout()
plt.savefig("product_reviews.png")  # Save plot as PNG
plt.show()
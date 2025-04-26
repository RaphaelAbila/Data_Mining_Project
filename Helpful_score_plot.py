import matplotlib.pyplot as plt

# Data
ratings = [1.0, 2.0, 3.0, 4.0, 5.0]
helpfulness = [0.523, 0.736, 0.730, 0.835, 0.839]

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(ratings, helpfulness, color=['#ff6b6b', '#ffa502', '#feca57', '#2ecc71', '#1dd1a1'])

# Customize
plt.title("Average Helpfulness Score by Star Rating", fontsize=14)
plt.xlabel("Star Rating", fontsize=12)
plt.ylabel("Helpfulness Score (0-1)", fontsize=12)
plt.ylim(0, 1)
plt.xticks(ratings)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f"{height:.3f}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("helpfulness_bar.png", dpi=300)
plt.show()
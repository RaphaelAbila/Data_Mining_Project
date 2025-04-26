# plot_frequent_words.py
import matplotlib.pyplot as plt
from collections import defaultdict

# Read the output file
def read_frequent_words(filename):
    data = defaultdict(list)

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue
            key, count = parts
            key = eval(key)  # e.g., ("positive", "great")
            category, word = key
            count = int(count)
            data[category].append((word, count))
    
    return data

# Plot function
def plot_words(word_counts, category, top_n=10):
    # Sort and get top N words
    top_words = sorted(word_counts, key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*top_words)

    plt.figure(figsize=(10,6))
    plt.bar(words, counts, color='skyblue')
    plt.title(f'Top {top_n} Frequent Words - {category.capitalize()} Reviews')
    plt.xticks(rotation=45)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig("frequentwords.png")
    plt.show()

if __name__ == "__main__":
    data = read_frequent_words('frequent_words.txt')

    for category in ['overall', 'positive', 'negative']:
        if category in data:
            plot_words(data[category], category)

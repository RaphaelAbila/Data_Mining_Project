import matplotlib.pyplot as plt

# Read data from sentiment_analysis.txt
labels = []
counts = []

with open('sentiment_analysis.txt', 'r', encoding='utf-8') as file:
    for line in file:
        sentiment, count = line.strip().split('\t')  # split by tab
        sentiment = sentiment.strip('"')  # remove the double quotes
        labels.append(sentiment)
        counts.append(int(count))

# Create a bar chart
plt.bar(labels, counts, color=['red', 'gray', 'green'])

# Add title and labels
plt.title('Sentiment Analysis of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

plt.savefig("visualize_sentiment.png")
plt.show()

import matplotlib.pyplot as plt
import os

# Path to your TXT file
file_path = r'time_rating.txt'

months = []
ratings = []

# Read the raw file in binary, strip out any NULL bytes, then decode
with open(file_path, 'rb') as f:
    raw = f.read().replace(b'\x00', b'')
    text = raw.decode('utf-8', errors='ignore')

# Parse each non-empty line
for line in text.splitlines():
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    # Remove surrounding quotes from month, convert rating to float
    month = parts[0].strip().strip('"')
    try:
        rating = float(parts[1])
    except ValueError:
        continue
    months.append(month)
    ratings.append(rating)

# Ensure output directory exists
os.makedirs(r'visuals', exist_ok=True)

# Generate a distinct color for each bar
cmap = plt.get_cmap('tab20')            # pick a colormap
colors = [cmap(i) for i in range(len(months))]

# Plot bar chart with different colors
plt.figure()
plt.bar(months, ratings, color=colors)
plt.xlabel('Month')
plt.ylabel('Average Rating')
plt.title('Average Rating by Month')
plt.tight_layout()

# Save to file and display
plt.savefig(r'monthly_ratings_bar_colored.png')
plt.show()

# frequent_word_analysis.py
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import string

# Basic stopwords list
STOPWORDS = set([
    'the', 'and', 'is', 'in', 'to', 'of', 'for', 'it', 'this', 'that', 'a', 'an', 'on', 'was', 'with', 'as', 'at', 'by', 'from', 'but', 'be', 'are'
])

WORD_RE = re.compile(r"\b\w+\b")

class WordFrequency(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words)
        ]

    def mapper_get_words(self, _, line):
        try:
            # Expect CSV format: Book_Title, Review_Text, Rating
            parts = line.strip().split(',')
            if len(parts) < 3:
                return
            review_text = parts[1]
            rating = float(parts[2])

            # Normalize text
            review_text = review_text.lower()
            review_text = review_text.translate(str.maketrans('', '', string.punctuation))
            words = WORD_RE.findall(review_text)

            for word in words:
                if word not in STOPWORDS and len(word) > 2:
                    if rating >= 4:
                        yield ("positive", word), 1
                    elif rating <= 2:
                        yield ("negative", word), 1
                    yield ("overall", word), 1
        except Exception as e:
            pass  # Skip bad lines

    def reducer_count_words(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    WordFrequency.run()

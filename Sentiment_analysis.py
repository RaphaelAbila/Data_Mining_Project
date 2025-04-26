from mrjob.job import MRJob
import csv
from textblob import TextBlob

class SentimentAnalysis(MRJob):

    def parse_csv(self, line):
        reader = csv.reader([line])
        return next(reader)

    def mapper(self, _, line):
        try:
            fields = self.parse_csv(line)
            if len(fields) > 9:
                review_text = fields[9]
                sentiment = TextBlob(review_text).sentiment.polarity
                sentiment_label = 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'
                yield (sentiment_label, 1)
                # yield (sentiment_label, review_text)
        except:
            pass

    def reducer(self, key, values):
        yield (key, sum(values))
        # yield (key, list(values))

if __name__ == "__main__":
    SentimentAnalysis.run()

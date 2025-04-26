from mrjob.job import MRJob
import csv

class HelpfulnessAnalysis(MRJob):

    def parse_csv(self, line):
        reader = csv.reader([line])
        return next(reader)

    def mapper(self, _, line):
        try:
            fields = self.parse_csv(line)
            if len(fields) > 6:
                helpful_votes, total_votes = fields[5].split('/')  # Extract votes
                helpful_votes, total_votes = int(helpful_votes), int(total_votes)
                rating = float(fields[6])  # Extract star rating

                if total_votes > 0:  # Avoid division by zero
                    helpfulness_score = helpful_votes / total_votes
                    yield (rating, (helpfulness_score, 1))
        except:
            pass

    def reducer(self, key, values):
        total_helpfulness, count = 0, 0
        for score, num in values:
            total_helpfulness += score
            count += num
        yield (key, total_helpfulness / count if count > 0 else 0)

if __name__ == "__main__":
    HelpfulnessAnalysis.run()

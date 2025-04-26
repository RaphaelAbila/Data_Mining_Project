from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
import calendar

class MonthBasedAnalysis(MRJob):

    def steps(self):
        return [
            # Step 1: compute (month_num → avg_rating)
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),

            # Step 2: collect all (month_num, avg) pairs into ONE reducer
            #         and emit them sorted by month_num, but with names
            MRStep(mapper=self.pass_through,
                   reducer=self.sort_reducer),
        ]

    def parse_csv(self, line):
        reader = csv.reader([line])
        return next(reader)

    def mapper(self, _, line):
        try:
            fields    = self.parse_csv(line)
            timestamp = fields[10]
            rating    = float(fields[6])
            month_str = timestamp.strip().split('/')[0]

            if month_str.isdigit():
                yield int(month_str), (rating, 1)
        except:
            pass  # skip malformed lines

    def reducer(self, month, values):
        total, count = 0, 0
        for rating, num in values:
            total += rating
            count += num
        avg = total / count if count else 0
        yield month, avg

    def pass_through(self, month, avg):
        # send everything to a single reducer
        yield None, (month, avg)

    def sort_reducer(self, _, month_avg_pairs):
        # sort by numeric month, then swap to name
        for month, avg in sorted(month_avg_pairs, key=lambda x: x[0]):
            month_name = calendar.month_abbr[month]  # Jan, Feb, Mar, ...
            yield month_name, avg

if __name__ == "__main__":
    MonthBasedAnalysis.run()

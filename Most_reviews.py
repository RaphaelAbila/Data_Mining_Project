from mrjob.job import MRJob
from mrjob.step import MRStep
class ReviewCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.top_10_reducer)
        ]
    def mapper(self, _, line):
        try:
            fields = line.strip().split(',')
            product_id = fields[0]
            title = fields[1]
            if product_id.lower() != "product_id" and title:
                yield product_id, (title, 1)
        except Exception:
            pass
    def reducer(self, product_id, values):
        title = None
        total_count = 0
        for val in values:
            title = val[0]
            total_count += val[1]
        if title:
            yield None, (total_count, title)
    def top_10_reducer(self, _, values):
        top_10 = sorted(values, reverse=True, key=lambda x: x[0])[:10]
        for count, title in top_10:
            yield title, count

if __name__ == '__main__':
    ReviewCount.run()

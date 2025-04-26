from mrjob.job import MRJob

class ReviewCount(MRJob):
    def mapper(self, _, line):
        # Skip header lines
        if not (line.startswith("product_id") or line.startswith("Id")):
            parts = line.strip().split(',')
            if len(parts) > 1:
                product_id = parts[0].strip()
                product_title = parts[1].strip().strip('"')
                # Emit composite key (product_id, product_title) with count 1
                yield (product_id, product_title), 1

    def reducer(self, product_key, counts):
        product_id, product_title = product_key
        total_reviews = sum(counts)
        # Emit product_id as key, and a tuple of (product_title, count) as value
        yield product_id, (product_title, total_reviews)

if __name__ == '__main__':
    ReviewCount.run()
from mrjob.job import MRJob

class MRAverageRatingByTitle(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        if len(fields) > 6 and fields[6].replace('.', '', 1).isdigit(): 
            title = fields[1].strip()  
            rating = float(fields[6])  
            yield title, (rating, 1)

    def reducer(self, title, values):
        total_rating = 0
        count = 0
        for rating, num in values:
            total_rating += rating
            count += num
        average_rating = total_rating / count if count > 0 else 0
        yield title, average_rating

if __name__ == "__main__":
    MRAverageRatingByTitle.run()
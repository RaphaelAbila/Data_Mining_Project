Data Mining Project

Amazon Reviews Sentiment Analysis using MapReduce
=====================================================

Step 1: Environment Setup and Data Loading
------------------------------------------
To set up the environment, first install the required libraries listed in requirements.txt using the following command within your virtual environment:

pip install -r requirements.txt


Step 2: Run source code files
---------------------------

# TASK 2: Review counts
1. python Review_counts.py Books_rating_new.csv 
2. python Review_counts.py Books_rating_new.csv > reviewcounts.txt
3. python Review_counts_plot.py

# TASK 3: Average star rating
1. python Average_star_rating.py Books_rating_new.csv
2. python Average_star_rating.py Books_rating_new.csv > averagescores.txt
3. python Average_star_rating_plot.py

# TASK 4: Most reviewed Books
1. python Most_reviews.py Books_rating_new.csv
2. python Most_reviews.py Books_rating_new.csv > topreviews.txt
3. python Most_reviews_plot.py

# TASK 5: Helpful scores
1. python Helpful_score.py Books_rating_new.csv 
2. python Helpful_score.py Books_rating_new.csv > helpfulscores.txt
3. python Helpful_score_plot.py


# TASK 6 : (Additional Analysis) 
    - Sentiment Analysis of Review Text
1. python Sentiment_analysis.py Books_rating_new.csv
2. python Sentiment_analysis.py Books_rating_new.csv > sentiment_analysis.txt
3. python Sentiment_analysis_plot.py (Change the code to read from the .txt file)


    - Time-Based Analysis of Ratings
1. python Time_based_analysis.py Books_rating_new.csv 
2. python Time_based_analysis.py Books_rating_new.csv > time_rating.txt
3. python Time_based_analysis_plot.py
    
    - Frequent Word Analysis in Review Text
1. python Frequent_words.py Books_rating_new.csv
2. python Frequent_words.py Books_rating_new.csv > frequent_words.txt
3. python Frequent_words_plot.py

    - Correlating Helpfulness and Star Ratings
1. python Helpfulness_vs_ratings.py Books_rating_new.csv
2. python Helpfulness_vs_ratings.py Books_rating_new.csv > helpfulness_rating.txt
3. python Helpfulness_vs_ratings_plot.py

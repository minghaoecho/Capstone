
# Amazon Product Recommendation system

## Executive summary


This project is to try to reproduce the amazon recommendation system which is one of amazon's best features. 
To achive the goal, I got data from both UCSD data set and also I used selenium to get scrape product information from amazon's website.
The score I used is the cosine similarity score, and based on the the data we have, our model perform better for content based reccmendation system rather than user based recommendation


## Summary of Statistical Analysis

To get a good recommender, I first fit the model on indivual user's rating for each product. As our dataset is based on item number, user's consistensy is limited, so score is not perfect.
While when I build recommendation based on categories and brand, product recommendation makes more sense. After that I clusered the text for brand and category the score improves more. 
From the model we can tell, as user information is limited, NLP with clusteing gives better result for a content based recommendation system.


# Understanding repo

Understanding of the repo:
    in this repo, the first notebook is the cut the huge user review dataset to several pieces, as this is a large data, we will focus on year 2018
    second notebook is the selenium scraper that have been scraping during the data cleaning and modeling procesll
    The 3rd notebook has data cleaning and 3 recommender system based on user, basic content and clustering content.
    the Data will be upload to SQL and the flask app will retrive the data from SQL to performe for users.

# Result
![content]('/Asset/content.png')


# Flask App
![content]('ASset/content_flalsk.png)
![content]('ASset/user_flalsk.png)

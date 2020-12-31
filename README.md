# Movie Review System

##### 1. Users of the service can review only movies which are released so far, they cannot review upcoming movies.
##### 2. Users can give a review-score between 1 to 10. (Higher the score the better the liking for the movie). Currently we are not allowing a user to review the same movie multiple times.
##### 3. The service by default on-boards a user as a ‘viewer’. Later a ‘viewer’ can be upgraded to a ‘critic’ after he/she has published more than 3 reviews for various movies.
##### 4. Critics are considered as experts in the judgement here, so critics reviews will be captured with more weightage. i.e. 6 review rating of a critic will be considered as 12 (2x) NOTE: Older reviews by the user as `viewer` shall not be affected.


See Code in movie/views.py

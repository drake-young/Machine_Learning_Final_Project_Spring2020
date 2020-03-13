# Machine Learning Final Project

A comparative evaluation of the performance and overhead of both Locality-Sensitive Hahsing and Classification when used in a search-by-image application.

The specifics and results will be added as a later data, as the project is still in progress

<hr/>

## Completed:

* Locality-Sensitive Hashing functionality is fully operational with the dummy dataset patches_color.csv, which contains 100 pixel vectors. Each row of the pixel vectors contains 400 RGB tuples to model a 20x20 image patch
* Utility functions for reading images as formatted DataFrames as well as storing DataFrames as images
* Evaluation for the LSH in terms of cpu time (perf_counter)

## To Do

* Implement the classification search by classifying query images, and evaluating only images within the determined class of the query. 
* Evaluate the performance of search-by-image via classification
* Enable the program to work with the full dataset located here: https://www.kaggle.com/puneet6060/intel-image-classification
* Convert the above dataset into a csv representation to be workable
* Create evaluation metrics which allow comparison of the two programs and visualize the differences

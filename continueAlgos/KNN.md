K-Nearest Neighbors (KNN)

KNN is a "lazy learner" that makes decisions based on the proximity of data points. It is highly intuitive and works for both classification and regression.

The Concept: It assumes that "birds of a feather flock together." To classify a new point, it looks at the k closest existing points in the dataset and takes a majority vote.

    The Math (Euclidean Distance):
    d(p,q)=i=1∑n​(qi​−pi​)2​

The Project: Movie Recommender System

Goal: Suggest movies to a user based on their preferences.

Implementation: Represent movies as points in space based on features like genre, duration, and director. Find the "nearest neighbors" to a movie the user already likes.

Dataset: https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system

Steps: follow all previous steps

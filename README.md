
Author: Jervis Muindi   
Date: October 2013   


# Word Suggest

##Introduction

Word Suggest is a simple idea that aims to help people with composing sentences. Given the current
word, word suggest program will attempt to auto-complete the next word for the user by showing
possible candidates. 

## Algorithm
Algoritm for program is kept simple to simplify implementation. Essentially, there are three steps
involved.

1. Find all words in an input dataset
1. For each word, build a hashmap that has the word as the key, and all the words that we find
in the dataset that come after this word along with how many times it appears
1. So, Given a candidate input word, look it up in the built hashmap and return the word
that apppears the most times.


<strong>NOTE:</strong> This is an O(N^2) algorithm due to the second step. That is too slow as I'd want to be able 
to process large data sets quickly. TODO(jervis): Optimize that step to make it an O(N) algorithm
so ideally we build the same data-structuure but do it in O(N) with one parse through the data. 


## Application
The main usecase here is to be used as a general API that can be queried to give word suggestions
based on the previous word. 


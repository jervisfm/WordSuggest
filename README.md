Author: Jervis Muindi   
Date: October 2013   


# Word Suggest

##Introduction

Word Suggest is a simple program that aims to experiment with the idea of helping people with composing sentences. Given the current
word, word suggest program will attempt to auto-complete the next word for the user by showing
possible candidates. 

## Algorithm
Algorithm for program is kept simple to simplify implementation. Essentially, there are three steps
involved.

1. Scan all words in an input dataset and process them in pairs <previous_word, current_word>. Would
need to keep track of previous word and also respect sentence boundaries.

1. For all  word pairs, build a hashmap that has the first word as the key, and then keeps track about
how often the second word appears as the value. To allow efficient updating of word counts during data import,
 we store these in a hashmap as well.<br/>
So the data structure looks like:<br/>
Hashmap(word - > Hashmap(word -> word_count))

1. So, Given a candidate input word, look it up in the built hashmap and return the word
that apppears the most times.

TODO(jervis): Convert this processed data into a form that will allow quick lookups (the above structure is not 
ideal due to the values not being sorted by word-count). Bonus: try and see it we can do that online, otherwise 
will have to resort doing another pass through the processed data to sort based on word-count.  

SideNote: I have considered perhaps using bayes theorem in predicting the probabilities as this is a possibility. 
In general Bayes says: P(A|B) = P(A and B) / P(B) = P(B|A)P(A) / P(B). 

In our case: we want to compute P(some_next_word | current_word).  
However, this value should already match our word-frequency counts so we can just use those. i.e, given a word
like 'hello', the most likely subsequent is one that appears most often after 'hello' from the original body
of input text. 

TODO(jervis): I take that back. Modeling with probabilities will actually be useful. Small scale testing has
shown the suggested words will always be the same for a given input. This is not ideal as it essentially
always picks the commonly occuriing word pairs. 

NOTE: So essentially, I want to return a word based on the probability distribution that we have seen. At one extreme,
we can have/keep the entire probability distribution modelling the probabilities of consecutive words for a given
particular word. To give an answer, we'd then sample from this distribution. The sampling process described 
in this Wikipedia article can be used directly: http://en.wikipedia.org/wiki/Categorical_distribution#Sampling

## Application
The main usecase here is to be used as a general API that can be queried to give word suggestions
based on the previous word. 


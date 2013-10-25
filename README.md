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


## Application
The main usecase here is to be used as a general API that can be queried to give word suggestions
based on the previous word. 


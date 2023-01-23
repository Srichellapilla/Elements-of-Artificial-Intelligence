
###### Made by Sri Varsha Chellapilla (srchell), Akash Bhapkar (abhapkar) and Roopank Kohli (rookohli) 

# Part 1: Raichu

## Approach:

To the given turn taking game which is almost like chess with white pichu, pikachu, raichu and black pichu, pikachu raichu minimax algorithm with alphabeta pruning is used to determine the best move for the player. 

## Abstraction:

* State space: All the possible combination of moves of each player
* Initial state: The input board 
* Successor function: All the possible moves of each player that is 
     - If the player is white return all the possible moves of white pichu, pikachu and raichu
     - If the player is black return all the possible moves of black pichu, pikachu and raichu
* The actions of MAX and MIN alternate, with MAX taking the lead in the first state.
* Terminal test:  It determines if the state is terminal, that is if it is a win or loss for MAX player or if it is a draw.
     - To check for terminal state we calculate the difference between the MAX and the MIN players, that is the difference between total number of white players and total number of black players. If the difference is greater for MAX player it is a WIN or it is a LOSS. Otherwise its a draw.
 
## Evaluation function:

Evaluation function e(s) is used to determine the favorable state for MAX,
* If e(s)>0 the state is favorable for MAX player,
* If e(s)<0 the state is favorable for MIN player,
* If e(s)=0 the state is neutral.

The calculate the evaluation function for the raichu game the following features were defined:
* if the MAX player can kill either pichu, pikachu or raichu of the MIN player the feature is given more weight so that the best move can be returned from the successors.
    - The difference between MAX and MIN player count(white)-count(black) is used to determine if a kill is possible.
* the forward move is given next hight weight after kill because only when a pichu or pikachu moves forward they can become raichu when reaching the last row of the opposite side.

## Problems faced:

Initially several problems were faced while trying to return the best move for the MAX player.
* While defining the moves for pichu, pikachu and raichu the jump move and the evolution of pichu and pikachu to raichu where not being returned as best move due to the weight added to the features in the evaluation function.
* While the game tree was being traversed for a larger depth the solution was not being returned in the time limit.
*  I had to try various combinations of festures including giving equal weight to diagonal and forward moves. The player would just either go right or left but not forward.

## References:

The following youtube video was referred to implement the minimax algorithm with alpha-beta pruning.
Please find the link below:

https://www.youtube.com/watch?v=zp3VMe0Jpf8&t=10s&ab_channel=JohnLevine


# Part 2: Quintris

## Approach:
This problem we had to deal with a Quitris game. The game has an empty board with height 25 and there are certain set of pieces which we need to place according to the best combination.

In the beginning, we thought the approach could be to have successors of board with current piece placed in multiple combinations. But when we approached the problem, since we knew what next peice is going to be, we used it to make a better decision.

## Abstractions:

*State Space* : All possible board states after placing current piece and next pieces

*Initial State* : Current board configuration

*Goal State* : Maximum score with pieces placed height as minimum as possible

*Successor Function* : All board combinations with current and next piece placed

*Cost Function* : Cost for given board with 4 possible heuristics

## Solution:
The solution we implemented involves generating all the successors for the board with both the pieces placed and then decide where current piece to be placed.
After calculating the successors, we are calculating the cost for each board and then choosing the maximum cost board among them.

We applied below heuristic to define the cost of the board:
cost = x1 * aggregateHeight + x2 * Bumpiness + x3 * completeRows + x4 * numberOfHoles
where x1, x2, x3, x4 are wights need to be assigned for each parameter. Since aggregateHeight, bumpiness, numberOfHoles need to be as low as possible and completeRows more.

After running it multiple times, we decided to put x1, x2, x3, x4 = -5.5, -4.5, 4, -1.8

## Design Decisions:
Since there are possibly 10000 successors coming after placing both the pieces, there was a need to use a fast performing data structure to pick the maximum of them.
Therefore we used heapq in python to select the board with maximum cost from set of successors.

## Problem Faced:
The major problem we faced is to find the correct parameters and corresponding wights x1, x2, x3, x4. we tried different parameters such as average height, height difference, std of heights and with multiple weights.
After trying much of parameters and weight values, we decided to go with 4 parameters and their weights.

# Part 3: Truth be told

Here, we were provided with the following :

* train.txt - a training dataset containing user generated reviews of multiple hotels present in the city of Chicago. 
It contains both fake and legitimate reviews and its purpose is to train our classifier.

* test.txt - the testing dataset containing user generated reviews of multiple hotels present in the city of Chicago.
I contains both fake and legitimate reviews and it is used to test/evaluate the genuineness of a hotel review. Each 
review is fed to the classifier and it determines the legitimacy of the review.

* route.py - it contained the skeleton code where we are supposed to publish our solution.

## Problem Statement

To write a program that estimates the Naive Bayes parameters from training data (where the correct label is given), and 
then uses these parameters to classify the reviews in the testing data. The task is to classify reviews into faked or 
legitimate, for 20 hotels in Chicago.

## Solution

Naive Bayes is a family of probabilistic algorithms that take advantage of probability theory and Bayes’ Theorem to 
predict the tag of a text (like a customer review). They are probabilistic, which means that they calculate the 
probability of each tag for a given text, and then output the tag with the highest one. The way they get these 
probabilities is by using Bayes’ Theorem, which describes the probability of a feature, based on prior knowledge of 
conditions that might be related to that feature. We've tried to implement Multinomial Naive Bayes here. The multinomial
naive Bayes model is typically used for discrete counts. Below we have tried to explain the implementation of our 
solution in a hierarchical form.

### Data Cleaning

The raw data provided to us contains some anomalies and redundancies that may hamper the computation of our classifier.
The raw data, a sequence of symbols (i.e. strings) cannot be fed directly to the algorithms themselves as most of them 
do not contribute towards the classification of reviews. In order to clean/filter our data, certain operations were 
applied over the data so that it produces optimal result. These operations include removing stopwords, converting every
single word to lowercase, removing punctuation marks, removing non ascii characters, and applying regex to surpass the 
meaningful words. This process was applied over both training and testing dataset.

###  Frequency Calculation

As per the Naive Bayes theorem, our efforts should go to calculating the frequency of every word rather then looking at
the individual sentences. This means that the frequency of a word is calculated in both fake and legitimate part of the 
dataset, and then based on the frequency, we calculate the probability of that word in that category.

### Applying Conditional Probability using Naive Bayes 

The final step is just to calculate every probability and see which one turns out to be larger. Calculating a 
probability is just counting in our training data. First, we calculate the a priori probability of each word: 
for a given sentence in our training data, Then, calculating how many times the word categorical texts divided by the 
total number of words in that category.

### Using Laplace Smoothening

At times, we might encounter one or more than one word in our testing text, which does not appear in our training data. 
This can cause a problem as it will make our probability equal to zero. This problem can be handled using Laplace 
Smoothening. It is nothing but a technique where a small-sample correction, or pseudo-count, will be incorporated in 
every probability estimate. 

## Design Decisions

A number of data structures including list, set, dictionary etc. and a variety of inbuilt functions like 
math.log, str.maketrans were used in this solution. Along with that, regular expressions were used for filtering
out the unnecessary words. The main approach to decide the designing decisions for this problem was to implement 
the solution in minimum time complexity. Log of probabilities was taken and added in place of multiplying so that 
heavy computation is avoided and to ensure that very small probabilistic values are not ignored while calculating
the final conditional probability. The output here displays the accuracy attained by our classifier on this specific
dataset which comes out to be around 80-85%. 

## Assumpltions

It was assumed that every word in a sentence is independent of the other ones. This is done so that we can concentrate 
on individual words rather than sentences.

## Challenges Faced

Problems were faced for cleaning the data as a number of irrelevant and grammatically incorrect words were present in 
the database. Other than that, calculating probability of those words, which were not there in training data, was another
challenge, but it was appropriately handled using Laplace Smoothening. Lastly, computing probability of those words 
which had a small frequency was a problem, it was solved by taking the log of probabilities and adding them.



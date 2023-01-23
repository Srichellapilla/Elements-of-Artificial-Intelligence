
Report submitted by Sri Varsha Chellapilla, Gomati Sankarakrishnan Rahul, Jaswanth Kumar Ranga
## Part 1: Part-Of-Speech Tagging
A part-of-speech tag is a label assigned to each word in a text (sequence of words) to indicate the part of speech to which it belongs.
The following approches were used for POS:
1. Simplified Bayes net
2. HMM
3. MCMC with gibbs sampling

### Solution Overview:
**Simplified:**  In the simplified approch we have calculated the max of the the probability of a word being of certain part of speech divided by the total number of words in the given data.

**HMM:** There is a dependency on successive words in this approch, in addition to the word-to-sentence relationship. We used the Viterbi technique to accomplish this, which keeps track of the maximum probabilities until each of the sentence's words, beginning with the first, and iteratively calculating the maximum probability until each word, using the maximum probabilities until the previous word, which are pre-calculated.

**MCMC with Gibbs Sampling:** Generated a  random sample of size sentence and iterated it over possible parts of speech and calculate posterior probability for each sample generated.

### Problems Faced:
* While calculating the Gibbs approch the code was extremely slow when the dictionaries were stored globally, and when calculated the probabilities each time. To overcome this certain dictionaries are initialized locally and the calculated values were stored.
* As the sample size increased the accuracy in the Viterbi approach decreased due to incorrect calculation of transition probability.

### Output Images:

![part-1 accuracy](https://media.github.iu.edu/user/18386/files/37af6080-5450-11ec-8f77-baa85c1bcb6b)

## Part 2: Ice Tracking
The goal of this problem is to find airice boundry and ice rock boundry using the following algorithms:
* Simple Bayes net
* HMM Viterbi
### Solution Overview:
**Simple:** Assuming that the number of pixels given for airice would always be 10 pioxels greater than that of the icerock boundry.
We read the image and then calculate the edge strength. The value of edge strength is used to determine the boundry, higher the value of edge strength closer we are to the boundry.

**HMM viterbi:** In first iteration we calculate the initial probablities along with the corresponding emission probabilites in every further iteration a transition probability is incorporated with emmision probability to figure out the most optimal transition of pixels along the incrementening values of column. To achieve this we have given maximum weight to transition probability.

### Problems Faced:
* While calculating the transition and emission probability for HMM Viterbi and Human feedback, due to the incorrect assignment of weights the icerock boundry was far below the original boundry. 

### Output Images:


* Output image 23.png for airice and icerock boundry.


![airice_icerock_23](https://media.github.iu.edu/user/18481/files/083a1000-52f9-11ec-8fc8-064518e909aa)


* Output image 09.png for airice and icerock boundry.


![airice_icerock_09](https://media.github.iu.edu/user/18481/files/d034cc00-52fc-11ec-8a06-7cd0ba3afb66)



## Part 3: Reading Text
The goal is to return a text from an image using Simple Naive Bayes classifier and HMM Viterbi.
### Solution Overview:
- For Simple Naive Bayes net, calculated emisiion probabilities giving 0.77 weightage to * and 0.13 to space and 0.1 to not match. The minimum of the negative logs of the probability is taken to return the text from the image.
- For HMM Viterbi calculated the emission, initial and transition probabilities to find the likelihood of theoccurence of the letters. Here the probability of the previous character is taken to find the probability of the current character.

**Emission Probability:**
The emission probabilities are just the total of all P(image[i][j]|letter), and the naive Bayes assumption implies that P(image|letter) equals P(image[i][j]|letter). The outcome, however, is a sum rather than a product because we're using -log.

**Transition Probabilities:**
The probability of a character transitioning to another character must be saved. We may achieve this by counting the number of times a character appears after another.

**Initial Probability:**
We must utilize the training data to calculate this probability. In this situation, we must calculate the chances of each character being the first letter of the sentence. We do this by going through each word and counting the first characters, counting them if they match, and then dividing by the total number of words.

### Problems faced:
Assigning appropriate weights to emission probabilities helped in recognizing the text in image accurately.

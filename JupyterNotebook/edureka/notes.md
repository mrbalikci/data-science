Math Statistics
Hacking 
Data Bases
Cooding 

Make the company to make a better business decisions 
Complex Data Problems with scientific disiplines 

# Road Map
Tech Skills: 
R/Python SAS
BI
Data Warehouse 

Business Skills
Analytic Problem-Solving
Effective Communication
Creative Thinking
Industry Knowledge

Experties in the field

Work on Project related to the field 

Analytical Skills > Communication Skills > Critical Thinking > Attention to detail > Mathematics Skills > Technical Skills/tools: R, py, Java, 
Calculus/Statistics, Signal Processing, Applied Maths, Neural Networks, Language Processing 

Statistics
Prog Languages 
Software 

## Data 
Quantitative Data >>  Discreet and Continuous Data: Nominal Data -- Ordinal Data -- Binary Data

### Variables and Research
Independent and Dependent variables 

### Population and Sampling 
population of interest 
sample of the population of interest 

Sampling techniques 
Probability and non-probability 

- Sampling error 

Random
Systematic sampling 
Stratified sampling

### Measure of Center
- Range 
- Mean
- Mode

# Measure of Spread 
- Range 
- inter quartile range 
- variance 
- standard deviation 

# Skewnes 
- left 
- right 
- symetric 
- non-symetric 

# Confusion Matrix 
accurac = tru pos + tru neg / tru ps + tru neg + 

# Probability 
measure of the likelihood 

- Probability Density function
- normal distribution
- central limit theorem 

# Machine Learning 
- alghoritms that makes learning 
1. uses data to detect patterns
2. use computer program to teach themselfs 
3. find the hidden insights 
4. automate the model

### Applications of Machine Learning 
- Siri, alexa, google, cortana 
- NLP: natural language processing 
- Google translate 
- Tesla cars 
- Netflix, Amazon, hulu, etc 
- dynamic pricing 

### Life Cyle 
Collect data: 
Data wrangling: discover, structure, clean, enrich
Analyse Data
Train Algorithm
Test Algorithm
Operation and Optimization > Deployment

### Python
- Seaborn: visual statistical model -- heat maps, etc 
- Matplotlib
- Scikit-learn
- Pandas: data wrangling 
- Numpy: numerical python, mathematical purposes 

### Types of Learning 
1. Supervised Learning: 
- Input raw data 
- label face, label non face 
- we have desired output 

2. Unsupervised learning 
- we don't have label as output 
- clusters: apples, bananas, etc 

3. Rainforcement Learning 
- takes the best action based on the data 

### Supervised Learning 
- imput x and output y
- train and test data sets 
- learning 
- model 
- test the model 
- data > model > predicted outcome 

linear regression: estimate values based on 
logistic regression: estimate discreate values like yes and no
decision tree: classification categorical 
random forest: 
naive bayes classifier: based on assumption of 


1. Linear Regression: 
- dep and ind variables 
- y = a + bx
- correlation important 
- regression line or fit of line 
- distance between the regression line 
- ex: 

2. Logistic Regression
- If there are one or more than one independent variables to determine the outcome 
- Outcome is binary like 0/1s
- Logistic Regression Curve: Sigmoid Curve 
- Ploynomial Regression

3. Decision Tree 
- Root split -- child split 
- outlook - sunny - overcat - rain 
- sunny - humidity 

4. Random Forest 
- An enseble classifer made using many decision tree models 
- Better than the decision tree coz can be more accurate 
- 

5. Naive Bayes
- predictive modeling 
- classification 
- Conditional Probability: Given Hypothesis H, evidence E based on Bayes P(H|E) = P(E|H).P(H)/P(E)

### Unsupervised Learning 
- unlabelled data 
- clustering models
- distributes for predictions 
- clustering most important 

Clustering: Group of similar records 
- how many groups 
- partitioning is the goal
- unlabelled data 
- like netflix, amazon, flickr
- banking, insurance, retail, banking
- recommendation of movies 
- Exclusive Clustering: Several 
- Overall clustering 
- Hierarchical Clustering 

K- Means Clustering 
- predefined groups 
- nubmer of clusters
- centroid
- distant object to centroids 
- guess the number of clusters
- data points on each clusters
- distance to the points determined
- steps repated until new centroids determined 

- how to determine the value of k
- sum squared error: SSE
- the best number of cluster at the 'elbow'
- the graph is changing 
- pros: simple, understandable, automatically assing to cluster
- cons: must define clusters, all items forced into clusters, unable to handle noisy data and outliers, it effects whole model 

1. Fuzzy Clustering:
- each data point can belong to more than one cluster
- range from 0 to 1
- degree of membership is important 
- allows data in multiple cluster
- naturel rep of the behavior of genes
- genes in multiple functions 
- need to define c 
- 

2. Hierarcy Clustering 
- build up clustering from bottom-up
- does not require the number of clusters 
- it cannot be undone 
- too slow for large datasets 

### Market Basket Analysis Algorithms 
- association rule mining 
- apriori algorithm: uses freq sets to generate association rule. based on the concept of subset of frequent items 
- ex: how items are associated to each other
customer who buy bread likely will buy jam 60%
customer who purchase laptop also may purchase laptop bags

so, how items are related to each other
support > confidence > lift 
freq(a,b)/n
frea(a,b)/freq(A)
support / supp(a)xsupp(b)


## Rainforcement Learning 
- agent learns to behave in an env by performing actions and seeing the results 
- what action should be taken 
- ex: 
baby starts crawling but falls 
agent: RL algorithm that learns from trail and error 
environment: world the agent moves
action (A): possible steps 
state (S): current condition 
reward (R): instant return from env 
policy (pi): approach agent uses to determine next action
value (V): expected long-term return 
action-value (Q): extra parameters 

ex: RL must be trained so takes the best action so reward is maxiumum 

Value of Gamma is 0-1
Exploitation using already known exploited form 

K-Armed 
The Epsilon Greedy Algorithm 
Markov Decision Process  (MDP)

### Understanding Q-Learning 
- metrix R
- Q(state, action) = R(state, action) + Gamma * max(Q(next state, all actions))
- set gamma parameter and envi reward in matrix R
- 












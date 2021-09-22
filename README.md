# Twitter-sentiment-analysis

A sentiment analysis model trained using a Kaggle GPU. 

# Dataset

- Train/test split : 90% / 10% 
- Size : 1.6M samples 
- Link : https://www.kaggle.com/ibrahimserouis99/twitter-sentiment-analysis-and-word-embeddings


# Model

- Model type : Sequential, RNN, classification
- Optimizer : Adam
- Loss function : Binary cross entropy 
- Outputs : 0 or 1. 0 = negative, 1 = positive
- Training epochs : initially 50, but 18 with early stopping and a patience factor = 10

## Architecture

![Model_architecture](Screenshots/Model%20architecture.png)

# Libraries

- Deep Learning Framework : Tensorflow 2.0 or higher 
- Data visualization : Pandas, seaborn, matplotlib
- Regular expressions builder : re 
- NLP library : NLTK, with stopwords
- Train/test splitting : Scikit-learn

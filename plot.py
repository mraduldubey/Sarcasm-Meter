'''BernoulliNB gave slightly better results than MultinomialNB on just TF-IDF feature vector.'''

import numpy as np

#Load the binary files of sarcastic and non-sarcastic tweets
sarcasm=np.load("posproc.npy")
neutral=np.load("negproc.npy")

#Print sample data
print ("10 sample sarcastic lines:")
print (sarcasm[:10])
print ("10 sample non-sarcastic lines:")
print (neutral[:10])

#Stats
sarcasm_size=len(sarcasm)
print ("Total sarcastic lines = "+str(sarcasm_size))
neutral_size=len(neutral)
print ("Total non-sarcastic lines = "+str(neutral_size))

#Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

dataset_pos = sarcasm
dataset_neg = neutral
print ("Total length of dataset = "+str(len(dataset_pos)+len(dataset_neg)))

##Plotting data using LSI(SVD) since PCA doesn't support sparse data.

pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
])        

X = pipeline.fit_transform(dataset_pos)
Y = pipeline.fit_transform(dataset_neg)

data2DX = TruncatedSVD(n_components=2).fit_transform(X)
data2DY = TruncatedSVD(n_components=2).fit_transform(Y)

#Red - Sarcastic, Green - Regular.
plt.scatter(data2DX[:,0], data2DX[:,1], c=np.array([1, 0, 0]))
plt.scatter(data2DY[:,0], data2DY[:,1], c=np.array([0, 1, 0]))
plt.show()              #not required if using ipython notebook	
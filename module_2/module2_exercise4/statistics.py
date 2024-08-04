
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import gdown


def compute_mean(x):
    return np.mean(x)


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    print(x[3-1])
    a = int(size/2)
    if (size % 2 == 0):
        # your code here **************************
        return (x[a-1] + x[a])/2
    else:
        return x[a+1]  # your code here **************************


def compute_std(x):
    mean = compute_mean(x)
    var = (np.sum((x-mean)**2))/len(x)
    return np.sqrt(var)


def compute_correlation_cofficient(x, y):
    N = len(x)
    numerator = N*(np.sum(x*y)) - np.sum(x)*(np.sum(y))
    denominator = np.sqrt(N*np.sum(x**2) - np.sum(x)**2) * \
        np.sqrt(N*np.sum(y*y) - np.sum(y)**2)
    return np.round(numerator / denominator, 2)


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores =  cosine_similarity(context_embedded, query_embedded).reshape((-1,))

    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores . argsort()[- top_d:][:: -1]:
        doc_score = {'id': idx, 'cosine_score': cosine_scores[idx]}
        results.append(doc_score)
    return results


def corr_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded =  tfidf_vectorizer.transform([question.lower()])
    corr_scores =  np.corrcoef( query_embedded.toarray()[0], context_embedded.toarray())
    corr_scores = corr_scores[0][1:]
    # Get top k correlation score and index its
    results = []
    for idx in corr_scores . argsort()[- top_d:][:: -1]:
        doc = {'id': idx, 'corr_score': corr_scores[idx]}
        results.append(doc)
    return results


# Question 1
X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print(" Mean : ", compute_mean(X))

# Question 2
X = [1, 5, 4, 4, 9, 13]
print(" Median : ", compute_median(X))

# Question 3
X = [171, 176, 155, 167, 169, 182]
print('compute_std(X):', compute_std(X))

# Question 4
X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print(" Correlation : ", compute_correlation_cofficient(X, Y))

# Question 5
path = '/Users/nguyendung/git/AIO_exercises/module_2/module2_exercise4'
file_url = 'https://drive.google.com/uc?export=download&id=1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
gdown.download(file_url, 'advertising.csv', quiet=False)
data = pd.read_csv("advertising.csv")

x = data['TV']
y = data['Radio']
corr_xy = compute_correlation_cofficient(x, y)
print(f" Correlation between TV and Sales : {round(corr_xy, 2)}")

# Question 6
features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_cofficient(
            data[feature_1], data[feature_2])
        print(f" Correlation between{feature_1} and {
              feature_2}: {round(correlation_value, 2)}")

#Question 7
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)


# Question 8
print(data.corr())

# Question 9
plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()

# Question 10
path = '/Users/nguyendung/git/AIO_exercises/module_2/module2_exercise4'
file_url = 'https://drive.google.com/uc?export=download&id=1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6'
gdown.download(file_url, 'vi_text_retrieval.csv', quiet=False)

vi_data_df = pd.read_csv("vi_text_retrieval.csv")
print(vi_data_df)
context = vi_data_df["text"]
print('context',context)
context = [doc.lower() for doc in context]

# encode văn bản thành vector
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
context_embedded.toarray()[7][0]
print('context_embedded.toarray()[7][0]',context_embedded.toarray()[7][0])
print(tfidf_vectorizer.vocabulary_.items())

# Question 11
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print(results[0]['cosine_score'])


# Question 12
results = corr_search(question, tfidf_vectorizer, top_d=5)
print(results[1]['corr_score'])


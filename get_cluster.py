"""
author
"""
import pickle
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

#DOC_INPUT_FP = "sample_news.txt"
#DOC_DISTANCE_FP = "sample_news_wmd_d.pk"

DOC_INPUT_FP = "all_twitter_by_line.txt"
DOC_DISTANCE_FP = "twitter_wmd_d.pk"

docs = list()
with open(DOC_INPUT_FP, "rb") as f:
    for line in f:
        doc = line.strip().split('\t')[1]
        docs.append(doc)

with open(DOC_DISTANCE_FP, "rb") as f:
    dis_matrix = pickle.load(f)

print(np.sum(np.isnan(dis_matrix)))
n = dis_matrix.shape[0]

condensed_dist = [dis_matrix[j][k] for j in range(n) for k in range(j+1, n)]
print(condensed_dist)

# print(np.sum(np.isinf(condensed_dist)))
# print(np.sum(np.isnan(condensed_dist)))

Z = linkage(condensed_dist, 'ward')

MAX_D = 3.8
C = fcluster(Z, MAX_D, criterion="distance")

clustered_doc = pd.DataFrame(data={
    'cid': C,
    'doc': docs
})

print(clustered_doc)

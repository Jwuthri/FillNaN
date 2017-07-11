# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


class Kmeans(object):

    def __init__(self, filepath, n_clusters=None):
        """
        Args:
        -----
            filepath (string): Path of the data file
            n_clusters (int): Number of class needed
        """
        self.n_clusters = n_clusters
        self.dataset = pd.read_csv(filepath, encoding="utf-8-sig")
        self.dummifyCategoricalVariable()

    def fillMissingValue(self):
        self.dataset.fillna(getattr(self.dataset, "mean")(), inplace=True)

    def dummifyCategoricalVariable(self):
        dummify = self.dataset.loc[:, self.dataset.dtypes == object]
        for col in dummify.columns:
            df = pd.get_dummies(self.dataset[col], drop_first=True)
            self.dataset = pd.concat([df, self.dataset], axis=1)
        self.dataset.drop(dummify.columns, axis=1, inplace=True)

    def wcss(self, X, max_cluster=20, plot=True):
        self.fillMissingValue()
        wcss = list()
        for i in range(1, max_cluster):
            kmeans = KMeans(n_clusters=i, init='k-means++')
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)
        if plot:
            plt.plot(range(1, max_cluster), wcss)
            plt.title('Elbow')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            plt.show()

        return wcss

    def clustering(self, X, nb_cluster=2):
        kmeans = KMeans(n_clusters=nb_cluster, init='k-means++')

        return kmeans.fit_predict(X)

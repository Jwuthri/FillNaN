# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: JulienWuthrich
"""
import pandas as pd

from fillnan.kmeans import Kmeans


class FillNaN(object):

    def __init__(self, filepath, n_clusters=None, method="clustering"):
        """
        Args:
        -----
            filepath (str): Path of the data file
            n_clusters (int): Number of class needed
            method (str): Method of filling:
                clustering, mean, median
        """
        self.n_clusters = n_clusters
        self.filepath = filepath
        self.method = method
        self.dataset = pd.read_csv(filepath, encoding="utf-8-sig")

    def nbCluster(self):
        user_input = input('How many clusters do you want ? ')
        try:
            return int(user_input)
        except ValueError:
            raise ValueError("An int is requiered")

    def meanCluster(self, col):
        d_cluster = dict()
        for cluster in self.dataset["Cluster"].unique():
            d_cluster[cluster] = self.dataset[
                self.dataset["Cluster"] == cluster
            ][col].mean()

        return d_cluster

    def fillWithMeanCluster(self, subset_df, col, d_cluster):
        for idx, row in subset_df.iterrows():
            value = d_cluster.get(row["Cluster"])
            self.dataset.set_value(idx, col, value)

    def fillCol(self, col):
        subset_df = self.dataset[~self.dataset[col].notnull()]
        d_cluster = self.meanCluster(col)

        return self.fillWithMeanCluster(subset_df, col, d_cluster)

    def fill(self):
        km = Kmeans(self.filepath)
        self.dataset = km.dataset
        _ = km.wcss(km.dataset)
        nb_cluster = self.nbCluster()
        cluster = km.clustering(X=km.dataset, nb_cluster=nb_cluster)
        km.dataset["Cluster"] = cluster
        self.dataset["Cluster"] = cluster
        for col in self.dataset.columns:
            self.fillCol(col)

        return self.dataset

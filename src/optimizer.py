import sys
sys.path.append('../')
from src import reader as r
from src import visualization as v
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.metrics import silhouette_score


def elbow_kmeans(X, min_k=2, eps = 1e-2, step=10):
    error = 0
    Ks = []
    Js = []    
    it = 1
    J = 0.
    k = min_k
    last_j = 999999999.
    print("###############################")
    while ((error > eps) or (it == 1)):
        print("Number of Clusters:",k)
        print("Starting K-means++")
        cluster = KMeans(n_clusters=k,random_state=42,n_jobs=-1)
        cluster_result = cluster.fit(X)
        print("Finished")
        error = J
        J = cluster_result.inertia_ / X.shape[0]        
        print("J =",J)        
        error = abs(error-J)  
        Ks.append(k)
        print("error =",error)
        Js.append(J)        
        print("###############################")
        k += step
        it += 1                    
        if J > last_j: 
            break        
        last_j = J        
        
    best_K = k-step
    print("\nBest k:",best_K)
    print("Number of iterations:",it)
    return best_K, Ks, Js

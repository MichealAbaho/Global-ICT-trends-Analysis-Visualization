import numpy as num
import pandas as plib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from math import *
from matplotlib import style
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
style.use('ggplot')

def cluster(file):
	'''clustering the total subscriptions into 4 clusters'''
	readCluster = plib.read_csv(file, encoding='latin1')

	x_values = [i+1 for i in range(len((readCluster['Countries']).tolist()))] 
	y_values = [round(j/1000000) for j in ((readCluster['total_subscriptions']).tolist())]

	clusterPair = []

	for x,y in zip(x_values, y_values):
		clusterPair.append([x,y])

	clusterArray = num.asarray(clusterPair)
	
	kmeans = KMeans(n_clusters=4)
	kmeans.fit(clusterArray)

	centroids = kmeans.cluster_centers_
	labels = kmeans.labels_

	colors = ['g.','r.','b.','m.']
	font = {
        'color':  'black',
        'size': 13,
        'weight': 'bold'
        }

	for i in range(len(clusterArray)):
		plt.plot(clusterArray[i][0], clusterArray[i][1], colors[labels[i]], markersize=10)

	plt.ylim([-500, 17500])
	plt.xlim([-10, 250])
	# plt.annotate('Developed', xy=(10, 900), xytext=(0, 1800), arrowprops=dict(facecolor='blue', shrink=0.05)
	# plt.annotate('Developed', xy=(80, 2200), xytext=(100, 3500))
	plt.tick_params(axis='x',colors='#f06215', length=5, top='off', pad=-2)
	plt.tick_params(axis='y',colors='#f06215', length=5, right='off', pad=-2)
	plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='k', s=50, linewidths=5, zorder=0)
	plt.title("Clustering the total number of subscriptions")
	plt.ylabel("total annual subsctiptions (in mlns)")
	plt.xlabel("countries")

	ax = plt.axes()
	ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
	
	plt.show()

cluster('../generated csv files/Summary_per_country.csv')


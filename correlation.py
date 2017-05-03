import numpy as num
import pandas as plib
import matplotlib.pyplot as plt
from math import *
from matplotlib import style
style.use('ggplot')
def correlation(file):

	df = plib.read_csv(file, encoding="latin1")

	x_values = (df['fixTel_subscrptions']/1000000)
	y_values = (df['fixedBroadband_subscriptions']/1000000)

	x = []
	y = []

	for i in x_values:
		x.append(i)

	for j in y_values:
		y.append(j)

	font = {
        'color':  'black',
        'size': 13,
        }

	print (max(y))
	plt.scatter(x, y, label='subscriptions', marker='o', c='b', s=50)
	#plt.axis([0, max(x), 0, max(y)])
	plt.xlim([400, (max(x)+400)])
	plt.ylim([0, (max(y))+50])
	plt.title('Fixed Telephone Vs Fixed Broadband\nSubscriptions')
	plt.tick_params(axis='x', colors='#f06215')
	plt.tick_params(axis='y', colors='#f06215')
	plt.xlabel('Fixed Telephone (in millions)', fontdict=font)
	plt.ylabel('Fixed Broadband Subscriptions (in millions)', fontdict=font)
	plt.legend()
	plt.show()  


correlation("../generated csv files/year_summary.csv")



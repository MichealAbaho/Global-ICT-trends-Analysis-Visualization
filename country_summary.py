import numpy as num
import pandas as plib

def rowsSummation(files):

	try:
	#variables to hold to hold  the processed data
		subscriptions = {'mob_subscriptions':[], 'fixTel_subscrptions':[], 'fixedBroadband_subscriptions':[], 'indInternet_subscriptions':[]}
		countries = []
		total_subscriptions = []

		''' Loops through each file, sums up each row i.e. the total subscriptions per country
		repeats this for the different subscrition type'''
		for i,j in zip(files, subscriptions):
			readData = plib.read_csv(i, encoding="latin1")
			newData_Array = num.array(readData)
			newData_ArrayList = newData_Array.tolist()
			for x in (newData_ArrayList):
				subscriptions[j].append(int(num.nansum(x[1:])))
		
		#creating a list of the countries
		for country in readData:
			countries.append(readData[country])
			break

		#Generating data frames to hold the countries, summed up subscriptions
		countryList = plib.DataFrame({'Countries': countries[0].tolist()})
		
		subFrame = plib.DataFrame(subscriptions)
		
		subFrameList = num.array(subFrame).tolist()

		#summing up the new rows to get an overall total subscription per country
		for rows in subFrameList:
			total_subscriptions.append(num.sum(rows))

		#Merging the frames and outputiing a new file
		total_subscriptions_Frame = plib.DataFrame({'total_subscriptions': total_subscriptions})
		summaryPerCountryFrame = countryList.join(subFrame)

		final_CountryFrame = summaryPerCountryFrame.join(total_subscriptions_Frame)
		final_CountryFrame.set_index('Countries', inplace=True)
		final_CountryFrame.to_csv('../generated csv files/Summary_per_country.csv')

	except (IOError, ValueError, TypeError) as e:
		print (e)


rowsSummation(['../generated csv files/Mobile_Cellular_subscriptions.csv', '../generated csv files/Fixed_tel_subscriptions.csv', '../generated csv files/Fixed_broadband_subscriptions.csv', '../generated csv files/Individual_Internet_subscriptions.csv'])




#!/usr/bin/env python
########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

def normalize(mylist):
	intermid_normalized_list = []
	normalized_list = []
	minimum = min(mylist)
	maximum = max(mylist)
	difference = maximum - minimum
	for value in mylist:
		normalized_value = 1 + (value-minimum)*(10-1)/difference
		intermid_normalized_list.append(normalized_value)
	print intermid_normalized_list
	minimum = min(intermid_normalized_list)
	maximum = max(intermid_normalized_list)
	difference = maximum - minimum
	for value in intermid_normalized_list:
		normalized_value = (value - minimum)/ difference
		normalized_list.append(normalized_value)
	print normalized_list

X = [1034.4947916667,193.8489583333,600.5052083333,10.9322916667,21.5885416667,10.9322916667,35.28125,75.7916666667,15.9583333333,15.7708333333,343.0833333333,169.27]
normalize(X)

#1.0, 0.17870590869302078, 0.5760008955648531, 0.0, 0.010410942175001528, 0.0, 0.023788443141772014, 0.06336630640532455, #0.004910341739366182, 0.0047271580060817, 0.3245048950763632
















########################################################
## CIS 700 Term Project
## Saurabh Patel, Ojas Juneja, Ronak Bhuptani
#######################################################

#!/usr/bin/env python

import numpy as np
import sys
from sklearn.cluster import KMeans

normalize_list = []
input_train = []
#this function  is main function and responsible for prediction of performance of movies
def kmeansCluster(X_list,filename):
	X = normalize(X_list)
	kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
	labels = kmeans_model.labels_
	fw  = open(filename,"w")
	for label in labels:
		fw.write(str(label) + "," + str(input_train[0]) + "," + str(input_train[1]) + "," + str(input_train[2]) + "," + str(input_train[3]) + "\n")
	fw.close()
	print labels
	return labels

#it reads csv file and place it in list	
def readCSVFile(filename):
	fr = open(filename)
	line = fr.readline()
	while line:
		mylist = []
		mylist = line.split(",")
		input_train.append(mylist[1:])
		line = fr.readline()
	return input_train

#it will normalize the values of the input file	
def normalize(X_list):
		normalize_list = []
		maximum = 0
		minimum = sys.maxint
		firstlist = []
		secondlist = []
		thirdlist = []
		fourthlist = []
		print X_list
		for mylist in X_list:
			firstlist.append(float(mylist[0]))
			secondlist.append(float(mylist[1]))
			thirdlist.append(float(mylist[2]))
			fourthlist.append(float(mylist[3]))
			
		firstlist = normalizeHelper(firstlist,min(firstlist),max(firstlist),True)
		secondlist = normalizeHelper(secondlist,min(secondlist),max(secondlist),False)
		thirdlist = normalizeHelper(thirdlist,min(thirdlist),max(thirdlist),False)
		fourthlist = normalizeHelper(fourthlist,min(fourthlist),max(fourthlist),False)
		
		for value1,value2,value3,value4 in zip(firstlist,secondlist,thirdlist,fourthlist):
				value_list = []
				value_list.append(value1)
				value_list.append(value2)
				value_list.append(value3)
				value_list.append(value4)
				normalize_list.append(value_list)
		return normalize_list

		
def normalizeHelper(mylist,minimum,maximum):
			normalize_list = []
			for value in mylist:
					y = 1 + (value-minimum)*(10-1)/(maximum-minimum)
					normalize_list.append(y)
			return normalize_list
			
#if any one flag(sentiment factor) is set to true then it will do weighted normalization otherwise non weighted normalization
def normalizeHelper(mylist,minimum,maximum,weight):
			normalize_list = []
			for value in mylist:
					if weight == True:
						y = 1 + (value-minimum)*(30-1)/(maximum-minimum)
					else:
						y = 1 + (value-minimum)*(10-1)/(maximum-minimum)
					normalize_list.append(y)
			return normalize_list

X_list = readCSVFile("kmeans_file.csv")
predictions = kmeansCluster(X_list,"clustered_results.csv")

		
		
	

	
	

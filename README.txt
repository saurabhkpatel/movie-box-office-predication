IMPORTANT NOTE: The Dataset we have made is a huge data set ~1 GB. So, it can be seen on below dropbox link:
https://www.dropbox.com/sh/h53v9vcpsdl9mof/AADyUJ3nez6VRDqmt_W8PaF6a?dl=0

The Diretory structure of the project is as follows:
1. data - It contains:
		data collection folder - This folder has all the data obtained from the tweets of the movies we have considered.
		results_sentimental folder - It contains the results of sentimental analysis
		MoviePerformance_ActualData.txt - It contains the actual performance of the movies according to IMDB.com
		movies_specific_stop_words.txt - It contains the stop words for all the movies.

2.Presentation - It contains the presentation of our project
3.Results - It contains the results obtained from two tasks: 1. Box Office revenue collection 2. prediction of movie performance (Hit,Flop,neutral)
4.source_code-It contains
		data_collection_sourecode - It is responsible for data collection from different social media - facebook, twitter and youtube
		kmeans - It is responsible for calculating performance of movies into hip,flop and average
		stanfordnlpdemo - It is responsible for sentimental analysis of tweets and uses stanford core NLP Library
		sentimental_svm -  It contains the sentimental analysis code we have tried for the svm
		calculateHypeFactor.py - It is responsible for calculating the hype factor
		getTweetsBeforeOneWeek.py - It is responsible for collection of tweets one bedore the movie is released.it will extract data from already extracted data.
		movie_hype_normalization.py - Normalization of the values required for the hype count.

5.Proposal_TermProject - The project proposal
6.Report_TermProject - This is the project report for the term project.


Task of all files:
1. facebook_collect.py - This is responsible of collecting the comments,posts of the particuar movie page. ypu just have to input the movie page name as shown in code.
2. jsonTOcsv.py - This is responsible to convert json data collected from the tweets to csv format.
3. tweets_collect.py - This is responsible to collect streaming data about movie tweets from twitter.
4. youtube_collect.py - This is responsible to collect data from youtube.
5. kmeans_classifier.py -  It is responsible for calculating performance of movies into hip,flop and average.
6. senti_analyzer_svm.py - This is responsible for doing setimental analysis on tweets using svm classifier.
7. NLP.java and test.java - It uses stanford Core NLP and does sentimental analysis which can classify into positive, negative and neutral
8. calculateHypeFactor.py - This script is responsible for calculating hype factor.
9.getTweetsBeforeOneWeek.py - It is responsible for collection of tweets one bedore the movie is released.it will extract data from already extracted data.
10.movie_hype_normalization.py - Normalization of the values required for the hype count.

Our system is a big system. It requires a lot of pre -processing to achieve our tasks. The sentimental analysis took a lot of time like in days to run.
So, running our system is not possible at this time.However we have provided all the input, output and source code files along with their results.
We are planning to launch website soon(probably in summer) through which our system can be run.

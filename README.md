# About
Creates a word cloud based on the frequency of the word.


# Details
There can be different approaches implemented based on the size of text:
	1. If the text size is very huge (Big data) then we can use spark for our statistical analysis. We would need EMR, HDFS, Spark etc. for doing our analysis.
	2. If the text size is not so huge then analysis in python would be sufficient. We just need python and other python libraries.

Following statistics can be taken out from the text:

	1. Word Frequency/Information retrieval: This would help us get the more frequently occurring words. This statistic can help us better understand the gist of the whole text without
	   going through the whole text. Word cloud by d3.js can give us better insights on the most common words in a text.
	2. Positive/Negative/Neutral polarity of words: Get the polarity of all the words and group them into positive and negative word groups. These groups can help
	   us better understand the overall mood of the text.

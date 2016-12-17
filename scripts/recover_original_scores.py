#!/usr/bin/python
import csv

csvfile1 = open('../datasets/movie_metadata.csv','r')
reader1 = csv.reader(csvfile1, delimiter=',', quotechar='\"')
csvfile2 = open('../datasets/movie_metadata_clean.csv','r')
reader2 = csv.reader(csvfile2, delimiter=',', quotechar='\"')
csvfile3 = open('../datasets/movie_metadata_clean_alt.csv','w')
writer = csv.writer(csvfile3)

reader1.next()
writer.writerow(reader2.next()) # header

for row1,row2 in zip(reader1,reader2):
	assert(row1[11].strip()==row2[20].strip())
	print '{} -> {}'.format(row2[27], row1[25])
	row3 = row2
	row3[27] = row1[25]
	writer.writerow(row3)
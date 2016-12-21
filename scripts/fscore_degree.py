#!/usr/bin/python
import csv

def get_reader():
	csvfile = open('../out/svm/parameters_degree.log','r')
	reader = csv.reader(csvfile, delimiter='\t', quotechar='\"')
	next(reader)
	next(reader)
	return reader

def get_writer():
	csvfile = open('../out/svm/fscore_degree.csv','w')
	writer = csv.writer(csvfile)
	writer.writerow(('f1-score','gamma','c', 'd'))
	return writer


row_precision = 4 
row_recall = 5
row_gamma = 3
row_c = 0
row_degree = 2

reader = get_reader()
writer = get_writer()
stats = []
for line in reader:
	c=float(line[row_c])
	gamma=float(line[row_gamma])
	recall=float(line[row_recall])
	degree=float(line[row_degree])
	precision=float(line[row_precision])
	fscore = 2*(precision*recall)/(precision+recall)
	stats+=[(fscore,gamma,c,degree)]

for f,g,c,d in sorted(stats, key=lambda x: x[0]):
	print('f-sorted: '+str(f))
	print('-------------------')
	writer.writerow((f,g,c,d))




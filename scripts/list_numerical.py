#!/usr/bin/python
import csv
import pprint

def get_reader():
	csvfile = open('../datasets/movie_metadata_clean_alt.csv','r')
	return csv.reader(csvfile, delimiter=',', quotechar='\"')

csvfile = open('../datasets/movie_metadata_prenumerical.csv','w')
writer = csv.writer(csvfile)
reader = get_reader()
titles =  reader.next()
ex_len = len(titles)

#Rows 
genre = 18
plot_keywords = 22

def get_plottwist(row,res={}):
	keys = row[plot_keywords].split('|')
	for key in keys:
		if key in res:
			res[key] +=1
		else:
			res[key] = 1
	return res


def get_genre(row,res={}):
	keys = row[genre].split('|')
	for key in keys:
		if key in res:
			res[key] +=1
		else:
			res[key] = 1
	return res

res = {}
for row in reader:
	plot = get_plottwist(row)
	genres = get_genre(row)

pp = pprint.PrettyPrinter(indent=4)

# Filter plots
plot = [k for k,v in plot.items() if v > 60]
genres = [k for k,v in genres.items() if v > 60]

#titles
reader = get_reader()
titles = reader.next()
[titles.append('plot_'+k) for k in plot]
[titles.append('genre_'+k) for k in genres]
print(len(plot))
print(len(genres))


writer.writerow(titles) # header
for row in reader:
	for k in plot:
		row.append(int(k in row[plot_keywords]))
	for k in genres:
		row.append(int(k in row[genre]))

	writer.writerow(row)



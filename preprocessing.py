#!/usr/bin/python
import csv

currencies = {} # currencies to usd
currencies['South Korea'] = 0.000852 # South Korean won
currencies['Turkey'] = 0.286784 # Turkish lira
currencies['Japan'] = 0.008671 # Japanese yen
currencies['Hungary'] = 0.003354 # Hungarian forint
currencies['India'] = 0.014818 # Indian rupee
currencies['Spain'] = 0.00634571 # Spanish peseta
currencies['China'] = 0.144776 # Chinese yuan
currencies['Thailand'] = 0.028032 # Thai baht

csvfile = open('movie_metadata.csv','r')
reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
csvfile = open('movie_metadata_prep.csv','w')
writer = csv.writer(csvfile)
writer.writerow(reader.next()) # header

country = 20
budget = 22
aspect_ratio = 26

def treat_budget(row):
	if row[budget] != '' and int(row[budget]) > 3e8:
		old_budget = int(row[budget])
		new_budget = int(old_budget*currencies[row[country]])
		print '{} -> {}'.format(old_budget,new_budget)
		row[budget] = new_budget

def treat_aspect_ratio(row):
	if row[aspect_ratio] != '' and float(row[aspect_ratio]) > 3:
		old_ar = float(row[aspect_ratio])
		if old_ar == 4: new_ar = 4/3.
		if old_ar == 16: new_ar = 16/9.
		print '{} -> {}'.format(old_ar,new_ar)
		row[aspect_ratio] = new_ar

for row in reader:
	treat_budget(row)
	treat_aspect_ratio(row)
	writer.writerow(row)
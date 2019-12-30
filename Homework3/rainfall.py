#!/usr/bin/env python3
class RainfallTable(object):

	def __init__(self, filename):
		self.filename = filename
		self.rainfallTable = dict()
		self.build_table()

    def build_table():
        f = open(self.filename, 'r')
    	for year in f:
        	record = make_year_list(year)
        	rainfallTable[record[0]] = record[1]
    	f.close()
    	return rainfallTable

    def make_year_list(year_line):
        tokens = year_line.split()
        year = int(tokens[0])
        rainfall = [float(x) for x in tokens[1:]]
        return (year, rainfall)


def main():
    table = RainfallTable("njrainfall.txt")
    print(table)

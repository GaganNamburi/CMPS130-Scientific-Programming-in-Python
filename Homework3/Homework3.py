import statistics

class RainfallTable:
	def __init__(self, filename):
		self.filename = filename
		self.table = dict()
		
		def make_year_list(year_line):
			tokens = year_line.split()
			year = int(tokens[0])
			#List of floats
			rainfall = [float(x) for x in tokens[1:]]
			return (year, rainfall)
		self.f = open(self.filename, "r")
		for year in self.f:
			self.record = make_year_list(year)
			self.table[self.record[0]] = self.record[1]
		self.f.close()

	def get_rainfall(self, year, month):
		"""Returns the rainfall associated with
		the given year and month. Both values
		are assumed to be integers (month given
		as 1-12, year as a four digit year).
		Raises an exception if the year/month
		combination are not found
		"""
		try:
			return self.table[year][month-1]
		except KeyError:
			print("That year/month combination was not found")
		except ValueError:
			print("That year/month combination was not found")

	def get_average_rainfall_for_month(self, month):
		"""Returns the average rainfall associated with
		he given month across all years in the table.
		Month is assumed to be n integer (1-12).
		Raises an exception if the month is not valid.
		"""
		try:
			self.all_years = [self.table[x][month-1] for x in self.table]
			return sum(self.all_years)/ len(self.all_years)
		except IndexError:
			print("The month given is not valid")

	def get_min_year(self):
		"""Returns the minimum year in the table"""
		return min(self.table.keys())

	def get_max_year(self):
		"""Returns the maximum year in the table"""
		return max(self.table.keys())

	def get_median_rainfall_for_month(self, month):
		"""Returns the median* rainfall associated with
		the given month across all years in the table.
		Month is assumed to be an integer (1-12).
		Raises an exception if month is not valid."""
		try:
			self.years = [self.table[x][month-1] for x in self.table]
			return statistics.median(self.years)
		except IndexError:
			print("The month given is not valid")

	def get_average_rainfall_for_year(self, year):
		"""Returns the average rainfall in
		the given year across all months.
		Raises exception if year is not
		in table"""
		try:
			self.all_months = [self.table[year][x] for x in range(0,12)]
			return sum(self.all_months)/ len(self.all_months)
		except KeyError:
			print("Year is not in table")

	def get_median_rainfall_for_year(self, year):
		"""Returns the median rainfall in
		the given year across all months.
		Raises exception if year is not
		in table"""
		try:
			self.months = [self.table[year][x] for x in range(0,12)]
			return statistics.median(self.months)
		except KeyError:
			print("Year is not in table")

	def get_all_by_year(self, year):
		"""Returns the rainfall values for each
		month in the given year. Raise exception
		if year is not found"""
		try:
			self.months = [self.table[year][x] for x in range(0,12)]
			yield self.months
		except KeyError:
			print("Year not found")

	def get_all_by_month(self, month):
		"""Returns the rainfall values for each
		year during the given month. Raise exception
		if month is not valid"""
		try:
			self.years = [self.table[x][month-1] for x in self.table]
			yield self.years
		except IndexError:
			print("Month not valid")

	def get_droughts(self):
		"""Returns a list of strings, representing date (month/year) ranges
		where three or more months in a row had at least 5% less rainfall than
		their historical monthly medians"""
		self.droughts = []
		for year in self.table:
			self.median = self.get_median_rainfall_for_year(year) * .95
			for month in self.table[year]:
				if month < self.median:
					self.droughts.append(month)
		return self.droughts

table = RainfallTable("njrainfall.txt")
print(table.get_rainfall(1993, 6))
print(table.get_average_rainfall_for_month(6))

for year in range(table.get_min_year(), table.get_max_year()+1) :
    print("Average rainfall in ", year, "=", table.get_average_rainfall_for_year(year))
    print("Median rainfall in ", year, "=", table.get_median_rainfall_for_year(year))
    print("===========")
    for rain in table.get_all_by_year(year):
        print(rain, end='\t')
    print("\n===========")


for month in range(1, 13) :
    print("Average rainfall in month", month, "=", table.get_average_rainfall_for_month(month))
    print("Median rainfall in month", month, "=", table.get_median_rainfall_for_month(month))
    print("===========")
    for rain in table.get_all_by_month(month):
        print(rain, end='\t')
    print("\n===========")

for d in table.get_droughts() :
    print("Drought:  ", d)

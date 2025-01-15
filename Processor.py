import pandas as pd
#creates dataframe object
raw_data = pd.read_csv("Stocks.csv")

#A dictionary of all sectors extracted from stocks data
all_sectors = ['Consumer Discretionary', 'Telecommunications', 'Basic Materials', 'Technology', 'Finance', 'Energy', 'Real Estate', 'Health Care', 'Utilities', 'Industrials', 'Miscellaneous', 'Consumer Staples']


countries = ["Canada", "United States", "United Kingdom", "France", "China", "Russia", "China"]

#A dictionary of sectors with their indexes as keys
sectors_dict = {n + 1: all_sectors[n] for n in range(len(all_sectors))}

#A function that checks if a user's input is of a valid data type
def typecheck(value, typ, function):
	if typ(value) == True:
		return value 
	else:
		print("Please enter a valid value")
		return function()
	

def enteryear():
	user_input = typecheck(input("Enter a start year to filter your data\n"), str.isdigit, enteryear)
	return int(user_input)

sectors = set()
def entersector():
	print(str(sectors_dict).removeprefix("{").removesuffix("}"))
	user_input = typecheck(input("\nSelect a sector with it's referring number\n"), str.isdigit, enteryear)
	sectors.add(sectors_dict[int(user_input)])
	reselect = input("\nEnter 'x' to select add another sector\nEnter any other key to end selection\n")
	if reselect == 'x' or reselect == 'X':
		return entersector()
	return
		

#Function calls to collect user inputs to filter data
year = enteryear()
entersector()


#filters through dataframe for data from specific countries, years, and sector
filtered_data = raw_data[
	(raw_data["Country"].isin(countries))
	& (raw_data["IPO Year"] >= year)
	& (raw_data["Sector"].isin(sectors))
]

#Sorts data in descending order, putting the top stocks at the top
sorted_data = filtered_data.sort_values(["Volume"], ascending=False)

#converts dataframe object to a csv file and exports with unique file name
sorted_data.to_csv(f"refined stocks data/{year}-present_refined_stocks_data_{'_'.join(sectors)}.csv", index=False)

print(sorted_data)
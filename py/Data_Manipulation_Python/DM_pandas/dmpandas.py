import pandas as pd
homelessness = pd.read_csv('homelessness.csv', index_col='Unnamed: 0')
def inspecting():
    # Print the head of the homelessness data
    print(homelessness.head())

    # Print information about homelessness
    print(homelessness.info())

    # Print the shape of homelessness
    print(homelessness.shape)

    # Print a description of homelessness
    print(homelessness.describe())
    
def part_data():
        # Print the values of homelessness
    print(homelessness.values)

    # Print the column index of homelessness
    print(homelessness.columns)

    # Print the row index of homelessness
    print(homelessness.index)
    
def sorting_rows():
    # Sort homelessness by individuals
    homelessness_ind = homelessness.sort_values("individuals")

    # Print the top few rows
    print(homelessness_ind.head())
    
    # Sort homelessness by descending family members
    homelessness_fam = homelessness.sort_values("family_members", ascending=False)

    # Print the top few rows
    print(homelessness_fam.head())
    
    # Sort homelessness by region, then descending family members
    homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

    # Print the top few rows
    print(homelessness_reg_fam.head())
    
    
def selecting():
    # Select the individuals column
    individuals = homelessness[["individuals"]]

    # Print the head of the result
    print(individuals.head())
    
    # Select the state and family_members columns
    state_fam = homelessness[["state", "family_members"]]

    # Print the head of the result
    print(state_fam.head())
    
    # Select only the individuals and state columns, in that order
    ind_state = homelessness[["individuals" ,"state"]]

    # Print the head of the result
    print(ind_state.head())
    
    
def subsetting():
    # Filter for rows where individuals is greater than 10000
    ind_gt_10k = homelessness[homelessness["individuals"]>10000]

    # See the result
    print(ind_gt_10k)
    
    # Filter for rows where region is Mountain
    mountain_reg = homelessness[homelessness["region"]=="Mountain"]

    # See the result
    print(mountain_reg)
    
    # Filter for rows where family_members is less than 1000 
    # and region is Pacific
    fam_lt_1k_pac = homelessness[(homelessness["family_members"]<1000) & (homelessness["region"]=="Pacific")]

    # & - and operator 

    # See the result
    print(fam_lt_1k_pac)
    
    
def subsetting2():
    # Subset for rows in South Atlantic or Mid-Atlantic regions
    south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic", "Mid-Atlantic"])]

    # .isin() method filters the input if only equals to an element of given list
    
    # See the result
    print(south_mid_atlantic)
    
    # The Mojave Desert states
    canu = ["California", "Arizona", "Nevada", "Utah"]

    # Filter for rows in the Mojave Desert states
    mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

    # See the result
    print(mojave_homelessness)
    
    
def adding_cols():
    # Add total col as sum of individuals and family_members
    homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

    # Add p_individuals col as proportion of total that are individuals
    homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

    # See the result
    print(homelessness)
    
def transforming():
    # Create indiv_per_10k col as homeless individuals per 10k state pop
    homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

    # Subset rows for indiv_per_10k greater than 20
    high_homelessness = homelessness[homelessness["indiv_per_10k"]>20]

    # Sort high_homelessness by descending indiv_per_10k
    high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

    # From high_homelessness_srt, select the state and indiv_per_10k cols
    result = high_homelessness_srt[["state", "indiv_per_10k"]]

    # See the result
    print(result)
    
sales = pd.read_csv('sales_subset.csv', index_col='Unnamed: 0')

# .median() , .mode()
# .min() , .max()
# .var() , .std()
# .sum()
# .quantile()
# The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making your aggregations super-efficient. For example:
# df['column'].agg(function)

# .cumsum()
# .cummax()
# .cummin()
# .cumprod()

def aggregating():
    # Print the head of the sales DataFrame
    print(sales.head())

    # Print the info about the sales DataFrame
    print(sales.info())

    # Print the mean of weekly_sales
    print(sales["weekly_sales"].mean())

    # Print the median of weekly_sales
    print(sales["weekly_sales"].median())
    
    # Print the maximum of the date column
    print(sales["date"].max())

    # Print the minimum of the date column
    print(sales["date"].min())

# Import NumPy and create custom IQR function
import numpy as np
    # A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
  
def aggregating1():  
    # Print IQR of the temperature_c column
    print(sales["temperature_c"].agg(iqr))
    
    # Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
    print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
    
    # Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
    print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

def cums():
    # Sort sales_1_1 by date
    sales_1_1 = sales.sort_values("date")

    # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
    sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

    # Get the cumulative max of weekly_sales, add as cum_max_sales col
    sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

    # See the columns you calculated
    print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
    
def dropduplicates():
    # Drop duplicate store/type combinations
    store_types = sales.drop_duplicates(subset=["store", "type"])
    print(store_types.head())

    # Drop duplicate store/department combinations
    store_depts = sales.drop_duplicates(subset=["store", "department"])
    print(store_depts.head())

    # Subset the rows where is_holiday is True and drop duplicate dates
    holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

    # Print date col of holiday_dates
    print(holiday_dates["date"])

def valuecounts():
    store_types = sales.drop_duplicates(subset=["store", "type"])
    store_depts = sales.drop_duplicates(subset=["store", "department"])
    
    # Count the number of stores of each type
    store_counts = store_types["type"].value_counts()
    print(store_counts)

    # Get the proportion of stores of each type
    store_props = store_types["type"].value_counts(normalize=True)
    print(store_props)

    # Count the number of each department number and sort
    dept_counts_sorted = store_depts["department"].value_counts(sort=True)
    print(dept_counts_sorted)

    # Get the proportion of departments of each number and sort
    dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
    print(dept_props_sorted)
    
def group_by1():
    # Calc total weekly sales
    sales_all = sales["weekly_sales"].sum()

    # Subset for type A stores, calc total weekly sales
    sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

    # Subset for type B stores, calc total weekly sales
    sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

    # Subset for type C stores, calc total weekly sales
    sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

    # Get proportion for each type
    sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
    print(sales_propn_by_type)
    
def group_by2():
    # Group by type; calc total weekly sales
    sales_by_type = sales.groupby("type")["weekly_sales"].sum()

    # Get proportion for each type
    sales_propn_by_type = sales_by_type / sum(sales["weekly_sales"])
    print(sales_propn_by_type)
    
    # From previous step
    sales_by_type = sales.groupby("type")["weekly_sales"].sum()

    # Group by type and is_holiday; calc total weekly sales
    sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
    print(sales_by_type_is_holiday)
    
def mult_groupby():
    # For each store type, aggregate weekly_sales: get min, max, mean, and median
    sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

    # Print sales_stats
    print(sales_stats)

    # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
    unemp_fuel_stats = sales.groupby("type")["unemployment", "fuel_price_usd_per_l"].agg([np.min, np.max, np.mean, np.median])

    # Print unemp_fuel_stats
    print(unemp_fuel_stats)
    
def groupping_by_pivot():
    # Pivot for mean weekly_sales for each store type
    mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

    # Print mean_sales_by_type
    print(mean_sales_by_type)
    


    # Pivot for mean and median weekly_sales for each store type
    mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])

    # Print mean_med_sales_by_type
    print(mean_med_sales_by_type)
    
def pivot_two_cols():
    # Pivot for mean weekly_sales by store type and holiday 
    mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

    # Print mean_sales_by_type_holiday
    print(mean_sales_by_type_holiday)
    
def fill_missings():
    # Print mean weekly_sales by department and type; fill missing values with 0
    print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))
    
    # Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
    print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))
    

temperatures = pd.read_csv('temperatures.csv', index_col='Unnamed: 0')

def setindex():
    # Look at temperatures
    print(temperatures.head())

    # Set the index of temperatures to city
    temperatures_ind = temperatures.set_index("city")

    # Look at temperatures_ind
    print(temperatures_ind)

    # Reset the temperatures_ind index, keeping its contents
    print(temperatures_ind.reset_index())

    # Reset the temperatures_ind index, dropping its contents
    print(temperatures_ind.reset_index(drop=True))
    

def subsetting_loc():
    # Make a list of cities to subset on
    cities = ["Moscow", "Saint Petersburg"]
    # Set the index of temperatures to city
    temperatures_ind = temperatures.set_index("city")
    # Subset temperatures using square brackets
    print(temperatures[temperatures["city"].isin(cities)])

    # Subset temperatures_ind using .loc[]
    print(temperatures_ind.loc[cities])
    
def subsetting_mult():
    # Index temperatures by country & city
    temperatures_ind = temperatures.set_index(["country", "city"])

    # List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
    rows_to_keep = [("Brazil","Rio De Janeiro"), ("Pakistan","Lahore")]

    # Subset for rows to keep
    print(temperatures_ind.loc[rows_to_keep])

temperatures_ind = temperatures.set_index(["country", "city"])
def sorting_index():
    # Sort temperatures_ind by index values
    print(temperatures_ind.sort_index())

    # Sort temperatures_ind by index values at the city level
    print(temperatures_ind.sort_index(level="city"))

    # Sort temperatures_ind by country then descending city
    print(temperatures_ind.sort_index(level=["country","city"], ascending=[True, False]))

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()    
def slicing():

    # Subset rows from Pakistan to Russia
    print(temperatures_srt.loc["Pakistan":"Russia"])

    # Try to subset rows from Lahore to Moscow
    print(temperatures_srt.loc["Lahore": "Moscow"])

    # Subset rows from Pakistan, Lahore to Russia, Moscow
    print(temperatures_srt.loc[("Pakistan","Lahore"): ("Russia", "Moscow")])
    

def slicing1():
    # Subset rows from India, Hyderabad to Iraq, Baghdad
    print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad")])

    # Subset columns from date to avg_temp_c
    print(temperatures_srt.loc[:, "date": "avg_temp_c"])

    # Subset in both directions at once
    print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad"), "date": "avg_temp_c"])
    
def slicing2():
    # Use Boolean conditions to subset temperatures for rows in 2010 and 2011
    temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
    print(temperatures_bool)

    # Set date as the index and sort the index
    temperatures_ind = temperatures.set_index("date").sort_index()

    # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
    print(temperatures_ind.loc["2010": "2011"])

    # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
    print(temperatures_ind.loc["2010-08":"2011-02"])
    
def slicing3():
    # Get 23rd row, 2nd column (index 22, 1)
    print(temperatures.iloc[22, 1])

    # Use slicing to get the first 5 rows
    print(temperatures.iloc[:5])

    # Use slicing to get columns 3 to 4
    print(temperatures.iloc[:, 2:4])

    # Use slicing in both directions at once
    print(temperatures.iloc[:5, 2:4])
    
def pivoting():
    # Add a year column to temperatures
    temperatures["year"]=temperatures["date"].dt.year

    # Pivot avg_temp_c by country and city vs year
    temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"], columns="year")

    # See the result
    print(temp_by_country_city_vs_year)
    
def subsetting_pivot():
    temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"], columns="year")
    # Subset for Egypt to India
    temp_by_country_city_vs_year.loc["Egypt": "India"]

    # Subset for Egypt, Cairo to India, Delhi
    temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi")]

    # Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
    temp_by_country_city_vs_year.loc[("Egypt", "Cairo"): ("India", "Delhi"), "2005":"2010"]
    
def filtering_pivot():
    temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"], columns="year")
    # Get the worldwide mean temp by year
    mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")

    # Filter for the year that had the highest mean temp
    print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

    # Get the mean temp by city
    mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

    # Filter for the city that had the lowest mean temp
    print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
    
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt 
import pickle as pkl
# visualizing
with open("avoplotto.pkl", "rb") as f:
    object = pkl.load(f)
    

avocados = pd.DataFrame(object)

def make_plot():
    # Look at the first few rows of data
    print(avocados.head())

    # Get the total number of avocados sold of each size
    nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

    # Create a bar plot of the number of avocados sold by size
    nb_sold_by_size.plot(x="size", kind="bar")

    # Show the plot
    plt.show()
    
def make_plot1():
    # Get the total number of avocados sold on each date
    nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

    # Create a line plot of the number of avocados sold by date
    nb_sold_by_date.plot(x="date", kind="line")

    # Show the plot
    plt.show()
    
def scatterplot():
    # Scatter plot of avg_price vs. nb_sold with title
    avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

    # Show the plot
    plt.show()
    
def histogram1():
    # Histogram of conventional avg_price 
    avocados[avocados["type"]=="conventional"]["avg_price"].hist()

    # Histogram of organic avg_price
    avocados[avocados["type"]=="organic"]["avg_price"].hist()

    # Add a legend
    plt.legend(["conventional" , "organic"])

    # Show the plot
    plt.show()
    
def histogram2():
    # Modify bins to 20
    avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

    # Modify bins to 20
    avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

    # Add a legend
    plt.legend(["conventional", "organic"])

    # Show the plot
    plt.show()
    
# missing values
def missing_graph():
    # Check individual values for missing values
    print(avocados.isna())

    # Check each column for missing values
    print(avocados.isna().any())

    # Bar plot of missing values by variable
    avocados.isna().sum().plot(kind="bar")

    # Show plot
    plt.show()
    
def drop_missing():
    # Remove rows with missing values
    avocados_complete = avocados.dropna()

    # Check if any columns contain missing values
    print(avocados_complete.isna().any().sum())
    
def fill_missing():
    # From previous step
    cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
    avocados[cols_with_missing].hist()
    plt.show()

    # Fill in missing values with 0
    avocados_filled = avocados.fillna(0)

    # Create histograms of the filled columns
    avocados_filled[cols_with_missing].hist()

    # Show the plot
    plt.show()
    
def create_df():
    # Create a list of dictionaries with new data
    avocados_list = [
        {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
        {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
    ]

    # Convert list into DataFrame
    avocados_2019 = pd.DataFrame(avocados_list)

    # Print the new DataFrame
    print(avocados_2019)

def create_df1():
    # Create a dictionary of lists with new data
    avocados_dict = {
    "date": ["2019-11-17", "2019-12-01"],
    "small_sold": [10859987,	9291631],
    "large_sold": [7674135, 6238096]
    }

    # Convert dictionary into DataFrame
    avocados_2019 = pd.DataFrame(avocados_dict)

    # Print the new DataFrame
    print(avocados_2019)
    

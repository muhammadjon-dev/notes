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
    

import matplotlib.pyplot as plt 
import numpy as np
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005, 60.916, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678, 73.952, 59.443000000000005, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777,63.062, 74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]

gdp_cap = [974.5803384, 5937.029525999999, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995, 36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885, 4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000003, 6025.374752000001, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000001, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999999, 1201.637154, 3548.3308460000003, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.880262000001, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.7722710000003, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999999, 2013.977305, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000001, 1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561000001, 47143.17964, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.095407, 2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684, 1107.482182, 7458.396326999999, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]


def matplotlib_ex():

    plt.hist(life_exp)
    plt.show()
    plt.clf()

    plt.hist(life_exp, bins=5)

    # Show and clean up plot
    plt.show()
    plt.clf()

    # Build histogram with 20 bins
    plt.hist(life_exp, bins=20)

    # Show and clean up again
    plt.show()
    plt.clf()

    # Histogram of life_exp, 15 bins
    plt.hist(life_exp, bins=15)

    # Show and clear plot
    plt.show()
    plt.clf()

    # Histogram of life_exp1950, 15 bins
    plt.hist(life_exp, bins=15)

    # Show and clear plot again
    plt.show()
    plt.clf()

    # Basic scatter plot, log scale
    plt.scatter(gdp_cap, life_exp)
    plt.xscale('log') 

    # Strings
    xlab = 'GDP per Capita [in USD]'
    ylab = 'Life Expectancy [in years]'
    title = 'World Development in 2007'

    # Add axis labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    # Add title
    plt.title(title)

    # After customizing, display the plot
    plt.show()




    # 2

    # Scatter plot
    plt.scatter(gdp_cap, life_exp)

    # Previous customizations
    plt.xscale('log') 
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')

    # Definition of tick_val and tick_lab
    tick_val = [1000, 10000, 100000]
    tick_lab = ['1k', '10k', '100k']

    # Adapt the ticks on the x-axis
    plt.xticks(tick_val, tick_lab)

    # After customizing, display the plot
    plt.show()


    # 3

    pop = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226, 8.078314, 9.119152, 4.552198, 1.639131, 190.010647, 7.322858, 14.326203, 8.390505, 14.131858, 17.696293, 33.390141, 4.369038, 10.238807, 16.284741, 1318.683096, 44.22755, 0.71096, 64.606759, 3.80061, 4.133884, 18.013409, 4.493312, 11.416987, 10.228744, 5.46812, 0.496374, 9.319622, 13.75568, 80.264543, 6.939688, 0.551201, 4.906585, 76.511887, 5.23846, 61.083916, 1.454867, 1.688359, 82.400996, 22.873338, 10.70629, 12.572928, 9.947814, 1.472041, 8.502814, 7.483763, 6.980412, 9.956108, 0.301931, 1110.396331, 223.547, 69.45357, 27.499638, 4.109086, 6.426679, 58.147733, 2.780132, 127.467972, 6.053193, 35.610177, 23.301725, 49.04479, 2.505559, 3.921278, 2.012649, 3.193942, 6.036914, 19.167654, 13.327079, 24.821286, 12.031795, 3.270065, 1.250882, 108.700891, 2.874127, 0.684736, 33.757175, 19.951656, 47.76198, 2.05508, 28.90179, 16.570613, 4.115771, 5.675356, 12.894865, 135.031164, 4.627926, 3.204897, 169.270617, 3.242173, 6.667147, 28.674757, 91.077287, 38.518241, 10.642836, 3.942491, 0.798094, 22.276056, 8.860588, 0.199579, 27.601038, 12.267493, 10.150265, 6.144562, 4.553009, 5.447502, 2.009245, 9.118773, 43.997828, 40.448191, 20.378239, 42.292929, 1.133066, 9.031088, 7.554661, 19.314747, 23.174294, 38.13964, 65.068149, 5.701579, 1.056608, 10.276158, 71.158647, 29.170398, 60.776238, 301.139947, 3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143] 


    # Store pop as a numpy array: np_pop
    np_pop = np.array(pop)

    # Double np_pop
    np_pop = np_pop*2

    # Update: set s argument to np_pop
    plt.scatter(gdp_cap, life_exp, s = np_pop)

    # Previous customizations
    plt.xscale('log') 
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

    # Display the plot
    plt.show()

    col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue'] 

    # Specify c and alpha inside plt.scatter()
    plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

    # Previous customizations
    plt.xscale('log') 
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000,10000,100000], ['1k','10k','100k'])

    # Show the plot
    plt.show()


    # 5
    # Scatter plot
    plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

    # Previous customizations
    plt.xscale('log') 
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000,10000,100000], ['1k','10k','100k'])

    # Additional customizations
    plt.text(1550, 71, 'India')
    plt.text(5700, 80, 'China')

    # Add grid() call
    plt.grid(True)

    # Show the plot
    plt.show()



# Dictionaries & Pandas

def part1():
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

    # Print out the keys in europe
    print(europe.keys())

    # Print out value that belongs to key 'norway'
    print(europe['norway'])

def part2():
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

    # Add italy to europe
    europe['italy']='rome'

    # Print out italy in europe
    print('italy' in europe)

    # Add poland to europe
    europe['poland']='warsaw'

    # Print europe
    print(europe)
    
def part2_1():
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
            'australia':'vienna' }

    # Update capital of germany
    europe['germany']='berlin'

    # Remove australia
    del(europe['australia'])

    # Print europe
    print(europe)
    
def dictionariception():
    # Dictionary of dictionaries
    europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
            'france': { 'capital':'paris', 'population':66.03 },
            'germany': { 'capital':'berlin', 'population':80.62 },
            'norway': { 'capital':'oslo', 'population':5.084 } }


    # Print out the capital of France
    print(europe['france']['capital'])

    # Create sub-dictionary data
    data = {'capital':'rome', 'population':59.83}

    # Add data to europe under key 'italy'
    europe['italy']=data

    # Print europe
    print(europe)


# Pandas
# Import pandas as pd
import pandas as pd
def pandas1():
    # Pre-defined lists
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]



    # Create dictionary my_dict with three key:value pairs: my_dict
    my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

    # Build a DataFrame cars from my_dict: cars
    cars = pd.DataFrame(my_dict)

    # Print cars
    print(cars)
    
def pandas2():
    # Build cars DataFrame
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]
    cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
    cars = pd.DataFrame(cars_dict)
    print(cars)

    # Definition of row_labels
    row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

    # Specify row labels of cars
    cars.index=row_labels

    # Print cars again
    print(cars)

def pandas3():
    # Import the cars.csv data: cars
    cars = pd.read_csv("cars.csv")

    # Print out cars
    print(cars)
    


def pandas4():
    # Fix import by including index_col
    cars = pd.read_csv('cars.csv', index_col=0)

    # Print out cars
    print(cars)

def pandas5():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out country column as Pandas Series
    print(cars['country'])

    # Print out country column as Pandas DataFrame
    print(cars[['country']])

    # Print out DataFrame with country and drives_right columns
    print(cars[['country', 'drives_right']])
    
def pandas6():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out first 3 observations
    print(cars[:3])

    # Print out fourth, fifth and sixth observation
    print(cars[3:6])
    
def pandas7():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out observation for Japan
    print(cars.loc['JPN'])

    # Print out observations for Australia and Egypt
    print(cars.loc[['AUS', 'EG']])
    
def pandas8():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out drives_right value of Morocco
    print(cars.loc['MOR', 'drives_right'])

    # Print sub-DataFrame
    print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

def pandas9():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out drives_right column as Series
    print(cars.iloc[:, [2]])

    # Print out drives_right column as DataFrame
    print(cars.iloc[:, 2])

    # Print out cars_per_cap and drives_right as DataFrame
    print(cars.iloc[:, [0, 2]])


# chapter3

# Logic, Control Flow and Filtering



def compare_arrays():
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    # my_house greater than or equal to 18
    print(my_house>=18)

    # my_house less than your_house
    print(my_house<your_house)
    
def logical_oper():
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    # my_house greater than 18.5 or smaller than 10
    print(np.logical_or(my_house>18.5, my_house<10))

    # Both my_house and your_house smaller than 11
    print(np.logical_and(my_house<11, your_house<11))
    
def dr():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Extract drives_right column as Series: dr
    dr = cars['drives_right']

    # Use dr to subset cars: sel
    sel = cars[dr]

    # Print sel
    print(sel)
    
def cpc():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Create car_maniac: observations that have a cars_per_cap over 500
    cpc = cars['cars_per_cap']
    many_cars = cpc>500

    car_maniac = cars[many_cars]

    # Print car_maniac
    print(car_maniac)
    

def cpc1():
    cars = pd.read_csv('cars.csv', index_col = 0)
    # Create medium: observations with cars_per_cap between 100 and 500

    cpc = cars['cars_per_cap']
    between = np.logical_and(cpc > 100, cpc < 500)
    medium = cars[between]


    # Print medium
    print(medium)
    
def for_loop():
    # areas list
    areas = [11.25, 18.0, 20.0, 10.75, 9.50]

    # Change for loop to use enumerate() and update print()
    for index, area in enumerate(areas) :
        print("room " + str(index)+": "+str(area))
        
def loop_dict():
    # Definition of dictionary
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
            'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
            
    # Iterate over europe
    for k, v in europe.items():
        print("the capital of " + k + " is " + v)
        
def loop_nparray():
    # For loop over np_height
    np_life = np.array(life_exp)
    np_gdp = np.array(gdp_cap)
    for i in np.nditer(np_life):
        print(str(i)+" life exp")

    # For loop over np_baseball
    for i in np.nditer(np_gdp):
        print(i)
        
def loop_pandas():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Iterate over rows of cars
    for lab, row in cars.iterrows():
        print(lab)
        print(row)
    
        
def loop_pandas1():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Adapt for loop
    for lab, row in cars.iterrows() :
        print(lab+ ": " + str(row['cars_per_cap']))

def loop_pandas2():
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Code for loop that adds COUNTRY column
    for l, r in cars.iterrows():
        cars.loc[l, 'COUNTRY'] = cars.loc[l, 'country'].upper()


    # Print cars
    print(cars)

    cars['COUNTRY'] = cars['country'].apply(str.upper)
    
# case study

def rand_seed():
    # Import numpy as np
    # import numpy as np

    # Set the seed
    np.random.seed(123)

    # Generate and print random float
    print(np.random.rand())
    
def rand_int():
    np.random.seed(123)

    # Use randint() to simulate a dice
    print(np.random.randint(1, 7))

    # Use randint() again
    print(np.random.randint(1,7))
    
def dice():
    # NumPy is imported, seed is set
    np.random.seed(123)
    # Starting step
    step = 50

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Finish the control construct
    if dice <= 2 :
        step = step - 1
    elif dice <=5 :
        step+=1
    else :
        step = step + np.random.randint(1,7)

    # Print out dice and step
    print(dice)
    print(step)


def random_walk():
    # NumPy is imported, seed is set
    np.random.seed(123)
    # Initialize random_walk
    random_walk = [0]

    # Complete the ___
    for x in range(100) :
        # Set step: last element in random_walk
        step = random_walk[x]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            step = max(step - 1, 0)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # append next_step to random_walk
        random_walk.append(step)

    # Print random_walk
    print(random_walk)
    


def visualize_walk():
        # NumPy is imported, seed is set
    np.random.seed(123)
    # Initialization
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        random_walk.append(step)

    # Import matplotlib.pyplot as plt
    # import matplotlib.pyplot as plt

    # Plot random_walk
    plt.plot(random_walk)

    # Show the plot
    plt.show()
    
def all_walk():
        # numpy and matplotlib imported, seed set.
    np.random.seed(123)
    # initialize and populate all_walks
    all_walks = []
    for i in range(5) :
        random_walk = [0]
        for x in range(100) :
            step = random_walk[-1]
            dice = np.random.randint(1,7)
            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1,7)
            random_walk.append(step)
        all_walks.append(random_walk)

    # Convert all_walks to NumPy array: np_aw
    np_aw = np.array(all_walks)

    # Plot np_aw and show
    plt.plot(np_aw)
    plt.show()

    # Clear the figure
    plt.clf()

    # Transpose np_aw: np_aw_t
    np_aw_t = np.transpose(np_aw)

    # Plot np_aw_t and show
    plt.plot(np_aw_t)
    plt.show()
all_walk()
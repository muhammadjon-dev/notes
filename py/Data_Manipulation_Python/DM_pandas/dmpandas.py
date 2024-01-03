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
    
inspecting()
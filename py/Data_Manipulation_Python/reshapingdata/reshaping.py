import pandas as pd
fifa_players = pd.read_csv('players_20.csv')

def flipping():
    fifa_transpose = fifa_players.set_index('name')[['height', 'weight']]
    
    print(fifa_transpose)
    
    # Change the DataFrame so rows become columns and vice versa
    fifa_transpose = fifa_players.set_index('name')[['height', 'weight']].transpose()

    # Print fifa_transpose
    print(fifa_transpose)
    
    
    fifa_transpose = fifa_players.set_index('name')[['height', 'weight']].transpose().transpose()

    # Print fifa_transpose
    print(fifa_transpose)

def pivoting1():
    # Pivot fifa_players to get overall scores indexed by name and identified by movement
    fifa_overall = fifa_players.pivot(index="name", columns="movement", values="overall")

    # Print fifa_overall
    print(fifa_overall)
    
def pivoting2():
    # Pivot fifa_players to get attacking scores indexed by name and identified by movement
    fifa_attacking = fifa_players.pivot(index="name", columns="movement", values="attacking")

    # Print fifa_attacking
    print(fifa_attacking)

def pivotting3():
    # Use the pivot method to get overall scores indexed by movement and identified by name
    fifa_names = fifa_players.pivot(index="movement", columns="name", values="overall")

    # Print fifa_names
    print(fifa_names)
    
def pivotting3():
    # Pivot fifa_players to get overall and attacking scores indexed by name and identified by movement
    fifa_over_attack = fifa_players.pivot(index="name", 
                                        columns="movement", 
                                        values=["overall", "attacking"])

    # Print fifa_over_attack
    print(fifa_over_attack)
    
    # Use pivot method to get all the scores index by name and identified by movement
    fifa_all = fifa_players.pivot(index="name", columns="movement")

    # Print fifa_over_attack
    print(fifa_all)
    
def dropping_dups():
    # Drop the fifth row to delete all repeated rows
    fifa_no_rep = fifa_players.drop(4, axis=0)

    # Pivot fifa players to get all scores by name and movement
    fifa_pivot = fifa_no_rep.pivot(index="name", columns="movement") 

    # Print fifa_pivot
    print(fifa_pivot)  
    
def pivot_table1():
    # Discard the fifth row to delete all repeated rows
    fifa_drop = fifa_players.drop(4, axis=0)

    # Use pivot method to get all scores by name and movement
    fifa_pivot = fifa_drop.pivot(index="name", columns="movement") 

    # Print fifa_pivot
    print(fifa_pivot)  

    # Use pivot table to get all scores by name and movement
    fifa_pivot_table = fifa_players.pivot_table(index="name", 
                                        columns="movement", 
                                        aggfunc="mean")
    # Print fifa_pivot_table
    print(fifa_pivot_table)
    
def pivot_table2():
    # Use pivot table to display mean age of players by club and nationality 
    mean_age_fifa = fifa_players.pivot_table(index="nationality", 
                                    columns="club", 
                                    values="age", 
                                    aggfunc="mean")

    # Print mean_age_fifa
    print(mean_age_fifa)
    
def pivot_table3():
    # Use pivot table to display max height of any player by club and nationality
    tall_players_fifa = fifa_players.pivot_table(index="nationality", 
                                        columns="club", 
                                        values="height", 
                                        aggfunc="max")

    # Print tall_players_fifa
    print(tall_players_fifa)
    
def pivot_table4():
    # Use pivot table to show the count of players by club and nationality and the total count
    players_country = fifa_players.pivot_table(index="nationality", 
                                        columns="club", 
                                        values="name", 
                                        aggfunc="count", 
                                        margins=True)

    # Print players_country
    print(players_country)
    
def pivot_table5():
    # Set the argument to get the maximum for each row and column
    fifa_mean = fifa_players.pivot_table(index=['nationality', 'club'], 
                                        columns='year', 
                                        aggfunc='max', 
                                        margins=True)

    # Print fifa_mean
    print(fifa_mean)
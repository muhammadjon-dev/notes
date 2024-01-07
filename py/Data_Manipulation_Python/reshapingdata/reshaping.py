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
    
# wide to long transformation
# using .melt(id_vars= , value_vars= , var_name= , value_name= )
books_gothic = pd.read_csv('books.csv')

def melting1():
    # Melt books_gothic using the title column as identifier 
    gothic_melted = books_gothic.melt(id_vars="title")

    # Print gothic_melted
    print(gothic_melted)

    # Melt books_gothic using the title, authors, and publisher columns as identifier
    gothic_melted_new = books_gothic.melt(id_vars=["title", "authors", "publisher"])

    # Print gothic_melted_new
    print(gothic_melted_new)
    
def melting2():
    # Melt publisher column using title and authors as identifiers
    publisher_melted = books_gothic.melt(id_vars=["title", "authors"], 
                                        value_vars="publisher")

    # Print publisher_melted
    print(publisher_melted)

    # Melt rating and rating_count columns using the title as identifier
    rating_melted = books_gothic.melt(id_vars="title", 
                                    value_vars=["rating", "rating_count"])

    # Print rating_melted
    print(rating_melted)
    
    # Melt rating and rating_count columns using title and authors as identifier
    books_melted = books_gothic.melt(id_vars=["title", "authors"], 
                                    value_vars=["rating", "rating_count"])

    # Print books_melted
    print(books_melted)
    
def melting3():
    # Melt the rating and rating_count using title, authors and publisher as identifiers
    books_ratings = books_gothic.melt(id_vars=["title", "authors", "publisher"], 
                                    value_vars=["rating", "rating_count"])

    # Print books_ratings
    print(books_ratings)
    
    # Assign the name feature to the new variable column
    books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], 
                                    value_vars=['rating', 'rating_count'], 
                                    var_name='feature')

    # Print books_ratings
    print(books_ratings)
    
    # Assign the name number to the new column containing the values
    books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], 
                                    value_vars=['rating', 'rating_count'], 
                                    var_name='feature', 
                                    value_name='number')

    # Print books_ratings
    print(books_ratings)
    
# using pd.wide_to_long(df_name, stubnames= , i= , j= , sep= )
    
def wide_to_long1():
    # Reshape wide to long using title as index and version as new name, and extracting isbn prefix 
    isbn_long = pd.wide_to_long(books_gothic, 
                        stubnames="isbn", 
                        i="title", 
                        j="version")

    # Print isbn_long
    print(isbn_long)
    
    # Reshape wide to long using title and authors as index and version as new name, and prefix as wide column prefix
    prefix_long = pd.wide_to_long(books_gothic, 
                        stubnames="prefix", 
                        i=["title", "authors"], 
                        j="version")

    # Print prefix_long
    print(prefix_long)
    
def wide_to_long2():
    # Specify that wide columns have a suffix containing words
    the_code_long = pd.wide_to_long(books_gothic, 
                                    stubnames=['language', 'publisher'], 
                                    i=['author', 'title'], 
                                    j='code', 
                                    sep='_', 
                                    suffix='\w+')

    # Print the_code_long
    print(the_code_long)
    
    # Modify books_hunger by resetting the index without dropping it
    books_gothic.reset_index(drop=False, inplace=True)

    # Reshape using title and language as index, feature as new name, publication and page as prefix separated by space and ending in a word
    publication_features = pd.wide_to_long(books_gothic, 
                                        stubnames=["publication", "page"], 
                                        i=["title", "language"], 
                                        j="feature", 
                                        sep=" ", 
                                        suffix="\w+")

    # Print publication_features
    print(publication_features)
    
# splitting columns (splittings strings)
# column.str.split('sep')
# ex: books['title'].str.split(":").str.get(0)
# books['title'].str.split(":", expand=True)
# books[['main_title','subtitle']] = books['title'].str.split(":", expand=True)
# books.drop('title', axis=1, inplace=True)

books_dys = pd.read_csv('bookdys.csv', index_col="title")
author_list = ['Ray Bradbury', 'George Orwell', 'Aldous Huxley']
def splitting1():   
    # Get the first element after splitting the index of books_dys
    books_dys.index = books_dys.index.str.split('-').str.get(0)

    # Print books_dys
    print(books_dys)

# concanating columns
# column.str.cat(col_or_list, sep='sep')

def concanating():
    splitting1()
    # Split by the hyphen the index of books_dys
    books_dys.index = books_dys.index.str.split('-').str.get(0)

    # Concatenate the index with the list author_list separated by a hyphen
    books_dys.index = books_dys.index.str.cat(author_list, sep='-')

    # Print books_dys
    print(books_dys)
    
hp_books = pd.read_csv('hp_books.csv', index_col='Unnamed: 0')

def all_in_one():
    # Concatenate the title and subtitle separated by "and" surrounded by spaces
    hp_books['full_title'] = hp_books['title'].str.cat(hp_books['subtitle'], sep =" and ") 

    # Split the authors into writer and illustrator columns
    hp_books[['writer', 'illustrator']] = hp_books['authors'].str.split('/', expand=True)

    # Melt goodreads and amazon columns into a single column
    hp_melt = hp_books.melt(id_vars=['full_title', 'writer'], 
                            var_name="source", 
                            value_vars=["goodreads", "amazon"], 
                            value_name="rating")

    # Print hp_melt
    print(hp_melt)
    
books_sh = pd.read_csv('book_sh.csv', index_col='Unnamed: 0')

def all_in_one2():
    # Split main_title by a colon and assign it to two columns named title and subtitle 
    books_sh[['title', 'subtitle']] = books_sh['main_title'].str.split(':', expand=True)

    # Split version by a space and assign the second element to the column named volume 
    books_sh['volume'] = books_sh['version'].str.split(' ').str.get(1)

    # Drop the main_title and version columns modifying books_sh
    books_sh.drop(['main_title', 'version'], axis=1, inplace=True)

    # Reshape using title, subtitle and volume as index, name feature the new variable from columns starting with number, separated by undescore and ending in words 
    sh_long = pd.wide_to_long(books_sh, stubnames=['number'], i=['title', 'subtitle', 'volume'], 
                    j="feature", sep="_", suffix="\w+")

    # Print sh_long 
    print(sh_long)
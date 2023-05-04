import csv
# from models import Pokemon, PokemonStats

def uploadCSVFileToPokemonDatabase(file, db):
    # extract data from file
    fileContent = file.file.read().decode("utf-8")
    
    # convert data to rows using csv module. Its a built in module in python
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
  
    # skip the first row as it contains the column names
    next(rows)

    # iterate over the rows and add them to the database
    for row in rows:
        # uncomment the line below and see the output in terminal it should show you the data in each row (list of rows)
        # print(row)

        # add the row to the database. Remember the sequence of the data in the row matters
        # we will create a bulk insert to avoid performance issue and also to avoid multiple commits
        # on the first iteration of the loop
        # row[0] means first row first column cell. We skipped the first row as it contains the column names
        # row[1] means first row second column cell so on and so forth
        # on next iteration of the loop row[0] will be second row first column cell and so on and so forth
        pokemon = Pokemon(classification=row[1], name=row[3], type1=row[5], type2=row[6], generation=row[7])
        # here we are adding the pokemon object to the database session and not to the database itself
        db.add(pokemon)
    
    # commit the changes to the database which will insert the data into the database 
    db.commit()
    # check the result in the database using pgadmin

def uploadCSVFileToPokemonStatsDatabase(file, db):
    # the process is similar to the above function
     # extract data from file
    fileContent = file.file.read().decode("utf-8")
    
    # convert data to rows using csv module. Its a built in module in python
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
  
    # skip the first row as it contains the column names
    next(rows)

     # iterate over the rows and add them to the database
    for row in rows:
        # uncomment the line below and see the output in terminal it should show you the data in each row (list of rows)
        # print(row)

        # add the row to the database. Remember the sequence of the data in the row matters
        # we will create a bulk insert to avoid performance issue and also to avoid multiple commits
        # on the first iteration of the loop
        # row[0] means first row first column cell. We skipped the first row as it contains the column names
        # row[1] means first row second column cell so on and so forth
        # on next iteration of the loop row[0] will be second row first column cell and so on and so forth
        # on some rows, there are missing values for height and weight. we need to make sure to handle these edge cases as well
        # we are using the if condition to check if the value is present or not. If it is present then we are using it else we are using None
        # To accepts None values, we need to make sure that the column in the database is nullable
        # I have made the height_m and weight_kg columns nullable in the models.py and also changed their data type to Float
        # To migrate a new table with nullable columns, we need to drop the table and then create it again
        # To drop the table, we need to go to pgadmin and drop the table manually by right clicking on the table and selecting Delete/Drop

        pokemonStats = PokemonStats(pokemon_id=row[0], height_m=row[26] if row[26] else None, weight_kg=row[31] if row[31] else None, attack=row[19])
        # here we are adding the pokemon object to the database session and not to the database itself
        db.add(pokemonStats)
    
    # commit the changes to the database which will insert the data into the database 
    db.commit()
    # check the result in the database using pgadmin
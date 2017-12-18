# retailrocket
Steps For Execution:

Give absolute path of the directory containing config.json in the config.json file

1. Load the data into the SQL database.
    1.1 Install MySQL if it does not exists.
    1.2 Enter MySQL config information in config.json for keys mysql_user and mysql_password
    1.3 Run import_sql.py from ./Mindstix/ using the command :
            python db/import_sql.py
    This should create a db and load the csv files into it.

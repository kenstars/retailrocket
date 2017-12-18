# retailrocket
Steps For Execution:

Give absolute path of the directory containing config.json in the config.json file

1. Load the data into the SQL database.
    1.1 Install MySQL if it does not exists.
    1.2 Enter MySQL config information in config.json for keys mysql_user and mysql_password
    1.3 You will need to install MySQLDB python package and dependencies:
        Ubuntu 14.04:
            1. sudo apt-get install python-pip python-dev libmysqlclient-dev
            2. pip install MySQL-python
    1.4 Run import_sql.py from ./Mindstix/ using the command :
            python db/import_sql.py
    This should create a db and load the csv files into it.
    This will take a significant amount of time to load.
    Have patience.
    1.5 Open mysql and check for the data being correctly dumped
            select count(*) from item_properties;
                +----------+
                | count(*) |
                +----------+
                | 20275904 |
                +----------+
            1 row in set (4.91 sec)

2. 

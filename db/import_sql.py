"""
This module is to enter the dataset into a SQL db for faster processing
"""

import json
import MySQLdb
import os

def create_db(sql_cursor):
    """
    Create a database for retailrocket if it does not exist
    """

    createdsqldb = "CREATE DATABASE IF NOT EXISTS retailrocket"
    result = sql_cursor.execute(createdsqldb)
    usesqldb = "use retailrocket"
    result = sql_cursor.execute(usesqldb)
    return result

def create_table_items(sql_cursor):
    """
    Create all the tables for CSV files in retailrocket
    if they do not exist
    """

    create_sql_table = "create table \
                       IF NOT EXISTS item_properties (timestamp double, \
                       item long, property varchar(15), value varchar(15));"
    result = sql_cursor.execute(create_sql_table)
    if not sql_cursor.messages:
        os.system(''' mysql -uroot -ppassword --local_infile=1 retailrocket -e\
                     "LOAD DATA LOCAL INFILE 'db/data/item_properties_part1.csv'\
                     INTO TABLE item_properties FIELDS TERMINATED BY ','"
                     ''')
        
        os.system(''' mysql -uroot -ppassword --local_infile=1 retailrocket -e\
                     "LOAD DATA LOCAL INFILE 'db/data/item_properties_part2.csv'\
                     INTO TABLE item_properties FIELDS TERMINATED BY ','"
                     ''')
    return result

def create_table_category(sql_cursor):
    create_sql_table = "create table \
                       IF NOT EXISTS category_tree (categoryid long, \
                       parentid long);"
    result = sql_cursor.execute(create_sql_table)
    if not sql_cursor.messages:
        os.system(''' mysql -uroot -ppassword --local_infile=1 retailrocket -e\
                     "LOAD DATA LOCAL INFILE 'db/data/category_tree.csv'\
                     INTO TABLE category_tree FIELDS TERMINATED BY ','"
                     ''')
    return result

def create_table_events(sql_cursor):
    create_sql_table = "create table \
                       IF NOT EXISTS events (timestamp double, \
                       visitorid long, event varchar(15), itemid long, transactionid long);"
    result = sql_cursor.execute(create_sql_table)
    if not sql_cursor.messages:    
        os.system(''' mysql -uroot -ppassword --local_infile=1 retailrocket -e\
                     "LOAD DATA LOCAL INFILE 'db/data/events.csv'\
                     INTO TABLE events FIELDS TERMINATED BY ','"
                     ''')

if __name__ == '__main__':
    with open("config.json", "r") as config_file:
        CONFIG = json.load(config_file)
    DB = MySQLdb.connect(user=str(CONFIG["mysql_user"]),
                       passwd=str(CONFIG["mysql_password"]))
    CURSOR = DB.cursor()
    RESULT = create_db(CURSOR)
    print "db created.. "
    print CURSOR.execute("show tables;")
    RESULT = create_table_items(CURSOR)
    print CURSOR.execute("show tables;")
    print "items table created.. "
    RESULT = create_table_category(CURSOR)
    print "category table created.. "
    RESULT = create_table_events(CURSOR)
    print "events table created.. "
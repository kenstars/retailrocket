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

def create_table(sql_cursor):
    """
    Create all the tables for CSV files in retailrocket
    if they do not exist
    """

    create_sql_table = "create table \
                       IF NOT EXISTS item_properties (timestamp varchar(20), \
                       item varchar(10), property varchar(15), value integer);"
    try:
        result = sql_cursor.execute(create_sql_table)
    except Warning as warningvariable:
        print "table exists", warningvariable
    else:
        print "in else"
        os.system(''' mysql -uroot -proot --local_infile=1 retailrocket -e
                     "LOAD DATA LOCAL INFILE 'db/item_properties_part1.csv'
                     INTO TABLE item_properties FIELDS TERMINATED BY ','"
                     ''')
    return result


if __name__ == '__main__':
    with open("config.json", "r") as config_file:
        CONFIG = json.load(config_file)
    DB = MySQLdb.connect(user=str(CONFIG["mysql_user"]),
                       passwd=str(CONFIG["mysql_password"]))
    CURSOR = DB.cursor()
    RESULT = create_db(CURSOR)
    RESULT = create_table(CURSOR)
    print RESULT

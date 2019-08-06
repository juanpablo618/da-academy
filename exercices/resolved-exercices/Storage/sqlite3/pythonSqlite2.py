#!/usr/bin/python

import urllib
import codecs

import sqlite3
import time
import requests
from sqlite3 import Error

"""
para hacer update de la base de datos sqlite de alguna calle:
 UPDATE capital_old
   ...> SET domicilio = replace(domicilio, 'P DE LA GASCA', 'Pedro de la Gasca') ;

"""


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
  
def select_all_tasks(conn):
    
    cur = conn.cursor()
    #The final rowid number is 2899005
    
    rowId = 653395;
    finalRowId = 653398;

    cur.execute("select domicilio from capital_old where rowid between "+str(rowId)+" and "+str(finalRowId)+";")
 
    rows = cur.fetchall()
 
    for row in rows:
        time.sleep(10)
        
        row = str(row)
        row = row.replace("u'","")
        row = row.replace("',","")
        row = row.replace("    )","")
        row = row.replace("(","")
        
        #print(row.decode("unicode_escape"))
        r = requests.get("http://buscador.telexplorer.com/scripts/search_xml.asp?q="+row.decode("unicode_escape")+"&location=c%C3%B3rdoba")
        #print("text:")
        #print(r.text)
        #print("r status code:")
        #print(r.status_code)
        #print("r.content:")
        print(row.decode("unicode_escape"))
        print(r.content)
        print(str(rowId))
        print("-----------------------")

        cur.execute("update capital_old set telefono='"+r.content+"' where rowid="+str(rowId)+";")
        rowId = rowId + 1;

def main():
    database = "/home/developer/Downloads/padroncba.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. conecting...")
        select_all_tasks(conn)
 

if __name__ == '__main__':
    main()
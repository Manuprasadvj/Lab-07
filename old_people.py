"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
import sqlite3
import pandas as pd


def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    old_ppl_query = """
        SELECT name, age FROM people
        WHERE age >= 50;
        """
    
    cur.execute(old_ppl_query)
    query_outcome = cur.fetchall()
    con.close()
    
    return query_outcome

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body
    for n, a in name_and_age_list:
        print(f'{n} is {a} year old.')
   

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    header_row = ['Name', 'Age']
    old_people_df = pd.DataFrame(name_and_age_list, columns=header_row)
    old_people_df.to_csv(csv_path, index=False)
    return

if __name__ == '__main__':
   main()
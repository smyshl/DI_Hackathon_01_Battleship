import psycopg2

import random
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DBNAME = 'battleship'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
TABLE = 'fleets'


def create_database() -> None:
    with psycopg2.connect(dbname="postgres", user=USER, password=PASSWORD, host=HOST, port=PORT) as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sqlCreateDatabase = f"create database '{DBNAME}';"
        cursor.execute(sqlCreateDatabase)


def create_table(name: str) -> None:
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        query = f'''
            CREATE TABLE cars (
            id serial PRIMARY KEY,
            data TEXT);
        '''
        cursor.execute(query)

def save_fleet_to_db(data_list: list) -> None:
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        data = ",".join(data_list)
        query = f'''
            INSERT INTO {TABLE}(fleet)
            VALUES
                ('{data});
        '''
        cursor.execute(query)


def load_random_list_from_db(data_list: list) -> list:
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT) as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        query = f'''
            SELECT data FROM {TABLE};
        '''
        cursor.execute(query)
        data = cursor.fetchall()       # list of tuple
        data_str:str = data[random(len(data))][0]
        return data_str.split(",")

def main():
    create_database()
    create_table(TABLE)


if __name__ == "__main__":
    main()

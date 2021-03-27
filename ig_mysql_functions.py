from mysql.connector import connect, Error
from getpass import getpass

exit_value = 6

def mysql_login():
    try:
        sql_host = input("Enter host (enter for localhost): ") or "localhost"
        sql_user = input("Enter username (enter for root): ") or "root"
        sql_password = getpass("Enter password (hint: hello): ")

        with connect(
            host=sql_host,
            user=sql_user,
            password=sql_password,
            ) as connection:
            #print(connection)

            #--- Show Databases ---
            with connection.cursor() as cursor:
                cursor.execute('SHOW DATABASES')
                databases = cursor.fetchall()
                print('\nExisting Databases: ')
                for db in enumerate(databases):
                    print(db)
        
            #cursor = connection.cursor()
        
        answer = int(input('\nEnter database number (Enter for database 0): ') or 0)
        if answer in range(len(databases)):
            print(f'Selected database: {databases[answer][0]}.')
            table_options(sql_host, sql_user, sql_password, databases[answer][0])
        
        #cursor.execute("CREATE DATABASE ig_users") to create database first time

    except Error as e:
        print(e)

def table_options(sql_host, sql_user, sql_password,sql_database):
    try:
        with connect(
            host=sql_host,
            user=sql_user,
            password=sql_password,
            database=sql_database,
            ) as connection:

            cursor = connection.cursor()

            #--- Show Table Options ---
            with cursor as cursor:

                show_tables(cursor)
                option = menu2()

                while option != exit_value:
                    if option == 1:
                        create_table(cursor)
                    if option == 2:
                        show_tables(cursor)
                    if option == 3:
                        show_tables(cursor)
                        describe_table(cursor)
                    if option == 4:
                        show_tables(cursor)
                        show_content_table(cursor)
                    if option == 5:
                        show_tables(cursor)
                        delete_table(cursor)

                    option = menu2()


    except Error as e:
        print(e)

def menu2():

    while True:
        print(
            "\nSQL Menu\n"
            "1 - Create new table 'followers' \n"
            "2 - Show tables\n"
            "3 - Describe specific table\n"
            "4 - Show table contents\n"
            "5 - Delete Table\n"
            "6 - Exit\n")

        try:
            answer = int(input('Enter a value (1 - 6):  '))
        except ValueError:
            print('\nInvalid input. Enter a value between 1 - 6: ')
            continue
        if not answer in range(1, (exit_value+1)):
            print('\nInvalid input. Enter a value between 1 - 6: ')
            continue

        return answer

def show_tables(cursor):
    cursor.execute('SHOW TABLES')
    print('\nExisting Tables: ')
    for tables in enumerate(cursor):
        print(tables)

def describe_table(cursor):

    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    
    answer = int(input('\nEnter table number (Enter for table 0): ') or 0)
    if answer in range(len(tables)):
        print(f'Selected table: {tables[answer][0]}.')
        cursor.execute(f'DESCRIBE {tables[answer][0]}')
        result = cursor.fetchall()
        for row in result:
            print(row)

def create_table(cursor):
    create_table_query = """
    CREATE TABLE followers (
        username VARCHAR(30) PRIMARY KEY,
        followed_count INT,
        follower_count INT,
        post_count INT,
        follows_viewer VARCHAR(8),
        requested_by_viewer VARCHAR(8))"""
    cursor.execute(create_table_query)

def show_content_table(cursor):
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    
    answer = int(input('\nEnter table number to show (Enter for table 0): ') or 0)
    if answer in range(len(tables)):
        print(f'Selected table: {tables[answer][0]}.')
        cursor.execute(f'SELECT * FROM {tables[answer][0]}')
        
        #show_tables(cursor)

        result = cursor.fetchall()
        for row in result:
            print(row)

def delete_table(cursor):
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    
    answer = int(input('\nEnter table number to drop (Enter for table 0): ') or 0)
    if answer in range(len(tables)):
        print(f'Selected table: {tables[answer][0]}.')
        cursor.execute(f'DROP TABLE {tables[answer][0]}')
        
        show_tables(cursor)

def insert_followers_ig_users_followers(sql_followers_array):
    try:
        sql_host = input("Enter host (Enter for localhost): ") or "localhost"
        sql_user = input("Enter username (Enter for root): ") or "root"
        sql_password = getpass("Enter password (hint: hello): ")

        with connect(
            host=sql_host,
            user=sql_user,
            password=sql_password,
            database="ig_users",
            ) as connection:

            #--- Insert into ig_users array key values ---
            with connection.cursor() as cursor:
                for account in sql_followers_array:

                    insert_followers_table_query = f"""INSERT INTO followers
                    (username,followed_count,follower_count,post_count,follows_viewer,requested_by_viewer)
                    VALUES
                    ('{account.get('username')}',
                    '{account.get('followed_count')}',
                    '{account.get('follower_count')}',
                    '{account.get('post_count')}',
                    '{account.get('follows_viewer')}',
                    '{account.get('requested_by_viewer')}')
                    """
                    #print(insert_followers_table_query)

                    cursor.execute(insert_followers_table_query)

                cursor.execute("SELECT * FROM followers")
                people = cursor.fetchall()

                print("\nData in table followers: ")
                for person in people:
                    print(person)
                
                ## --- COMMIT DATABASE ---
                connection.commit()

    except Error as e:
        print(e)


if __name__ == '__main__':
    mysql_login()
    pass
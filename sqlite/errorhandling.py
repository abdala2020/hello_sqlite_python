import sqlite3
import traceback

# Create and add sample data

try:
    db = sqlite3.connect('my_second_db.db')  # Creates or opens database file

    cur = db.cursor()  # Need a cursor object to perform operations

    # Create a table
    cur.execute('create table if not exists phones (brand text, version int)')

    # Add some data
    cur.execute('insert into phones values ("Android", 5)')
    cur.execute('insert into phones values ("iPhone", 6)')

    db.commit()  # Save changes

# This will catch all database errors. You might also want to
# catch distinct errors separately e.g. IntegrityError or OperationalError, depending on context
except sqlite3.Error as e:

    # Handle error in an appropriate way for your application
    # You might want to roll back changes since the last commit, try again,
    # quit the program, log/report the error, something else...
    print('rolling back changes because of error:', e)
    traceback.print_exc()   # Displays a stack trace, useful for debugging
    db.rollback()    # Optional - depends on what you are doing with the db


finally:
    # The finally block always runs if an error occurs or not.
    # This is a good place to close the db connection
    print('closing database')  # Close database in a finally block
    db.close()


# Read some data from DB

try:

    db = sqlite3.connect('my_second_db.db')  # Creates or opens database file
    c = db.cursor()

    # Fetch some data, using the cursor. This returns another cursor object
    # that can be iterated over
    for row in c.execute('select * from phones'):
        print(row)

except sqlite3.Error as e:
    # As we are reading, no changes to roll back
    print('Error reading from database')
    print(e)

finally:
    db.close()


# Delete table

try:

    db = sqlite3.connect('my_second_db.db')  # Creates or opens database file
    c = db.cursor()
    c.execute('drop table phones')  # Delete table
    db.commit()  # Ask the database to save changes

except sqlite3.Error as e:
    # As we are reading, no changes to roll back
    print('Error deleting phones table from database')
    print(e)

finally:
    db.close()

import sqlite3
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

# Connect to database
conn = sqlite3.connect('exercise.db')

# Create a cursor
cur = conn.cursor()


# The below code is commented out because an "exercise" table has already been created.
# If you'd like, you may delete the "exercise.db" file, uncomment lines 18-23, and run this script again to create 
# an empty db.

# cur.execute("""CREATE TABLE exercise(   
#              activity_type text,
#              activity_duration integer,
#              calories_burnt,
#              activity_date text
#             )""")



# Show all records
def show_all():
    print("\nACTIVITY    | DURATION    | CALORIES    | DATE")
    print("---------------------------------------------------------")
    cur.execute("SELECT * FROM exercise")
    activities = cur.fetchall()
    for activity in activities:
        print(activity[0].ljust(11, ' ') + "   " + str(activity[1]).ljust(11, ' ') + "   " + str(activity[2]).ljust(11, ' ') + "   " + activity[3].ljust(6, ' '))

        conn.commit()

# Add one record
def add_record():
    activity =  input(Fore.GREEN + "What type of activity did you engage in?: ")
    duration = int(input(Fore.GREEN + "How long was the activity (in minutes)?: "))
    calories = int(input(Fore.GREEN + "How many calories did you burn?: "))
    date = input(Fore.GREEN + "On what date was this activity performed(YYYY-MM-DD)?: ")
    print("\n")
    cur.execute(f"INSERT INTO exercise VALUES (?,?,?,?)",(activity, duration, calories, date))

    conn.commit()

    print(Fore.GREEN + "The activity was successfully added.")

# Remove one record
def remove_record():
    print("\nID  | ACTIVITY    | DURATION    | CALORIES    | DATE")
    print("---------------------------------------------------------")
    cur.execute("SELECT rowid, * FROM exercise")
    activities = cur.fetchall()
    for activity in activities:
        print(str(activity[0]).ljust(3, ' ') + "   " + activity[1].ljust(11, ' ') + "   " + str(activity[2]).ljust(11, ' ') + "   " + str(activity[3]).ljust(11, ' ')  + "   " + activity[4].ljust(6, ' '))
        conn.commit()
    
    delete_index = input("\nPlease enter the ID number of the row you would like to remove: ")
    cur.execute(f"DELETE FROM exercise WHERE rowid ={delete_index}")

    print(Fore.GREEN + "The row has been successfully deleted.")

# Modify a record
def modify_record():
    print("\nID  | ACTIVITY    | DURATION    | CALORIES    | DATE")
    print("---------------------------------------------------------")
    cur.execute("SELECT rowid, * FROM exercise")
    activities = cur.fetchall()
    for activity in activities:
        print(str(activity[0]).ljust(3, ' ') + "   " + activity[1].ljust(11, ' ') + "   " + str(activity[2]).ljust(11, ' ') + "   " + str(activity[3]).ljust(11, ' ')  + "   " + activity[4].ljust(6, ' '))
        conn.commit()
    
    modify_index = int(input("\nPlease enter the ID number of the row you would like to modify: "))

    activity =  input(Fore.GREEN + "What type of activity did you engage in?: ")
    duration = int(input(Fore.GREEN + "How long was the activity (in minutes)?: "))
    calories = int(input(Fore.GREEN + "How many calories did you burn?: "))
    date = input(Fore.GREEN + "On what date was this activity performed(YYYY-MM-DD)?: ")

    cur.execute(f"""UPDATE exercise SET activity_type =?,
                                        activity_duration =?,
                                        calories_burnt =?,
                                        activity_date =?
                                        WHERE rowid =?""", (activity, duration, calories, date, modify_index))
    
    print(Fore.GREEN + "The row has been successfully updated.")







import sqlite3

connection = sqlite3.connect("movies.db")
print("Connection established")
cursor = connection.cursor()

run = True
query = "SELECT * FROM movies"
while(run):
    # query = input("Please enter a query (quit to exit program): ")
    if query == "quit":
        break
    cursor.execute(query)
    print(cursor.fetchall())

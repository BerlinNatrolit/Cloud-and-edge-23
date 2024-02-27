import sqlite3
import pprint

def mainMenu():
    print("""
1. add game
2. add developer
3. add publisher
4. see all games
5. see game with id
6. quit
""")
    return int(input("please enter your choice: "))

def addGame(cursor):
    title = input("please enter game title: ")
    
    print(pprint.pformat(cursor.execute("SELECT id, name FROM publishers").fetchall()))
    publisher = input("please enter publisher id: ")
    
    print(pprint.pformat(cursor.execute("SELECT id, name FROM developers").fetchall()))
    developer = input("please enter developer id: ")
    
    print(pprint.pformat(cursor.execute("SELECT id, category FROM categories").fetchall()))
    category = input("please enter category id: ")
    
    price = input("please enter game price: ")
    score = input("please enter Metacritic score: ")
    description = input("please enter game description: ")
    
    query = "INSERT INTO games(title, publisher, developer, category, price, score, description) VALUES('"+title+"','"+publisher+"','"+developer+"','"+category+"','"+price+"','"+score+"','"+description+"')"
    cursor.execute(query)

def addDeveloper(cursor):
    name = input("please enter developer name: ")
    location = input("please enter developer location: ")
    query = "INSERT INTO developers(name, location) VALUES('" + name + "','" + location + "')"
    cursor.execute(query)

def addPublisher(cursor):
    name = input("please enter publisher name: ")
    location = input("please enter publisher location: ")
    reputation = input("please enter publisher reputation: ")
    query = "INSERT INTO publishers(name, location, reputation) VALUES('" + name + "','" + location + "','" + reputation + "')"
    cursor.execute(query)
    
def seeAllGames(cursor):
    query = "SELECT * FROM games"
    cursor.execute(query)
    print(cursor.fetchall())
    
def seeGameId(cursor):
    id = input("please enter game id: ")
    query = "SELECT games.title, games.price, games.score, games.description, publishers.name, publishers.location, publishers.reputation, developers.name, developers.location FROM games LEFT JOIN publishers ON games.publisher = publishers.id LEFT JOIN developers ON games.developer = developers.id WHERE games.id=" + id
    # Dont do this.
    # query = "SELECT * FROM games LEFT JOIN publishers ON games.publisher = publishers.id LEFT JOIN developers ON games.developer = developers.id WHERE games.id=" + id
    cursor.execute(query)
    print(cursor.fetchone())
    response = cursor.fetchone()
    
    print("Title: " + response[0])
    print("Price: " + str(response[1]))
    print("Metacritic score: " + str(response[2]))
    print("Publisher: " + response[4])
    print("Publisher location: " + response[5])
    print("Publisher reputation: " + response[6])
    print("Developer: " + response[7])
    print("Developer location: " + response[8])
    print("description:\n===================\n" + response[3])
    
    
if __name__ == "__main__":
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()

    run = True
    while run:
        choice = mainMenu()
        if choice == 1:
            addGame(cursor)
        elif choice == 2:
            addDeveloper(cursor)
        elif choice == 3:
            addPublisher(cursor)
        elif choice == 4:
            seeAllGames(cursor)
        elif choice == 5:
            seeGameId(cursor)
        elif choice == 6:
            run = False
            
        connection.commit()
        
    connection.close()
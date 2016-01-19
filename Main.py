import sqlite3

option = ''

# Creates a connection to the db
conn = sqlite3.connect('bobbleheads.db')
# Points to the db used
c = conn.cursor()
# Creates a new table if it doesn't exist yet
c.execute('''CREATE TABLE IF NOT EXISTS Collectors (name TEXT, bobbleheads int, country TEXT)''')
# c.execute("INSERT INTO collectors VALUES ('Jesse', '10')")
# Commits table creation
conn.commit()

# Menu GUI
def menu():
    print("Welcome to the Bobblehead Collector!\n\nMenu\n1. Add new collector\n2. Add bobbleheads\n"
          "3. Search records\n4. Delete records\n5. View records")
    optionInput = input("Select an option: ")
    optionInt = int(optionInput)
    if optionInt <= 1 and optionInt >=4:
        menu()
    else: return optionInt

# def connectCreate():
#     conn = sqlite3.connect('bobbleheads.db')
#     c = conn.cursor()
#
#     c.execute('''CREATE TABLE IF NOT EXISTS Collectors (name TEXT, bobbleheads int, country TEXT)''')
#     conn.commit()

# Generic record creation
def recordInput():
    collector = input("Collector name: ")
    bobbles = input("Bobbleheads: ")
    bobblesInt = int(bobbles)
    country = input("Country: ")

    # Makes a list for the created entry
    recordData = [(collector, bobblesInt, country)]

    return recordData

# May need to be converted to int
def bobbleInput():
    bobbles = input("Bobbles to add: ")

    return bobbles

def nameInput():
    name = input("Name to search/add to: ")
    return name

def countryInput():
    country = input("Country: ")
    return country

# Adds new record to the table using generic input method
def newCollector():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    recordData = recordInput()

    c.executemany('INSERT INTO Collectors VALUES (?,?,?)', recordData)
    conn.commit()

def addBobble():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    nameInp = nameInput()
    bobblesInp = bobbleInput()
    c.execute('UPDATE Collectors'
              'SET bobbleheads = ' + bobblesInp +
              'WHERE name = ' + nameInp)
    conn.commit()

def search():
    return 0

def delete():
    return 0

def viewRecords():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Collectors")
    print(c.fetchall())

viewRecords()

option = menu()

if option == 1:
    newCollector()
if option == 2:
    addBobble()
if option == 3:
    search()
if option == 4:
    delete()
if option == 5:
    viewRecords()

conn.commit()
conn.close()
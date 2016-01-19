import sqlite3

option = ''

conn = sqlite3.connect('bobbleheads.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Collectors (name TEXT, bobbleheads int, country TEXT)''')
# c.execute("INSERT INTO collectors VALUES ('Jesse', '10')")
conn.commit()

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

def recordInput():
    collector = input("Collector name: ")
    bobbles = input("Bobbleheads: ")
    bobblesInt = int(bobbles)
    country = input("Country: ")

    recordData = [(collector, bobblesInt, country)]

    return recordData

def bobbleInput():
    bobbles = input("Bobbles to add: ")
    bobblesInt = int(bobbles)
    return bobblesInt

def nameInput():
    name = input("Name to search/add to: ")
    return name

def countryInput():
    country = input("Country: ")
    return country

def newCollector():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    recordData = recordInput()

    c.executemany('INSERT INTO Collectors VALUES (?,?,?)', recordData)
    conn.commit()

def addBobble():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    name = nameInput()
    c.execute('UPDATE Collectors'
              'SET bobbleheads = ' + bobbleInput() +
              'WHERE name LIKE '' + name + ''')
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

# viewRecords()

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

conn.close()
import sqlite3

option = ''

def menu(option):
    print("Welcome to the Bobblehead Collector!\n\nMenu\n1. Add new collector\n2. Add bobbleheads\n"
          "3. Search records\n4. Delete records\n5. View records")
    option = input("Select an option: ")
    optionInt = int(option)
    if optionInt <= 1 and optionInt >=4:
        menu(option)
    else: return option

def connectCreate():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Collectors (name TEXT, bobbleheads INTEGER, country TEXT)''')
    conn.commit()

def recordInput():
    collector = input("Collector name: ")
    bobbles = input("Bobbleheads: ")
    country = input("Country: ")

    recordData = [(collector, bobbles, country)]

    return recordData

def newCollector():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    c.executemany('INSERT INTO Collectors VALUES (?,?,?)', recordInput())

def addBobble():
    conn = sqlite3.connect('bobbleheads.db')
    c = conn.cursor()
    data = recordInput()
    nameData = data[0]
    bobbleData = data[1]
    c.execute('INSERT INTO Collectors(bobbleheads) VALUES (?) WHERE name = ' + nameData, bobbleData)

def search():
    return 0

def delete():
    return 0

def viewRecords():
    c.execute("SELECT * FROM Collectors")
    print(c.fetchall())

option = menu(option)

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

connectCreate()

conn = sqlite3.connect('bobbleheads.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Collectors (name TEXT, bobbleheads INTEGER)''')
# c.execute("INSERT INTO collectors VALUES ('Jesse', '10')")
conn.commit()

conn.close()
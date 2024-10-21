import sqlite3

connection = sqlite3.connect("people.sqlite")
c = connection.cursor()
# query = """
# SELECT * FROM friends
# WHERE l_name = "Goldman"
# """
#
# query2 = """
# UPDATE friends SET email = "nauajs.email@gmail.com"
# WHERE l_name = "Jonaitis"
# """
#
# query3 = """
# DELETE FROM friends
# WHERE l_name = "Pakenas"
# """
name = input("Enter a name: ")
query4 = f"SELECT * FROM friends WHERE f_name =?" #dedami klaustuka, apsaugom nuo " OR 1=1--"

# c.execute(query)
# connection.commit() #uztvirina pakeitimus
# connection.close() #uzdarom connection

with connection: # be uzdarymo
    #c.execute(query)
    #record = (c.fetchone()) #istraukiam 1 elementa
    #print(record)
    #c.execute(query)
    #allrecords = (c.fetchall()) # istraukiam visus israsus su filtru where kur naudojom virsuje
    #print(allrecords)
    #c.execute(query2) # pasileidziam info is query2
    #c.execute(query3) # pasileidziam info is query3
    c.execute(query4, (name,))
    result = c.fetchall()
if len(result) > 0:
    print(result)
else:
    print("No such name!")

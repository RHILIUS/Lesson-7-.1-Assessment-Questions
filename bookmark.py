import os
import sqlite3

def add():

  # User input 
  title = input("Enter Title: ")
  url = input("Enter URL: ")
  os.system('cls')


  try:
      # Connect to SQLite database
  
      conn = sqlite3.connect("Bookmarks.db")
      cursor = conn.cursor()

      # SQL statement with placeholders
      strSQL = """
          INSERT INTO Bookmark (
              Title, URL
          ) VALUES (
              ?, ?
          )
      """
      
      # Execute the SQL statement with parameters
      cursor.execute(strSQL, (title, url))

      # Commit the transaction
      conn.commit()
      print("Record inserted successfully")

  except sqlite3.Error as error:
      print("Error inserting data:", error)

  finally:
      # Close the connection
      if conn:
          conn.close()

def edit():


    try:
        # Connect to SQLite database
       
        conn = sqlite3.connect("Bookmarks.db")
        cursor = conn.cursor()

        id = input("Number of bookmark to edit: ")
        url = input("URL: ")
        title = input("Title: ")


        # SQL statement with placeholders
        strSQL = f"""
            UPDATE Bookmark 
            SET Title = ?, URL = ?
            WHERE Bk_ID = ?
        """
        
        # Execute the SQL statement with parameters
        cursor.execute(strSQL, (title, url, id))

        # Commit the transaction
        conn.commit()
        print(f"Update successful")

    except sqlite3.Error as error:
        print("Error updating data:", error)

    finally:
        # Close the connection
        if conn:
            conn.close()
def list():
  
  print("Bookmarks: ")

  #connect to sqlite database
  
  conn = sqlite3.connect("Bookmarks.db")

  #SELECT statement
  strSQL = "SELECT * FROM Bookmark"

  #execute() methods run sql query
  cursor = conn.execute(strSQL)

  #fetchall() method to fetch the data
  rows = cursor.fetchall()

  # Determine the size of the longest id
  idColLength = 2
  for row in rows:
      string = str(row[0])
      currID = len(string)
      if currID > idColLength:
          idColLength = currID
  
  # Determine the size of the longest title
  titleColLength = 0
  for row in rows:
      currID = len(row[1])
      if currID > titleColLength:
          titleColLength = currID
  
  
  # #loop into to cursor to get rows individually
  # for row in rows:
  #     print(row)
  
  # column header
  print("ID", end="")
  for i in range(len("ID"), idColLength):
     print(" ", end="")
  print(" Book Title", end="")
  for i in range(len("Book Title"), titleColLength):
     print(" ", end="")

  print(" URL")
  # Rows
  for row in rows:
    # ID
    print(f"{row[0]}", end="")
    string = str(row[0])
    currID = len(string)
    for i in range(currID,idColLength):
       print(" ", end="")
    print("|", end="")

    # Book Title
    currTitle = len(row[1])
    print(row[1], end="")
    for i in range(currTitle, titleColLength):
      print(" ", end="")

    print("|", end="")

    # URL
    print(row[2])

  #close cursor
  cursor.close()

  #close connection
  conn.close()

def remove():
  try:
      # Connect to SQLite database

      conn = sqlite3.connect("Bookmarks.db")
      cursor = conn.cursor()

      # SQL statement with placeholders for delete
      idToDelete = int(input("Enter Book ID to remove: "))

      strSQL = f"""
          DELETE FROM Bookmark
          WHERE Bk_ID = ?
      """

      # Execute the SQL statement with parameters
      cursor.execute(strSQL, (idToDelete,))

      # Commit the transaction
      conn.commit()
      print(f"Record(s) where Bk_ID is '{idToDelete}' deleted successfully")

  except sqlite3.Error as error:
      print("Error deleting data:", error)

  finally:
      # Close the connection
      if conn:
          conn.close()
def quit():
  print("Goodbye, have a great day!")
  exit()

  
def main_window():
  # Heading
  print("==========================================")
  function_to_execute = input("\n(A)dd (E)dit (L)ist (R)emove (Q)uit : ")
  function_to_execute = function_to_execute.upper()

  if function_to_execute == "A":
    os.system('cls')
    add()
    main_window()
  elif function_to_execute == "E":
    os.system('cls')
    edit()
    main_window()
  elif function_to_execute == "L":
    os.system('cls')
    list() 
    main_window()
  elif function_to_execute == "R":
    os.system('cls')
    remove()
    main_window()
  elif function_to_execute == "Q":
     os.system('cls')
     quit()
  else:
     os.system('cls')
     print("Please enter a valid input!")
     main_window()



main_window()






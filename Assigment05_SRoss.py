# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: A program that utilizes dictionaries and lists to create a
#              text file holding a user-inputted task and its priority.
#              User also has the ability to update and delete items as
#              they choose.
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
#  SRoss,02/12/2022,Added code to complete part of assignment 5
#  SRoss, 02/13/2022,Continued to work through code troubleshooting along
#  the way
#  SRoss, 02/14/2022, Finalized the assignment. Still having trouble deleting
#  items. Changed the way the items were stored in the dictionaries and
#  succesfully got items to delete with input of index number
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strObjFile = ""
strData = ""  # A row of text data from the file
strTask = ""  # Inputted task
strChoice = ""  # Choice for user
strPriority = ""  # Inputted priority
dicTaskPriority = {}  # dictionary to hold task and priority
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# try-except block because causing a non-existent file was causing errors
try:
    print("The following is currently on your agenda: ")
    print()  # Adding a new line for looks
    objFile = open("ToDoList.txt", 'r')
    for row in objFile:
        lstRow = row.split(",")  # Returns a list!
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        print(dicRow)
        lstTable.append(dicRow)
    objFile.close()
    input("press ENTER to continue: ")
except:
    print("    Your agenda is empty.")
    print("    What would you like to do?")

# Initialize Menu of options
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """
strObjFile = "ToDoList.txt"

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table

    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        try:
            if [lstTable] == []:
                print("your agenda is empty!")
            else:
                for ObjRow in lstTable:
                    print(ObjRow)
        except:
            print("lstTable variable empty, choose another option: ")
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("What task would you like to enter?: ")
        print()  # adding a new line for looks
        strPriority = input("Type the priority for this task - low/med/high: ")
        dicTaskPriority = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicTaskPriority)
        print("'" + strTask + "'", "has been added to your agenda with a", strPriority, "priority.")
        input("press ENTER to continue")

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        for ObjRow in lstTable:
            print(ObjRow)
        strChoice = input("which index would you like to delete? (0 is the first item on your agenda )")
        lstTable.pop(int(strChoice))

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("Data saved to", strObjFile, sep="--")

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("The program has ended")
        break  # and Exit the program

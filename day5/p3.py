
import sys
def insertRecord():
        print("record inserted")
def deleteRecord():
        print("record deleted")
def updateRecord():
        print("record updated")
def searchrecord():
        print("record searched")
def listAllRecord():
        print("record listed")
def exit_program():
        sys.exit("End of program")



def get_menu():
    menu = {
        1 : insertRecord,
        2 : deleteRecord,
        3 : updateRecord,
        4 : searchrecord,
        5 : listAllRecord,
        6 : exit_program,
    }
    return menu
def start_app():
    choice = 0
    while True:
        print('1:creat,2:delete,3:update,4.seracg,5:listAll,6:exit')
        choice = int(input("enter your choice"))
        menu = get_menu()
        menu.get(choice())
        choice = input("do you wish to continue? type 1 for yes, anything for no ")

start_app()

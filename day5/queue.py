import sys

def insertElement(queue):
    element = input('Enter the element to be pushed: ')
    queue.append(element)

def deleteElement(queue): # Mutator
    if len(queue) == 0:
        print('queue is empty')
        return
    print(f'Popped element is {queue[-1]}')
    del queue[-1]

def listqueue(queue): # Accessor
    if len(queue) == 0:
        print('Stack is empty')
        return
    print(f'The queue is {queue}')



def exit_program(queue):
    sys.exit('End of Program')

def invalid_choice(queue):
    print('Invalid choice entered')

def get_menu(choice, queue):
    menu = {
        1 : insertElement,
        2 : deleteElement,
        3 : listqueue,
        4 : exit_program
    }
    menu.get(choice, invalid_choice)(queue)

def start_app(queue):
    choice = 0
    while True:
        print('1insert 2:Pop 3:ListQueue 4:Exit')
        choice = int(input('Enter your choice: '))
        get_menu(choice, queue)

queue = [] # this list is gonna work as Stack
start_app(queue)
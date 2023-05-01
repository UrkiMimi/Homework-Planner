#init list
list = []
origlist = []
alpha = []

#functions
def main_1():
    print('**Homework Planner** \n 1. Add to homework planner\n 2. View homework planner\n 3. Delete item from homework planner\n 4. Sort List\n 5. Exit')
    inp = input('')
    if inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5':
        return inp
    else:
        print("Please enter a valid response")
        main_1()

def add_list():
    inp=input('What do you want to add? ')
    inp2=input('What time is it due?')
    return str(len(list)+1) + '. ' + str(inp) + " " + str(inp2)

def del_list():
    inp=int(input('Enter the number of what item you want to delete'))
    x=inp-1
    list.pop(x)
    origlist.pop(x)

def sort(list, origlist):
    print('How would you like to sort the list?')
    print(' 1. Sort by number\n 2. Sort by letter')
    inp = input('')
    if inp == '1':
        return origlist
    elif inp == '2':
        return sorted(list)
    
#init part 2 electric boogalo
while True:
    inp = main_1()
    if inp == '1':
        list.append(add_list())
    elif inp == '2':
        print('Current Homework Planner')
        print('\n'.join(map(str, list)))
        input('')
    elif inp == '3':
        del_list()
    elif inp == '4':
        list = sort(list, origlist)
    elif inp == '5':
        break
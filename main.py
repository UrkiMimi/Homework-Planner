#init list
list = []

#functions
def main_1():
    print('**Homework Planner** \n 1. Add to homework planner\n 2. View homework planner\n 3. Delete item from homework planner\n 4. Exit')
    inp = input('')
    if inp == '1' or inp == '2' or inp == '3' or inp == '4':
        return inp
    else:
        print("Please enter a valid response")
        main_1()

def add_list():
    inp=input('What do you want to? ')
    return inp

#init part 2 electric boogalo
while True:
    inp = main_1()
    if inp == '1':
        list.append(add_list())
    if inp == '2':
        print('Current Homework Planner')
        print('\n'.join(map(str, list)))
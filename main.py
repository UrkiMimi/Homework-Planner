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
    input=input('what do you want to add')
    return input
#init part 2 electric boogalo
inp = main_1()
if inp == '1':
    #Run Add to List
    print('h')
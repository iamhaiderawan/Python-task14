user_input='random'

data = {'comfort' : 'rahat', 'red' : 'surkh', 'care' : 'parvah'}

def showmenu():

    print("\n\t--Dictionary--")
    print("\n\tMenu: ")
    print("1. Enter a word you want to search:  ")
    print("2. View all words in Dictionary: ")
    print("3. Exit: ")


while user_input != '3':
    showmenu()
    user_input=input("\tEnter your Choice: ")

    if user_input == '1':
        item = input("Enter a word you want to Search:")
        if item in data:

            print('\t',data[item])
        else:
            print("Word does not exist in the Dictionary")
    elif user_input == '2':
        print(data)
    elif user_input == '3':
        print("\tGood Bye")

'''
Provides a basic frontend
'''
import sys
import timeit
from playhouse.dataset import DataSet
import main


def load_users():
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    main.load_users(filename)
    print("The time difference is :", timeit.default_timer() - starttime)


def load_status_updates():
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')
    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    main.load_status_updates(filename)
    print("The time difference is :", timeit.default_timer() - starttime)


def add_user():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.add_user(user_id, email, user_name, user_last_name, social_network_db):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")
    print("The time difference is :", timeit.default_timer() - starttime)


def update_user():
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    
    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.update_user(user_id, email, user_name, user_last_name, social_network_db):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")
    print("The time difference is :", timeit.default_timer() - starttime)


def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    result = main.search_user(user_id, social_network_db)
    print("The time difference is :", timeit.default_timer() - starttime)

    if not result or result is None:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Email: {result['EMAIL']}")
        print(f"Name: {result['NAME']}")
        print(f"Last name: {result['LASTNAME']}")


def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.delete_user(user_id, social_network_db):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")
    print("The time difference is :", timeit.default_timer() - starttime)


def add_status():
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.add_status(status_id, user_id, status_text, social_network_db):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")
    print("The time difference is :", timeit.default_timer() - starttime)


def update_status():
    '''
    Updates information for an existing status
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.update_status(status_id, user_id, status_text, social_network_db):
        print("An error occurred while trying to update status")
    else:
        print("Status was successfully updated")
    print("The time difference is :", timeit.default_timer() - starttime)


def search_status():
    '''
    Searches a status in the database
    '''
    status_id = input('Enter status ID to search: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    result = main.search_status(status_id, social_network_db)
    print("The time difference is :", timeit.default_timer() - starttime)

    if not result:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result['USER_ID']}")
        print(f"Status ID: {result['STATUS_ID']}")
        print(f"Status text: {result['STATUS_TEXT']}")


def delete_status():
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')

    starttime = timeit.default_timer()
    print("The start time is :", starttime)
    if not main.delete_status(status_id, social_network_db):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")
    print("The time difference is :", timeit.default_timer() - starttime)


def quit_program():
    '''
    Quits program
    '''
    sys.exit()


if __name__ == '__main__':
    social_network_db = DataSet('sqlite:///social_network.db')
    menu_options = {
        # 'A': print(timeit.timeit(stmt=timeme, number=1)),
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")

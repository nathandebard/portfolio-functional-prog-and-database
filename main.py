import csv
from functools import partial, reduce
from playhouse.dataset import DataSet
import users
import user_status


def load_users(filename):
    '''
    Requirements:
    - If a user_id already exists, it will ignore it and continue to the next.
    - Returns False if there are any errors (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    db = DataSet('sqlite:///social_network.db')
    db['users'].delete()  # Start with a new db every time we load a file for the sake of the demo.
    db['statuses'].delete()
    # db['users'].thaw(filename=filename, format='csv')  # how to load and still check data validity by using thaw()??

    # TO DO:  Use multiprocessing with this.  Break into chunks, could probably load several times faster.
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel')  # an iterable

        def csv_reader_row(reader_list):
            return reader_list['USER_ID'], reader_list['EMAIL'], reader_list['NAME'], reader_list['LASTNAME']

        reader_rows = map(csv_reader_row, reader)

        db_loaded_successfully = reduce(lambda x, y: x and y, map(partial(users.add_user, db=db), reader_rows))
        return db_loaded_successfully


def add_user(user_id, email, user_name, user_last_name, db):
    '''
    Requirements:
    - user_id cannot already exist in db
    - Returns False if there are any errors
    - Otherwise, it returns True.
    '''
    return users.add_user([user_id, email, user_name, user_last_name], db)


def update_user(user_id, email, user_name, user_last_name, db):
    '''
    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return users.modify_user(user_id, email, user_name, user_last_name, db)


def delete_user(user_id, db):
    '''
    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    return users.delete_user(user_id, db)


def search_user(user_id, db):
    '''
    Requirements:
    - If the user is found, returns the corresponding user's info
    - Otherwise, it returns None.
    '''
    return users.search_user(user_id, db)


def load_status_updates(filename):
    '''
    Requirements:
    - If a status_id already exists, it will ignore it and continue to the next.
    - Returns False if there are any errors (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    db = DataSet('sqlite:///social_network.db')
    db['statuses'].delete()

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect='excel')

        def csv_reader_row(reader_list):
            return reader_list['STATUS_ID'], reader_list['USER_ID'], reader_list['STATUS_TEXT']

        reader_rows = map(csv_reader_row, reader)

        no_errors = reduce(lambda x, y: x and y, map(partial(user_status.add_status, db=db), reader_rows))
        return no_errors


def add_status(status_id, user_id, status_text, db):
    '''
    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    return user_status.add_status([status_id, user_id, status_text], db)


def update_status(status_id, user_id, status_text, db):
    '''
    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return user_status.modify_status(status_id, user_id, status_text, db)


def delete_status(status_id, db):
    '''
    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    return user_status.delete_status(status_id, db)


def search_status(status_id, db):
    '''
    Requirements:
    - If the status is found, returns the corresponding info
    - Otherwise, it returns None.
    '''
    return user_status.search_status(status_id, db)

from peewee import IntegrityError
import users


def status_data_valid(status_id, user_id, status_text):
    if user_id == '' or status_id == '' or status_text == '':
        return False
    if user_id.isspace() or status_id.isspace() or status_text.isspace():
        return False
    return True


def add_status(status_info, db=None):
    status_id = status_info[0]
    user_id = status_info[1]
    status_text = status_info[2]

    if status_data_valid(status_id, user_id, status_text) is False:
        return False

    if users.search_user(user_id, db) is None:  # Can't add a status to a non-existant user_id
        return False

    # db['statuses'].create_index(['STATUS_ID'], unique=True)
    if db['statuses'].find_one(STATUS_ID=status_id) is not None:
        return False

    try:
        db['statuses'].insert(STATUS_ID=status_id, USER_ID=user_id, STATUS_TEXT=status_text)
    except IntegrityError:
        return False

    return True


def search_status(status_id, db=None):
    return db['statuses'].find_one(STATUS_ID=status_id)


def modify_status(status_id, user_id, status_text, db=None):
    if status_data_valid(status_id, user_id, status_text) is False:
        return False

    if db['statuses'].find_one(STATUS_ID=status_id) is None:
        return False

    db['statuses'].update(STATUS_ID=status_id, USER_ID=user_id, STATUS_TEXT=status_text)

    return True


def delete_status(status_id, db=None):
    if db['statuses'].find_one(STATUS_ID=status_id) is None:
        return False

    db['statuses'].delete(STATUS_ID=status_id)

    return True

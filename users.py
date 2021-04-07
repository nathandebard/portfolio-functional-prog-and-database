from peewee import IntegrityError


def user_data_valid(user_id, email, user_name, user_last_name):
    if user_id == '' or email == '' or user_name == '' or user_last_name == '':
        return False
    if user_id.isspace() or email.isspace() or user_name.isspace() or user_last_name.isspace():
        return False
    if '@' not in email or '.' not in email:
        return False
    if not user_last_name.isalpha() and '\'' not in user_last_name and '-' not in user_last_name:
        return False
    if not user_name.isalpha() and '\'' not in user_name and '-' not in user_name:
        return False

    if len(user_id) > 30:
        return False
    if len(user_name) > 30:
        return False
    if len(user_last_name) > 100:
        return False

    return True


def add_user(user_info, db=None):
    user_id = user_info[0]
    email = user_info[1]
    user_name = user_info[2]
    user_last_name = user_info[3]

    if user_data_valid(user_id, email, user_name, user_last_name) is False:
        return False

    # Should I put this somewhere else?
    # This keeps giving me problems, so I'm doing the two lines below it instead.
    # db['users'].create_index(['USER_ID'], unique=True)
    if db['users'].find_one(USER_ID=user_id) is not None:
        return False

    try:
        db['users'].insert(NAME=user_name, EMAIL=email, USER_ID=user_id, LASTNAME=user_last_name)
    except IntegrityError:  # if inserting a non-unique USER_ID, this will be raised.
        return False

    return True


def modify_user(user_id, email, user_name, user_last_name, db=None):
    if user_data_valid(user_id, email, user_name, user_last_name) is False:
        return False

    if db['users'].find_one(USER_ID=user_id) is None:
        return False

    db['users'].update(NAME=user_name, EMAIL=email, USER_ID=user_id, LASTNAME=user_last_name)

    return True


def delete_user(user_id, db=None):
    if db['users'].find_one(USER_ID=user_id) is None:
        return False

    db['users'].delete(USER_ID=user_id)

    # # if the status has this user as its user, delete the status, too
    if db['statuses'].find_one(USER_ID=user_id):
        db['statuses'].delete(USER_ID=user_id)

    return True


def search_user(user_id, db=None):
    return db['users'].find_one(USER_ID=user_id)

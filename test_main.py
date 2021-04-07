import os
import pytest
from playhouse.dataset import DataSet
import main


# This test will run first due to alphabetical ordering of test file names and then function names.
# I think ordering tests is a bad idea to rely on, but I do want to delete the db file first every time.
def test_1():
    if os.path.isfile('social_network.db'):
        os.remove('social_network.db')


@pytest.fixture
def db():
    social_network_db = DataSet('sqlite:///social_network.db')
    social_network_db['users'].delete()
    social_network_db['statuses'].delete()

    social_network_db['users'].insert(USER_ID='')
    social_network_db['users'].delete(USER_ID='')
    social_network_db['users'].insert(EMAIL='')
    social_network_db['users'].delete(EMAIL='')
    social_network_db['users'].insert(NAME='')
    social_network_db['users'].delete(NAME='')
    social_network_db['users'].insert(LASTNAME='')
    social_network_db['users'].delete(LASTNAME='')

    social_network_db['statuses'].insert(STATUS_ID='')
    social_network_db['statuses'].delete(STATUS_ID='')
    social_network_db['statuses'].insert(USER_ID='')
    social_network_db['statuses'].delete(USER_ID='')
    return social_network_db


def test_load_users(db):
    assert main.load_users('accounts_small.csv') is True
    print(list(db['users']))
    assert list(db['users']) == [{'id': 1, 'NAME': 'Eve', 'EMAIL': 'eve.miles@uw.edu', 'USER_ID': 'evmiles97', 'LASTNAME': 'Miles'},
                                 {'id': 2, 'NAME': 'David', 'EMAIL': 'david.yuen@gmail.com', 'USER_ID': 'dave03', 'LASTNAME': 'Yuen'},
                                 {'id': 3, 'NAME': 'Alvaro', 'EMAIL': 'aconejo@conejo.com', 'USER_ID': 'alcon49', 'LASTNAME': 'Conejo'}]


def test_add_user(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is False
    assert main.search_user("test1", db) == {'id': 1, 'NAME': 'tester', 'EMAIL': 'email@gmail.com', 'USER_ID': 'test1', 'LASTNAME': 'one'}


def test_update_user(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.update_user("test1", "email@gmail.com", "newfirstname", "one", db) is True
    assert main.update_user("this_id_does_not_exist", "email@gmail.com", "new_first_name", "one", db) is False


def test_delete_user(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.search_user('test1', db) == {'id': 1, 'NAME': 'tester', 'EMAIL': 'email@gmail.com', 'USER_ID': 'test1', 'LASTNAME': 'one'}
    assert main.delete_user("test1", db) is True
    assert main.delete_user('test1', db) is False
    assert main.delete_user('test2', db) is False
    assert main.search_user('test1', db) is None


def test_search_user(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.search_user('test1', db) == {'id': 1, 'NAME': 'tester', 'EMAIL': 'email@gmail.com', 'USER_ID': 'test1', 'LASTNAME': 'one'}
    assert main.search_user('test2', db) is None


def test_load_status_updates(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.add_status("test1_status_id", "test1", "test_status_text", db) is True
    assert main.add_status("test1_status_id", "bad_user_id", "test_status_text", db) is False


def test_update_status(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.add_status("test1_status_id", "test1", "test_status_text", db) is True
    assert main.update_status("test1_status_id", "test1", "NEW_status_text", db) is True


def test_delete_status(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.add_status("test1_status_id", "test1", "test_status_text", db) is True
    assert main.delete_status("test1_status_id", db) is True
    assert main.delete_status("bad_status_id", db) is False


def test_search_status(db):
    assert main.add_user("test1", "email@gmail.com", "tester", "one", db) is True
    assert main.add_status("test1_status_id", "test1", "test_status_text", db) is True
    assert main.search_status("test1_status_id", db) == {'id': 1, 'STATUS_ID': 'test1_status_id', 'USER_ID': 'test1', 'STATUS_TEXT': 'test_status_text'}
    assert main.search_status("badstatus_id", db) is None

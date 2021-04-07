import pytest
from playhouse.dataset import DataSet
import users
import user_status


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


def test_add_user(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is False


def test_modify_user(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert users.modify_user("test1", "new_email@gmail.com", "tester", "one", db) is True
    assert users.modify_user("user_id_not_in_db", "lolwhat@gmail.com", "tester", "me", db) is False
    assert users.search_user("test1", db) == {'id': 1, 'NAME': 'tester', 'EMAIL': 'new_email@gmail.com', 'USER_ID': 'test1', 'LASTNAME': 'one'}


def test_delete_user(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert users.add_user(("test2", "email@gmail.com", "tester", "two"), db) is True

    assert user_status.add_status(["test1_status_id", "test1", "test status text"], db) is True

    assert users.delete_user("test1", db) is True
    assert list(db['users']) == [{'id': 2, 'NAME': 'tester', 'EMAIL': 'email@gmail.com', 'USER_ID': 'test2', 'LASTNAME': 'two'}]

    assert user_status.search_status("test1_status_id", db) is None


def test_search_user(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert users.search_user("test1", db) == {'id': 1, 'NAME': 'tester', 'EMAIL': 'email@gmail.com', 'USER_ID': 'test1', 'LASTNAME': 'one'}
    assert users.search_user("test2", db) is None


def test_user_data_valid():
    assert users.user_data_valid("test1", "email@gmail.com", "tester", "one") is True
    assert users.user_data_valid("test2", "email@gmail.com", "tester", "O'Malley") is True
    assert users.user_data_valid("test3", "email@gmail.com", "tester", "Ocassio-Cortez") is True
    assert users.user_data_valid("test4", "email_missing_at_gmail.com", "tester", "one") is False
    assert users.user_data_valid("test5", "email@missing_period", "tester", "one") is False
    assert users.user_data_valid("test6", "email@gmail.com", "  ", "one") is False
    assert users.user_data_valid("test7", "email@gmail.com", "", "one") is False
    assert users.user_data_valid("test8", "email@gmail.com", "Mary-Ann", "one") is True
    assert users.user_data_valid("test9", "email@gmail.com", "B@b", "one") is False
    assert users.user_data_valid("test10", "email@gmail.com", "Yenn123", "one") is False
    assert users.user_data_valid("test11", "email@gmail.com", "tester", "B@b") is False
    assert users.user_data_valid("test12", "email@gmail.com", "tester", "Yenn123") is False

    assert users.user_data_valid("this_is_an_exceedingly_long_user_id", "email@gmail.com", "tester", "Yenn123") is False
    assert users.user_data_valid("test13", "email@gmail.com", "this_is_an_exceedingly_long_name", "Yenn123") is False
    assert users.user_data_valid("test14", "email@gmail.com", "tester",
                                 "this_is_an_exceedingly_long_last_name_this_is_an_exceedingly_long_last_name_this"
                                 "_is_an_exceedingly_long_last_name_this_is_an_exceedingly_long_last_name") is False

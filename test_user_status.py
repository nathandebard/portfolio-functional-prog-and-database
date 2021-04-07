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


def test_add_status(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test status text"], db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test status text"], db) is False
    assert user_status.add_status(["test1_status_id", "Non_existant_user_id", "test status text"], db) is False


def test_search_status(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test me"], db) is True
    assert user_status.search_status("test1_status_id", db) == {'id': 1, 'STATUS_ID': 'test1_status_id', 'USER_ID': 'test1', 'STATUS_TEXT': 'test me'}
    assert user_status.search_status("another_status_id", db) is None


def test_modify_status(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test status text"], db) is True
    assert user_status.modify_status("test1_status_id", "test1", "new status text", db) is True
    assert user_status.modify_status("status_id_not_in_db", "test1", "some status", db) is False
    assert user_status.modify_status("status_id_not_in_db", "baduserid", "some status", db) is False


def test_delete_status(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test status text"], db) is True
    assert user_status.delete_status("test1_status_id", db) is True
    assert user_status.delete_status("test1_status_id", db) is False
    assert user_status.delete_status("other_status_id", db) is False


def test_status_data_valid():
    assert user_status.status_data_valid("test_status_id", "test_user_id", "test text") is True
    assert user_status.status_data_valid("test_status_id123!@#", "test_user_id123!@#", "test text123!@#") is True
    assert user_status.status_data_valid(" ", "test_user_id", "test text") is False
    assert user_status.status_data_valid("", "test_user_id", "test text") is False


def test_delete_user_and_its_statuses(db):
    assert users.add_user(("test1", "email@gmail.com", "tester", "one"), db) is True
    assert user_status.add_status(["test1_status_id", "test1", "test me"], db) is True
    assert user_status.search_status("test1_status_id", db) == {'id': 1, 'STATUS_ID': 'test1_status_id', 'USER_ID': 'test1', 'STATUS_TEXT': 'test me'}

    assert users.delete_user("test1", db) is True
    assert user_status.search_status("test1_status_id", db) is None

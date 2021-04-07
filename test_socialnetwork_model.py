# from peewee import SqliteDatabase
# from socialnetwork_model import StatusTable, UserTable


# def test_basic_sqllite():
#     db = SqliteDatabase(':memory:')
#     db.connect()
#     db.create_tables([UserTable])

#     for user in UserTable.select():
#         user.delete_instance()

#     assert UserTable.get_or_none(UserTable.user_id == 'evmiles97') is None

#     new_user = UserTable.create(user_id='evmiles97', user_email='eve.miles@uw.edu',
#                                 user_name='Eve', user_last_name='Miles')
#     new_user.save()

#     assert UserTable.get(UserTable.user_id == 'evmiles97').user_id == 'evmiles97'
#     # OR (return none if not found in the line below)
#     assert UserTable.get_or_none(UserTable.user_id == 'evmiles97').user_id == 'evmiles97'
#     # OR
#     UserTable.get(UserTable.user_id == 'evmiles97')
#     for user in UserTable.select():
#         print(user.user_id)

#     db.close()


# def test_basic_sqllite_linked_tables():
#     db = SqliteDatabase(':memory:')
#     db.connect()
#     db.create_tables([UserTable, StatusTable])

#     for status in StatusTable.select():
#         status.delete_instance()
#     for user in UserTable.select():
#         user.delete_instance()

#     assert UserTable.get_or_none(UserTable.user_id == 'evmiles97') is None

#     new_user = UserTable.create(user_id='evmiles97', user_email='eve.miles@uw.edu',
#                                 user_name='Eve', user_last_name='Miles')
#     new_user.save()

#     assert UserTable.get_or_none(UserTable.user_id == 'evmiles97')
#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001') is None

#     new_status = StatusTable.create(status_id='evmiles97_00001', user=new_user, status_text='Code is finally compiling')
#     new_status.save()

#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001')
#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001').status_id == 'evmiles97_00001'
#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001').user == new_user
#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001').status_text == 'Code is finally compiling'
#     assert StatusTable.get_or_none(StatusTable.status_id == 'evmiles97_00001').user.user_id == 'evmiles97'

#     db.close()

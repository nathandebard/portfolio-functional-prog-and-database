Example of using databases and functional programming (when reasonably possible).
In particular, see load_users() and/or load_status_updates() in main.py for functional programming.

There is a file of users and some info about them.  There is a file of statuses associated with certain users.  Files are loaded into a database, social_network.db, and then you manipulate the .db. 

If you have a system with few things, but need to potentially add a lot of logic over time (but not new things), functional programming can excel. And functional programs, when well written, are easy to test.  PeeWee now supports an extension that should allow a more functional approach to interfacing to a database for Python. Its is called DataSet, and its documentation is at docs.peewee-orm.com/en/latest/peewee/playhouse.html#dataset

I put the .venv directory in .gitignore, so you'll have to make the venv and then install all the packagesfrom requirements.txt:
python -m venv .venv
Then to activate it:
ctrl+shift+p, Python:select interpreter, choose the '.ven' version of the interpreter
Activate the new virtual environment terminal
Ctrl+Shift+`
Update pip in the virtual environment
python -m pip install --upgrade pip
Finally, get all the extensions needed:
pip install -r requirements.txt

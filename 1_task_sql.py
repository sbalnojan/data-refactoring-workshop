
SQL = "SELECT (SELECT SUM(AA.facevalue) FROM (SELECT clients.client_id, clients.name, trades.facevalue FROM clients \
INNER JOIN trades ON clients.client_id=trades.client_id AND \
(clients.name LIKE '%Purple%')) AA) * 100 / (SELECT SUM(facevalue) FROM trades) AS Frac"

## 1. Now let's see how we would execute this

from sqlalchemy import create_engine

engine = create_engine('sqlite:///bookstore.db')

con=engine.connect()
con.execute(SQL)
con.close()

## 2. Of course this fails, because the tables are not there...
from sqlalchemy import create_engine

engine = create_engine('sqlite:///bookstore.db')

con=engine.connect()

def test_sql_executes():

    con.execute(SQL)
    con.close()


## 3. Fix it

class dummyConnection:
    def execute(self, sql):
        return 1
    def close(self):
        return 1

con = dummyConnection()

test_sql_executes()

## 4.

class dummyConnection:
    def execute(self, sql):
        return ("foo")
    def close(self):
        return 1

con = dummyConnection()

def test_sql_returns_result():
    res = con.execute(SQL)
    con.close()
    assert len(res) > 0

## 5. Test it works against real tables?
from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric

##clients.client_id, clients.name, trades.facevalue FROM clients
## trades ON clients.client_id=trades.client_id...

metadata = MetaData()
clients = Table('clients', metadata,
  Column('client_id', Integer),
  Column('name', String),
)

trades = Table('trades', metadata,
  Column('client_id', Integer),
  Column('facevalue', Numeric),
)

engine = create_engine('sqlite:///bookstore.db')
metadata.create_all(engine)

con=engine.connect()


def test_sql_executes_real_data():
    res = con.execute(SQL)
    con.close()

## 6. Now let's see what this thing actually does...

from sqlalchemy import insert

def test_sql_returns_data():
    stmt_1 = (
        insert(trades).
        values(client_id=1, facevalue=100.1)
    )

    stmt_2 = (
        insert(clients).
        values(client_id=1, name="Purple Cow")
    )

    con=engine.connect()
    con.execute(stmt_1)
    con.execute(stmt_2)
    res = con.execute(SQL)

for row in res:
    print(row)

    assert == ...;

## Notice, we just got our first business logic test!


# ---- now let's refactor!
## 7. Ok, now we got one test, which seems to be enough right? Let's do some refactoring!

SQL = " WITH client_trade_history AS (SELECT clients.client_id, clients.name, trades.facevalue FROM clients \
    INNER JOIN trades ON clients.client_id=trades.client_id AND \
    (clients.name LIKE '%Purple%'))" \
      "SELECT " \
      "(SELECT SUM(AA.facevalue) FROM AA * 100 / (SELECT SUM(facevalue) FROM trades) AS Frac"


## Now finally, let's do a small piece of refactoring here inside this one thing... now
## we could simply test the complete result, or we could test the unit.
## If you wanted to test the unit, which is there because you now named it, you could do so!

...
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect



import psqlparse
SQL = "With a as (select * from b), d as (select e from c) select * from a "
statements = psqlparse.parse(SQL)
stmt = statements[0]
used_tables = statements[0].tables()  # ['my_table']

with_clauses = stmt.with_clause
print(with_clauses)

a = with_clauses.queries["a"]

str(a)

stmt.nodes


Each object can be converted back to a string at any time:

https://sqlparse.readthedocs.io/en/latest/intro/#getting-started
# Let's start some SQL 
https://github.com/santoshmungle/Some-complex-SQL-Queries-and-solution/blob/master/SQL%20Queries%20Part1.sql


# Your Task!
Hey Y, can you quickly adapt ```1_task_sql.sql``` to also 
include trades with clients whos name includes the word "green", thanks!

Go!

# Oh wait, we might need to understand how to add a test first.... Ok
so let's do this one together...

# Step 0 wrap everything... 



We're completely free now, so let us use a simple process to get 
modular pieces of SQL we can test... 


Since we're completely free right now, let's use python for now:
https://github.com/andialbrecht/sqlparse
will help us, and then we'll just use default pytest.

First, let's create a super simple mock with the data, run it against it,
see what it returns, then refactor.




http://silab.fon.bg.ac.rs/wp-content/uploads/2016/10/Refactoring-Improving-the-Design-of-Existing-Code-Addison-Wesley-Professional-1999.pdf






Query 4. In 2015, due to government incentives, a significant proportion of trades were from clients with the word ‘Green’ or the word ‘Purple’ in their names. 
What fraction of total facevalue for the year can be attributed to these companies? 





We got these tables:
```
Usage:
These queries meant to give you an understanding of sql queries for analyzing data in database.
In this part, there are following 3 tables in the database:

2) Table: salesreps
   columns: salesrep_id (pk), first_name, last_name
 
 
 1) Table: trades
    columns: trade_id (pk), client_id, trade_datetime, facevalue, revenue    
    
 3) Table: clients
    columns: client_id (pk), name, assigned_salesrep_id, signup_datetime,   churn_datetime 
************************************************************************************************/

```

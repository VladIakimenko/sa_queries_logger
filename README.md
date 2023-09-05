The QueryLogger class in Python is a context manager designed to log SQL queries executed by a SQLAlchemy engine. It logs the following data:  

    *Database URL*: The URL of the database that the queries are being executed against. This is logged when the QueryLogger context manager is entered.

    *Time entered*: The time when the QueryLogger context manager is entered. This marks the beginning of the period during which queries are being logged.

    *SQL queries*: Each SQL query that is executed within the QueryLogger context manager is logged. The exact SQL statement is logged, along with the time it was executed.

    *Time exited*: The time when the QueryLogger context manager is exited. This marks the end of the period during which queries were being logged.

    *Total queries executed*: The total number of SQL queries that were executed within the QueryLogger context manager. This is logged when the context manager is exited.

    *Total execution time*: The total time, in seconds, that it took to execute all the SQL queries within the QueryLogger context manager. This is calculated as the difference between the time the context manager was entered and the time it was exited. This is also logged when the context manager is exited.  

The QueryLogger writes all these logs to a file. The name of the file can be specified when creating an instance of QueryLogger. If no file name is specified, it defaults to 'queries.log'.


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< INJECTION BEGINS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from datetime import datetime
from sqlalchemy import event


class QueryLogger:
    def __init__(self, engine, log_file_name='queries.log'):
        self.engine = engine
        self.log_file_name = log_file_name
        self.query_count = 0
        self.start_time = None

    def log_sql(self, conn, cursor, statement, *args):
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(f"\n\nTime: {datetime.now()}")
            log_file.write("\nSQL: " + statement)
            self.query_count += 1

    def __enter__(self):
        self.start_time = datetime.now()
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(f"\n\n\n\tDatabase URL: {self.engine.url}\n")
            log_file.write(f"\tTime entered: {self.start_time}\n")
        event.listen(self.engine, "before_cursor_execute", self.log_sql)

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds()

        with open(self.log_file_name, 'a') as log_file:
            log_file.write(f"\n\n\n\tTime exited: {end_time}\n")
            log_file.write(f"\tTotal queries executed: {self.query_count}\n")
            log_file.write(f"\tTotal execution time: {elapsed_time} seconds\n\n\n")

        event.remove(self.engine, "before_cursor_execute", self.log_sql)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INJECTION ENDS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# assuming current sa session is stored as "session"
with QueryLogger(session.get_bind()):
    # code fragment to log the queries from

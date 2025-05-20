from sqlalchemy import create_engine, Connection
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.pool import QueuePool, NullPool


# database connection URL
DATABASE_CONN = "mysql+mysqlconnector://root:todos@127.0.0.1:3307/blog_db"
engine = create_engine(DATABASE_CONN,
                       poolclass=QueuePool,
                       pool_size=10, max_overflow=0)

def direct_get_conn():
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(e)
        raise e

def context_get_conn():
    try:
        with engine.connect() as conn:
            return conn
    except SQLAlchemyError as e:
        print(e)
        raise e
    finally:
        conn.close()
        print("###### connection yield is finished")
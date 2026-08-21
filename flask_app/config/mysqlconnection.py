import os
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # Connection settings come from environment variables so real
        # credentials never have to live in the source code / git repo.
        # Locally, set these in a .env file (see .env.example). In
        # production, set them as environment variables on the host.
        connect_kwargs = dict(
            host = os.environ.get('DB_HOST', 'localhost'),
            user = os.environ.get('DB_USER', 'root'),
            password = os.environ.get('DB_PASSWORD', ''),
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True,
        )
        # Managed MySQL providers (e.g. Aiven) require an SSL connection.
        # Set DB_SSL_CA to the path of the downloaded CA certificate to
        # enable it; leave it unset for a plain local connection.
        ssl_ca = os.environ.get('DB_SSL_CA')
        if ssl_ca:
            connect_kwargs['ssl_ca'] = ssl_ca
            connect_kwargs['ssl_verify_cert'] = True
        connection = pymysql.connect(**connect_kwargs)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
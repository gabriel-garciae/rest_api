import psycopg2

class PostgreeSQLConnection:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def select_user(self, query):
        if not self.conn:
            print("Not connected to the database")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            print(f"Error selecting user: {e}")
            return None

    def insert_user():
        pass

    def update_user():
        pass

    def delete_user():
        pass

    def close(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from the database")
        else:
            print("Not connected to the database")
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

    def insert_user(self, id, nome, empresa, cargo, anos_experiencia, salario, is_ativo, qualidade_servico):
        if not self.conn:
            print("Not connected to the database")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (id, nome, empresa, cargo, anos_experiencia, salario, is_ativo, qualidade_servico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (id, nome, empresa, cargo, anos_experiencia, salario, is_ativo, qualidade_servico)
            )
            self.conn.commit()
            cursor.close()
            print("User inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting user: {e}")
            return None

    def update_user(self, id, name=None, empresa=None, cargo=None, anos_experiencia=None, salario=None, is_ativo=None, qualidade_servico=None ):
        if not self.conn:
            print("Not connected to the database")
            return None
        try:
            cursor = self.conn.cursor()
            update_query = "UPDATE users SET"
            update_values = []

            if name is not None:
                update_query += " nome = %s,"
                update_values.append(name)

            if empresa is not None:
                update_query += " empresa = %s,"
                update_values.append(empresa)

            if cargo is not None:
                update_query += " cargo = %s,"
                update_values.append(cargo)

            if anos_experiencia is not None:
                update_query += " anos_experiencia = %s,"
                update_values.append(anos_experiencia)

            if salario is not None:
                update_query += " salario = %s,"
                update_values.append(salario)

            if is_ativo is not None:
                update_query += " is_ativo = %s,"
                update_values.append(is_ativo)

            if qualidade_servico is not None:
                update_query += " qualidade_servico = %s,"
                update_values.append(qualidade_servico)

            update_query = update_query.rstrip(",") + " WHERE id = %s"
            update_values.append(id)

            cursor.execute(update_query, update_values)
            self.conn.commit()
            cursor.close()
            print("User updated successfully")
        except psycopg2.Error as e:
            print(f"Error updating user: {e}")
            return None
            
    def delete_user(self, user_id: int):
        if not self.conn:
            print("Not connected to the database")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM users WHERE id = %s",
                (user_id,)
            )
            self.conn.commit()
            cursor.close()
            print("User deleted successfully")
        except psycopg2.Error as e:
            print(f"Error deleting user: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from the database")
        else:
            print("Not connected to the database")
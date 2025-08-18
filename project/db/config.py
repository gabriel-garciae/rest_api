import os
from typing import Optional

class DatabaseConfig:
    """Configurações do banco de dados PostgreSQL"""
    
    def __init__(self):
        # Try to load from environment variables, otherwise use default values
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', '5432'))
        self.database = os.getenv('DB_NAME', 'rest_api_db')
        self.user = os.getenv('DB_USER', 'postgres')
        self.password = os.getenv('DB_PASSWORD', 'postgres123')
    
    def get_connection_string(self) -> str:
        """Returns the connection string for psycopg2"""
        return f"host={self.host} port={self.port} dbname={self.database} user={self.user} password={self.password}"
    
    def get_connection_params(self) -> dict:
        """Returns the connection parameters as a dictionary"""
        return {
            'host': self.host,
            'port': self.port,
            'dbname': self.database,
            'user': self.user,
            'password': self.password
        }

# Global instance of the configuration
db_config = DatabaseConfig() 